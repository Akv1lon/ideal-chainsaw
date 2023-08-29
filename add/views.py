from django.shortcuts import render
from django.http import HttpResponse #Подключение класса для ответа

# Create your views here. (создание классов или функций которые по запросу возвращают ответ)

def index(request):
     return render(request, 'index.html')

def top_sellers(request):
     return render(request, 'top-sellers.html')

