from django.shortcuts import render, redirect
from django.http import HttpResponse #Подключение класса для ответа
from .models import Advert
from .forms import AdvertForm
from django.urls import reverse 
# Create your views here. (создание классов или функций которые по запросу возвращают ответ)
     
def index(request):
     adverts = Advert.objects.all()
     context={'adverts': adverts}
     return render(request, 'index.html', context)

     
def top_sellers(request):
     return render(request, 'top-sellers.html')

def advert_post(request):
     if request.method == "POST":
          form = AdvertForm(request.POST, request.FILES)
          if form.is_valid():
               advertisement = Advert(**form.cleaned_data)
               advertisement.user = request.user
               advertisement.save()     
               url = reverse('main-page')
               return redirect(url)
     else:
          form = AdvertForm() 
     context = {'form': form}
     return render(request, 'advertisement-post.html', context)


