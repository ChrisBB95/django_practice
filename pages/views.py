from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'home.html', {})


def about_view(request):
    context = {
        "text": "squeedilyspooch",
        "number": 80085
    }
    return render(request, 'about.html', context)
