from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MovieModel
from .forms import MovieForm


# Create your views here.


def index(request):
    movie = MovieModel.objects.all()
    movie_details = {
        'movie': movie
    }
    return render(request, 'index.html', movie_details)


def details(request, movie_id):
    movie = MovieModel.objects.get(id=movie_id)
    return render(request, 'details.html', {"movie": movie})


def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        year = request.POST['year']
        desc = request.POST['desc']
        image = request.FILES['image']

        movie = MovieModel(name=name, year=year, desc=desc, img=image)
        movie.save()

        return redirect('/')
    return render(request, 'add.html')


def delete(request, movie_id):
    if request.method == 'POST':
        bike = MovieModel.objects.get(id=movie_id)
        bike.delete()
        return redirect('/')

    return render(request, 'delete.html')


def update(request, movie_id):
    movie = MovieModel.objects.get(id=movie_id)
    forms = MovieForm(request.POST or None, request.FILES, instance=movie)

    if forms.is_valid():
        forms.save()

        return redirect('/')

    return render(request, 'update.html', {'movie': movie, 'forms': forms})
