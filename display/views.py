from django.shortcuts import render
import requests
# Create your views here.
from urllib.parse import quote


def home(request):
    response = requests.get(
        'https://mpulse-ignite-backend.up.railway.app/api/register').json()

    sorted_response = sorted(response, key=lambda x: x.get('event_name', 0))
    entries = [{'first_name': entry['first_name'], 'last_name': entry['last_name'],
                'payment_id': entry['payment_id']} for entry in sorted_response]

    return render(request, 'home.html', {'entries': entries})


def info(request, name, payment_id):
    response = requests.get(
        'https://mpulse-ignite-backend.up.railway.app/api/register').json()

    full_name = f"{name} {payment_id}"
    encoded_full_name = quote(full_name)

    selected_entry = next(
        (entry for entry in response if name in entry['first_name'] + ' ' + entry['last_name'] and entry['payment_id'] == payment_id), None)

    return render(request, 'info.html', {'entry': selected_entry})
