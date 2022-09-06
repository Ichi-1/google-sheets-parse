import gspread
import pandas as pd
from apps.google_sheets.utils import get_current_usd_course, send_message
from celery import shared_task
from datetime import datetime, date
from decouple import config
from django.conf import settings
from sqlalchemy import create_engine
from .models import Order
from django.core import serializers


DB_PORT = config("DB_PORT")
DB_HOST = config("DB_HOST")
DB_NAME = config("POSTGRES_DB")
DB_USER = config("POSTGRES_USER")
DB_PASSWORD = config("POSTGRES_PASSWORD")

CBR_USD_COURSE = get_current_usd_course()

@shared_task(name='parse_google_sheet')
def parse_google_sheet():

    # read google api credentials
    service_account = gspread.service_account_from_dict(settings.CREDENTIALS)
    # open sheet from google drive
    sheet = service_account.open("ПоставкаДанные")
    # choose specific sheet
    work_sheet = sheet.worksheet("SupplyDataFirst").get_all_records()


    # transform google sheet to dataframe
    """
    Я удалил колонку "№" из таблицы Google, т.к. 
    считаю что она не несет в себе существенной информации.
    Уникально идентифицировать строку может либо индекс(PK), либо oreder_number,
    а порядок строк(нумерование) в реляционной базе данных ни на что не влияет. 
    
    """
    df = pd.DataFrame.from_dict(work_sheet).drop("№", axis=1)\
        .rename(columns={
        "заказ №": "order_number", 
        "стоимость,$": "value_usd", 
        "срок поставки": "supply_date"
    })

    # parse string-date to datetime object
    df["supply_date"] = df["supply_date"].apply(
        lambda date_string: datetime.strptime(date_string, "%d.%m.%Y").date()
    )
    # add new column value_rub to dataframe
    df["value_rub"] = df["value_usd"].apply(
        lambda value: value*CBR_USD_COURSE
    )

    try:
        engine = create_engine(
            f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )

        df.to_sql('google_sheets_order', engine, if_exists='replace')
        engine.dispose()
        return 'Reading and writing succesfully completed!'

    except BaseException:
        raise ValueError('Cannot write to Database!') 


@shared_task(name='notify_expired_supply')
def notify_expired_supply():
    """
    Осуществляет фильтрацию queryset по отношению к текущей дате.
    Если текущая дата больше чем дата поставки, то поставка просрочена - 
    небходимо отправить уведомление в Telegram: https://t.me/notifyMyExpired
    """
    today = date.today()
    expired_orders = Order.objects.filter(supply_date__lte=today)

    if expired_orders.exists():
        json = serializers.serialize(
            'json', 
            expired_orders.only('order_number', 'supply_date')
        )
    send_message(json)
    
