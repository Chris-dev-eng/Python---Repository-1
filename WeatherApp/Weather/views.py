import requests
from django.shortcuts import render

def weather_view(request):
    weather_data = None
    city = request.GET.get('city', 'Nairobi')  

    if city:
        api_key = 'bce879469fd94099e4ac465e347c09e5'  
        api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(api_url)
        if response.status_code == 200:
            weather_data = response.json()

    return render(request, 'weather/weather.html', {'weather_data': weather_data, 'city': city})
