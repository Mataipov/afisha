from django.shortcuts import render, Http404, redirect
from .models import Film, Director
from .forms import FilmForm, DirectorForm, UserLoginForm, UserCreateForm
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    context = {
        'form': UserLoginForm(),
        'directories': Director.objects.all()
    }
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if not user:
                return redirect('/login/')
            else:
                login(request, user)
                return redirect('/')
    return render(request, 'login.html', context)


def register_view(request):
    context = {
        'form': UserCreateForm(),
        'directories': Director.objects.all()

    }
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            User.objects.create_user(username=username, password=password)
            return redirect('/login/')
        context['form'] = form
    return render(request, 'register.html', context=context)

def create_films(request):
    context = {
        'form': FilmForm(),
        'directories': Director.objects.all()
    }
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/films/')
        else:
            context['form'] = form
    return render(request, 'create_films.html', context)



def create_director(request):
    context = {
        'form': DirectorForm(),
        'directories': Director.objects.all()
    }
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/films/')
        else:
            context['form'] = form
    return render(request, 'create_director.html', context)



def film_detail_view(request, id):
    context = {
        'directories': Director.objects.all()
    }
    try:
        film = Film.objects.get(id=id)
    except Film.DoesNotExist:
        raise Http404('Film not found')
    context['film_detail'] = film

    return render(request, 'detail.html', context)

def film_list_view(request):
    context = {
        'film_list': Film.objects.all(),
        'directories': Director.objects.all()
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

def director_films(request, director_id):
    try:
        director = Director.objects.get(id=director_id)
    except Director.DoesNotExist:
        raise Http404('Director not found!')
    context = {
        'directories': Director.objects.all(),
        'director': director
    }
    return render(request, 'director_films.html', context)


def index_view(request):
    context = {

         'directories': Director.objects.all()
    }
    return render(request, 'index.html', context)


