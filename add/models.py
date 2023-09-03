from django.db import models
from django.utils.html import format_html
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth import get_user_model


# Create your models here.


User = get_user_model()

class Advert(models.Model):
    title = models.CharField('Заголовок', max_length=128, )
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text=' - Добавить возможность торга')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображения', upload_to='adverts/')
    
    @admin.display(description='Дата создания')
    def creation_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {} </span>', created_time 
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description='Дата последнего обновления')
    def last_updated(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: red; font_weight: bold;">Сегодня в {} </span>', updated_time
            )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S") 
    
    @admin.display(description='Изображение')
    def show_image(self):
        if self.image:
            return format_html(
            '<img src="{}" height="200", width="400">', self.image.url, 
                )
    
    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'
    
    class Meta:
        db_table='advertisements'
    