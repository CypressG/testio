from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('tags/', views.tag.as_view(),name='tags'),
    path('tags/<int:pk>', views.tagSingle.as_view(),name='tags'),
    path('tests/',views.test.as_view(),name='tests'),
    path('comments/',views.comment.as_view(),name='comments'),
    path('question/',views.question.as_view(),name='question'),
    path('answer/',views.answer.as_view(),name='answer'),
    path('rating/',views.rating.as_view(),name='rating'),

]