from django.shortcuts import render, redirect
from django.http import HttpResponse #Подключение класса для ответа
from .models import Advert
from .forms import AdvertForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy 
# Create your views here. (создание классов или функций которые по запросу возвращают ответ)
     
def index(request):
     adverts = Advert.objects.all()
     context={'adverts': adverts}
     return render(request, 'add/index.html', context)

     
def top_sellers(request):
     return render(request, 'add/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
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
     return render(request, 'add/advertisement-post.html', context)


