# Generated by Django 2.2.9 on 2020-02-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0015_quoteprocessvariations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoteprocess',
            name='deductible',
            field=models.PositiveIntegerField(blank=True, choices=[(750, '750'), (1000, '1000'), (1500, '1500')], null=True, verbose_name='Physical Coverage'),
        ),
    ]
