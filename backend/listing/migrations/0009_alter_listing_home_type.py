# Generated by Django 4.2.3 on 2023-08-04 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0008_rename_decription_listing_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='home_type',
            field=models.CharField(choices=[('House', 'House'), ('Condo', 'Condo'), ('Townhouse', 'Townhouse')], default='House', max_length=225),
        ),
    ]
