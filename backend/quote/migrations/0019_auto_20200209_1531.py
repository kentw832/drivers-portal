# Generated by Django 2.2.9 on 2020-02-09 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0018_quoteprocess_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quoteprocessdocumentsaciddentreport',
            old_name='defensive_driving_certificate',
            new_name='accident_report',
        ),
    ]
