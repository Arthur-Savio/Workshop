from django.urls import path
from .views import *

urlpatterns = [
    path('movies/', movies),
    path('series/', series),
    path('home/', home),
    path('movie/<int:pk>/', movie_id)
]
