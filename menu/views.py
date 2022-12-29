from django.shortcuts import render


def index(request, pk=-1):
    return render(request, 'index.html', {'pk': pk})
