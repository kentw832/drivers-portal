# Generated by Django 2.2.9 on 2020-02-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0029_quoteprocess_base_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoteprocess',
            name='vehicle_owner',
            field=models.CharField(blank=True, choices=[('owner-driver', 'Owner-Driver Base Rate'), ('owner-named', 'Owner & Named Driver Base Rate'), ('corporate', 'Corporate Scheduled Driver')], max_length=12, null=True, verbose_name='Vehicle Owner'),
        ),
    ]
