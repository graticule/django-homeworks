import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        paginator = Paginator(list(reader), 10)
    page = paginator.get_page(request.GET.get('page', 1))
    print(page)
    context = {
         'bus_stations': page.object_list,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
