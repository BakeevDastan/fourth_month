from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime
from main.forms import FilmsCreateForm
from main.models import Films, Review, Genre


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
