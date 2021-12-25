from django.shortcuts import render, get_object_or_404
from.models import Youtuber

# Create your views here.


def youtubers(request):
    tuber = Youtuber.objects.order_by('-crated_data')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_search = Youtuber.objects.values_list(
        'cemera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list(
        'category', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tuber = tuber.filter(discription__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tuber = tuber.filter(city__iexact=city)

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tuber = tuber.filter(cemera_type__iexact=camera_type)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tuber = tuber.filter(category__iexact=category)

    data = {
        'tuber': tuber,
        'city_search': city_search,
        'camera_search': camera_search,
        'category_search': category_search
    }
    return render(request, 'youtubers/youtubers.html', data)


def youtubers_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)

    data = {
        'tuber': tuber

    }
    return render(request, 'youtubers/youtuber_detail.html', data)


def search(request):
    tuber = Youtuber.objects.order_by('-crated_data')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_search = Youtuber.objects.values_list(
        'cemera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list(
        'category', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tuber = tuber.filter(discription__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tuber = tuber.filter(city__iexact=city)

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tuber = tuber.filter(cemera_type__iexact=camera_type)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tuber = tuber.filter(category__iexact=category)

    data = {
        'tuber': tuber,
        'city_search': city_search,
        'camera_search': camera_search,
        'category_search': category_search
    }
    return render(request, 'youtubers/search.html', data)
