from django.urls import path
from . import views

urlpatterns = [

    path('result', views.result_view, name='result'),
    path('', views.initial_view, name='home'),
    path('mh', views.movie_view, name='movies')

]