# Generated by Django 4.2 on 2023-08-13 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0007_alter_complaint_air_alter_complaint_clear_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
    ]
