# Generated by Django 4.2 on 2023-08-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
