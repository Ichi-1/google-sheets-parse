from django.db import models


class Order(models.Model):

    """
    Я задал первичный ключ явно, поскольку
    для парсинга данных использую pandas, dataframe которого
    предоставляет колонку index.
    Просто что-бы не возникло противоречий между колонками.
    """
    index = models.AutoField(primary_key=True)
    order_number = models.PositiveIntegerField(
        verbose_name='Номер заказа', 
        null=False
    )
    value_usd = models.PositiveIntegerField(
        verbose_name='Стоимость заказа в USD', 
        null=False
    )
    supply_date = models.DateField(null=False)
    value_rub = models.DecimalField(decimal_places=3, max_digits=10)
    
    def __str__(self):
        return (f"Заказ №:{self.order_number}/ "
                f"Стоимость RUB: {self.value_rub}/ "
                f"Стоимость USD {self.value_usd}"
                )
