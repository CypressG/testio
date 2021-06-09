from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('tags/', views.tagsList.as_view(),name='tags'),
    path('tests/',views.tests,name='tests'),
    path('comments/',views.comments,name='comments'),
    path('question/',views.questions,name='question'),
    path('answer/',views.answer,name='answer'),
    path('rating/',views.tests,name='tests'),

]
