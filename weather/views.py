from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render
from django.conf import settings

def get_weather(request):
       weather_data = {}
       if request.method == "POST":
           city = request.POST.get('city')
           api_key = "87efd76957bb3ad88f873338ef265499"  # Replace with your OpenWeatherMap API key
           url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

           response = requests.get(url)
           data = response.json()

           if data.get('cod') == 200:
               weather_data = {
                   'city': data['name'],
                   'temperature': data['main']['temp'],
                   'description': data['weather'][0]['description'].capitalize(),
               }
           else:
               weather_data = {'error': 'City not found. Please try again.'}
               print('weather data',weather_data)

       return render(request, 'index.html', {'weather_data': weather_data})