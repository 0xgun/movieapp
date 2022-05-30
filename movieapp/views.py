from django.shortcuts import render
from .models import Movie
# Create your views here.
def home(request):
    # movie_data="THE GRAY MAN"
    # movie_data=[
    #     {
    #         "name":"THE GRAY MANWeb of Make Believe: Death, Lies and the Internet",
    #         "year":"2022"
    #     },
    #     {
    #         "name":"THE GRAY MAN",
    #         "year":"2022"
    #     },
    #     {
    #         "name":"Spriggan",
    #         "year":"2022"
    #     }
    # ]
    # movie_data=movie.objects.filter(star__gt=3,year__gt=2020)
    movie_data=Movie.objects.all()

    return render(request, 'home.html',{"movie":movie_data})
def testimonials(request):
    return render(request, 'testimonials.html',{})
def Movies(request,movie_id):
    movie_data=Movie.objects.get(id=movie_id)
    return render(request, 'movie.html',{"movie":movie_data})