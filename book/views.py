from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User

def index(request):
    data = Book.objects.all()
    params = {
        'data': data,
    }
    return render(request, 'book/index.html', params)

def create():
    pass

def detail():
    pass

def delete():
    pass

def edit():
    pass

def variations(request):
    data = Variation.objects.all()
    params = {
        'data': data,
    }
    return render(request, 'book/variations.html', params)

def users(request):
    data = User.objects.all()
    params = {
        'data': data,
    }
    return render(request, 'book/users.html', params)

def books(request):
    data = Book.objects.all()
    params = {
        'data': data,
    }
    return render(request, 'book/index.html', params)
