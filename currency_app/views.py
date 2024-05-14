from django.shortcuts import render


def index(request):
    templates = index.html
    return render(request , templates)
    