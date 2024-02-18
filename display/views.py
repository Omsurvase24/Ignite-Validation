from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    response = requests.get(
        'https://mpulse-ignite-backend.up.railway.app/api/register').json()
    return render(request, 'home.html', {'response': response})


def info(request):
    return render(request, 'info.html')
