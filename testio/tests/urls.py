from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('tags/', views.tagsListGeneric.as_view(),name='tags'),
    path('tests/',views.tests,name='tests'),
    path('comments/',views.comments,name='comments'),
    path('question/',views.questions,name='question'),
    path('answer/',views.AnswerListGeneric.as_view(),name='answer'),
    path('rating/',views.RatingListGeneric.as_view(),name='tests'),

]
