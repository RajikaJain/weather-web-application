from django.shortcuts import render

# Create your views here.
#edit
import urllib.request
import json

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city +'&units=metric&appid=976baac1ecd42c2b27a7f32340d285d8').read()
        list_of_data = json.loads(source)
        data ={
            "country_code": str(list_of_data['sys'][çountry]),
            "coordinate": str(list_of_data['coord']['lon']) + ',' + str(list_of_data['coord']['lat']),
            "main":  str(list_of_data['weather'][0]['main']),
            "temp": str(list_of_data['main']['temp']),
            "max_temp": str(list_of_data['main']['temp_max']),
            "min_temp":str(list_of_data['main']['temp_min']),
            "pressure": str(list_of_data['main']['pressure']),

            "humidity": str(list_of_data['main']['humidity']),

            "wind": str(list_of_data['wind']['speed']),
            "sunrise": str(list_of_data['sys']['sunrise']),
            "sunset": str(list_of_data['sys']['sunset']),

            
            "description": str(list_of_data['weather'][0]['description'])
            "icon": list_of_data['weather'][0]['icon'],

        }
        print (data)
    else:
        data = {}
    return render(request,"main/index.html",data)    
