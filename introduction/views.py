from django.shortcuts import render

# Create your views here.

def isweek(request):
    return render(request, 'isweek.html', {})

def hackersir(request):
    return render(request, 'hackersir.html', {})

def sponsor(request):
    return render(request, 'sponsor.html', {})
