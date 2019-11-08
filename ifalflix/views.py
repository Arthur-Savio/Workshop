# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *


def movies(request):
    movies = Movie.objects.all()
    return render(request, 'movie.html', {'movies': movies})

def movie_id(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movie.html', {'movie':movie})

def series(request):
    series = Series.objects.all()
    return render(request, 'series.html', {'series':series})    

def home(request):
    series = Series.objects.all()
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies':movies})    
