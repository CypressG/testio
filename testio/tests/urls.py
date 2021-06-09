from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('tags/', views.tags,name='tags'),
    path('tests/',views.tests,name='tests'),
<<<<<<< HEAD
=======
    path('question/',views.questions,name='question'),
    path('answer/',views.answer,name='answer'),
>>>>>>> 651841937da993e74f57b1fdca041f049dff99d2
]
