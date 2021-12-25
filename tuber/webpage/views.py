from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtuber



def home(request):
    teams = Team.objects.all()
    sliders = Slider.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-crated_data').filter(is_featured=True)
    all_tubers = Youtuber.objects.order_by('-crated_data')

    data ={
        'sliders': sliders,
        'teams': teams,
        'featured_youtubers': featured_youtubers,
        'all_tubers': all_tubers,

    }
    return render(request, 'webpage/home.html', data)


def about(request):
    return render(request,'webpage/about.html')



def contact(request):
    return render(request, 'webpage/contact.html')



def services(request):
    return render(request,'webpage/services.html')
