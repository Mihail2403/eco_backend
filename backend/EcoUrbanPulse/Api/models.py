from django.db import models
from django.dispatch import receiver
from datetime import timedelta, datetime
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

# Пользователи
class User(models.Model):
    user_name = models.CharField(max_length=255, null=False)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    tg_id = models.CharField(max_length=255, null=True)
    permition_id = models.ForeignKey('Permition', on_delete=models.CASCADE, null=False)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE, null=True)
    raiting = models.IntegerField(null=False, default=3)
    eco_scores = models.IntegerField(null=False, default=0)


# Права
class Permition(models.Model):
    name = models.CharField(max_length=50)


# Жалобы
class Complaint(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cords = ArrayField(models.FloatField(null=False)) #координаты
    rate = models.FloatField(null=True)
    text = models.CharField(max_length=255, default=False, null=True)
    photo = models.ImageField(upload_to='photos/', null=True)
    air = models.BooleanField(null=True, default=False)
    plants = models.BooleanField(null=True, default=False)
    environment = models.BooleanField(null=True, default=False)
    clear = models.BooleanField(null=True, default=False)
    water_obj = models.BooleanField(null=True, default=False)
    final_eval = models.FloatField(null=True, default=0)
    address = models.CharField(max_length=50, null=False, default='')


# Статус запроса на уборку
class RequsetStatus(models.Model):
    name = models.CharField(max_length=255, null=False, default='')


# Запрос на уборку
class Request(models.Model):
    complain_id = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    status_id = models.ForeignKey(RequsetStatus, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)


# Обновление типа звпроса на уборку, если он "провисел" в открытых задачах сутки (24 часа)
@receiver(post_save, sender=Request)
def update_request_status(sender, instanse, **kwargs):
    if datetime.now() - instanse.last_update > timedelta(days=1) and instanse.last_update.name == 'В работе':
        current_clean_request = RequsetStatus.objects.get(name='Передано в администрацию')
        instanse.last_update = current_clean_request
        instanse.save()


# Регион (имена и id)
class Region(models.Model):
    name = models.CharField(max_length=255, null=False, default='')


# Новости
class News(models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=255)
    adress = models.CharField(max_length=100)
