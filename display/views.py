from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    response = requests.get(
        'https://mpulse-ignite-backend.up.railway.app/api/register').json()

    sorted_response = sorted(response, key=lambda x: x.get('event_name', 0))
    return render(request, 'home.html', {'response': sorted_response})


def info(request):
    return render(request, 'info.html')
