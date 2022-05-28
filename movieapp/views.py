from django.shortcuts import render

# Create your views here.
def home(request):
    # movie_data="THE GRAY MAN"
    movie_data=[
        {
            "name":"THE GRAY MANWeb of Make Believe: Death, Lies and the Internet",
            "year":"2022"
        },
        {
            "name":"THE GRAY MAN",
            "year":"2022"
        },
        {
            "name":"Spriggan",
            "year":"2022"
        }
    ]
    return render(request, 'home.html',{"movie":movie_data})
def testimonials(request):
    return render(request, 'testimonials.html',{})
