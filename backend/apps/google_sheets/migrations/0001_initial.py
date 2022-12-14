# Generated by Django 4.1.1 on 2022-09-05 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('order_number', models.PositiveIntegerField(verbose_name='Номер заказа')),
                ('value_usd', models.PositiveIntegerField(verbose_name='Стоимость заказа в USD')),
                ('supply_date', models.DateField()),
                ('value_rub', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
