from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

list = []

path = 'C:\Users\Vlad\AppData\Roaming\Python\Python312\site-packages\django\django__________DZ\dj-homeworks\1.2-requests-templates\pagination\pagination\settings.py'
with open(path, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list += row['Name'], row['Sreet'], row['District']


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    paginator = Paginator(list, 10)
    page = paginator.get_page(1)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
 #        'bus_stations': ...,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
