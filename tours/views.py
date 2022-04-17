from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from tours.data import title, subtitle, description, departures, tours

def main_view(request):
    return render(request, 'index.html', {'title':title, 'subtitle':subtitle, 'description':description, 'departures':departures, 'tours':tours})

def departure_view(request, departure_id):
    departure = departures.get(departure_id)
    tour_count, max_nights, min_nights, max_price, min_price = 0, 0, 999, 0, 99999999

    for num, tour in tours.items():
        if tour.get('departure') == departure_id:
            tour_count = tour_count + 1
        if tour.get('price') > max_price:
            max_price = tour.get('price')
        if tour.get('price') < min_price:
            min_price = tour.get('price')
        if tour.get('nights') > max_nights:
            max_nights = tour.get('nights')
        if tour.get('nights') < min_nights:
            min_nights = tour.get('nights')

    return render(request, 'departure.html', {'title':title, 'subtitle':subtitle, 'description':description, 'departures':departures,
                                              'departure':departure, 'tours':tours, 'departure_id':departure_id,
                                              'tour_count':tour_count, 'max_price':max_price, 'min_price':min_price,
                                              'max_nights':max_nights, 'min_nights':min_nights})

def tour_view(request, tour_id):
    tour = tours.get(tour_id)
    return render(request, 'tour.html', {'title':title, 'subtitle':subtitle, 'description':description, 'departures':departures, 'tour':tour})

def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')

def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')