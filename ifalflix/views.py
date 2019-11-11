# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def movies(request):
    movies = Movie.objects.all()
    return render(request, 'movie.html', {'movies': movies})

def movie_id(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movie.html', {'movie':movie})

def series(request):
    series = Series.objects.all()
    return render(request, 'series.html', {'series':series})    

@login_required(login_url = '/login')
def home(request):
    series = Series.objects.all()
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies':movies})   

     
def login_user(request):
	return render(request, 'login.html')

@csrf_protect
def login_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Usuário e/ou senha inválidos!')
            return redirect('/login')
    else:
        return redirect('/login')

def logout_user(request):
    logout(request)
    return redirect('/login')


def register_view(request):
    return render(request, "register.html")

@csrf_protect
def register_user(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Ocorreu algo inesperado')
            return redirect('/register')
    else:
        return redirect('/register')

