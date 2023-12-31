# Generated by Django 4.2 on 2023-08-12 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_alter_user_region_id_alter_user_tg_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='category_id',
        ),
        migrations.AddField(
            model_name='complaint',
            name='air',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='complaint',
            name='clear',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='complaint',
            name='environment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='complaint',
            name='final_eval',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='complaint',
            name='plants',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='complaint',
            name='water_obj',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='ComplaintCategory',
        ),
    ]
