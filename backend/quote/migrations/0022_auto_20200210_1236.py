# Generated by Django 2.2.10 on 2020-02-10 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0021_auto_20200209_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quoteprocessdocuments',
            name='broker_of_record',
        ),
        migrations.AddField(
            model_name='quoteprocessdocuments',
            name='is_broker_of_record_signed',
            field=models.BooleanField(default=False, verbose_name='Broker of Record Change'),
        ),
    ]
