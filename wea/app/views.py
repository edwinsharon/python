from django.shortcuts import render
import requests
from .models import *
# Create your views here.
def index(request):
    context={}
    city='kochi'
    
    key='be35cc5517d57c9f68c1cc0cd18a9d6d'
    
    

    if request.method=="POST":
        if "mycity" in request.POST:
            city=request.POST.get("mycity")
    
   
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    
    response=requests.get(url)
   
    # if not data-
    data=response.json()
    
    
  

    weather=data['weather'][0]['description']
    temp=data['main']['temp']
    temp_min= data['main']['temp_min']
    temp_max=data['main']['temp_max']
    feels=data['main']['feels_like']

    context['city']=city
    context['weather']=weather
    context['temp']=temp
    context['temp_min']=temp_min
    context['temp_max']=temp_max
    context['feels_like']=feels
    img=Destination.objects.all()
    context['img']=img
    return render(request,'index.html',context)