from django.shortcuts import render
from django.http import HttpResponse #Подключение класса для ответа
from .models import Advert

# Create your views here. (создание классов или функций которые по запросу возвращают ответ)

def index(request):
     adverts = Advert.objects.all()
     context={'adverts': adverts}
     return render(request, 'index.html', context)

     
def top_sellers(request):
     return render(request, 'top-sellers.html')


