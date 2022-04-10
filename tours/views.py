from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError

def main_view(request):
    return render(request, 'index.html')

def departure_view(request, departure):
    return render(request, 'departure.html')

def tour_view(request, id):
    return render(request, 'tour.html')

def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')

def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')