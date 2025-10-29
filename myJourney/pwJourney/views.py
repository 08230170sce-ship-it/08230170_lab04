from django.shortcuts import render
from .models import LearningJourney

# Create your views here.

def index(request):
    journeys = LearningJourney.objects.all().order_by('-date')
    return render(request, 'index.html', {'journeys': journeys})

def about(request):
    return render(request, 'aboutMe.html')
