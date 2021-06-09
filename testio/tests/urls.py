from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('tags/', views.tagsListGeneric.as_view(),name='tags'),
    path('tests/',views.testsListGeneric.as_view(),name='tests'),
    path('comments/',views.commentsListGeneric.as_view(),name='comments'),
    path('question/',views.questionsListGeneric.as_view(),name='question'),
    path('answer/',views.AnswerListGeneric.as_view(),name='answer'),
    path('rating/',views.RatingListGeneric.as_view(),name='tests'),

]
