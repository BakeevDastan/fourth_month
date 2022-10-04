from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime
from main.forms import FilmsCreateForm, UserCreateForm, LoginForm
from main.models import Films, Review, Genre
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required


def date_now(request):
    current_datetime = datetime.datetime.now()
    html = "<b>Current Date and Time Value:</b> %s" % current_datetime
    return HttpResponse(html)


def about_us(request):
    return render(request, 'index.html')


def film_list_view(request):
    queryset = Films.objects.all()
    context = {
        'title': 'All news',
        'film_list': queryset,
        'genre': Genre.objects.all()
    }
    return render(request, 'films.html', context=context)


def film_item_view(request, id):
    try:
        detail = Films.objects.get(id=id)
    except Films.DoesNotExist:
        raise Http404('Films not found')
    if request.method == 'GET':
        context = {
            'films_detail': detail,
            'review': Review.objects.filter(films_id=id),
            'genre': Genre.objects.all()
        }
        return render(request, 'detail.html', context=context)
    else:
        film = request.POST.get('film')
        text = request.POST.get('text')
        Review.objects.create(
            film=film,
            text=text,
            films_id=id
        )
        print(request.POST)
        return redirect(f'/films/{id}')


def genre_view(request, id):
    try:
        genre = Genre.objects.get(id=id)
    except:
        raise Http404()
    context = {
        'title': genre.title,
        'film_list': Films.objects.filter(genre_id=id),
        'genre': Genre.objects.all()
    }
    return render(request, 'films.html', context=context)


@login_required(login_url='/login')
def films_create_view(request):
    if request.method == 'GET':
        context = {
            'form': FilmsCreateForm(),
            'genre': Genre.objects.all()
        }
        return render(request, 'add_films.html', context=context)
    else:
        form = FilmsCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/films/')
        print(request.POST)
        return render(request, 'add_films.html', context={
            'form': form,
            'genre': Genre.objects.all()
        })


def register_view(request):
    context = {
        'form': UserCreateForm(),
        'genre': Genre.objects.all()

    }
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username,
                                     password=password,
                                     email=email,
                                     is_active=True)
            return redirect('/login')
        else:
            context = {
                'form': form,
                'genre': Genre.objects.all()
            }
    return render(request, 'register.html', context=context)


def login_view(request):
    context = {
        'form': LoginForm(),
        'genre': Genre.objects.all()
    }
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/films')
        return redirect('/login')
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/login')
