# Generated by Django 4.2 on 2023-08-12 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=255)),
                ('adress', models.CharField(max_length=100)),
            ],
        ),
    ]
