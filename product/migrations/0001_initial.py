# Generated by Django 4.0.5 on 2022-06-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('expiry', models.DateField(null=True)),
            ],
        ),
    ]
