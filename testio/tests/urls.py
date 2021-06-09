from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('tags/', views.tags,name='tags'),
    path('tests/',views.tests,name='tests'),
<<<<<<< HEAD
    path('comments/',views.comments,name='comments')
=======
    path('question/',views.questions,name='question'),
    path('answer/',views.answer,name='answer'),
>>>>>>> 0452d719065953461e0f5be869fef3db2be5fe81
]
