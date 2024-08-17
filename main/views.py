from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def attractions(request):
    return render(request, 'attractions.html')

def history(request):
    return render(request, 'history.html')

def gallery(request):
    return render(request, 'gallery.html')
