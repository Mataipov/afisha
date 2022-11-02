from django.shortcuts import render,Http404
from .models import Film
import datetime

# Create your views here.

def film_detail_view(request, id):
    context = {}
    try:
        film = Film.objects.get(id=id)
    except Film.DoesNotExist:
        raise Http404('Film not found')
    context['film_detail'] = film

    return render(request, 'detail.html', context)

def film_list_view(request):
    context = {
        'film_list': Film.objects.all(),
        # 'categories': Category.objects.all()
    }
    return render(request, 'films.html', context)

def about_us(request):
    return render(request, 'about_us.html')

def date_now(request):
    date = datetime.datetime.now()
    context = {
        'date': date
    }
    return render(request, 'date_now.html', context)



