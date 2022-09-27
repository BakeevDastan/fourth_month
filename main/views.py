from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
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
    context = {
        'films_detail': detail,
        'review': Review.objects.filter(films_id=id),
        'genre': Genre.objects.all()
    }
    return render(request, 'detail.html', context=context)


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
