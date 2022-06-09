# Generated by Django 4.0.5 on 2022-06-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_quantity', models.IntegerField()),
                ('add_quantity', models.IntegerField(null=True)),
                ('expired_quantity', models.IntegerField(null=True)),
                ('price', models.FloatField()),
                ('date_product', models.DateField()),
            ],
        ),
    ]
