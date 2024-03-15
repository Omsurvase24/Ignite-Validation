from django.shortcuts import render
import requests
from . import api_key
# from decouple import config
# Create your views here.


def home(request):
    response = requests.get(api_key.key).json()

    sorted_response = sorted(response, key=lambda x: x.get('event_name', 0))
    entries = [{'first_name': entry['first_name'], 'last_name': entry['last_name'],
                'payment_id': entry['payment_id'], 'event_name': entry.get('event_name', ''), 'contact': entry.get('contact', '')} for entry in sorted_response]

    return render(request, 'home.html', {'entries': entries})


def info(request, name, payment_id):
    response = requests.get(api_key.key).json()

    selected_entry = next(
        (entry for entry in response if name in entry['first_name'] + ' ' + entry['last_name'] and entry['payment_id'] == payment_id), None)

    return render(request, 'info.html', {'entry': selected_entry})


def listing(request):
    response = requests.get(api_key.key).json()

    return render(request, 'list.html', {'response': response})
