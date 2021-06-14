from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('tags/', views.userCreatedTag.as_view(),name='tags'),
    path('tags/<int:pk>', views.tagSingle.as_view(),name='tags'),
    path('tags/<int:id>/tagsupdate', views.tagUpdateDelete.as_view(),name='tags'),

    path('user/tests/', views.test.as_view(),name='tests'),
    path('user/tests/<int:id>', views.testUpdateDelete.as_view(),name='tests'),
    path('user/tests/<int:id>/questions', views.allOneTestQuestions.as_view(),name='tests'),

    path('tests/', views.allTests.as_view(),name='tests'),
    path('tests/<int:id>/comment', views.commenttest.as_view(),name='comments'),

    path('question/', views.question.as_view(),name='question'),
    path('question/<int:id>', views.questionsUpdateDelete.as_view(),name='question_single'),
    path('question/<int:id>/answer', views.answerToSingleQuestion.as_view(),name='answer_to_single_question'),

    path('answer/', views.answer.as_view(),name='answer'),
    path('answer/<int:id>/answerupdate', views.answerUpdateDelete.as_view(),name='answer'),
    
    path('rating/', views.rating.as_view(),name='rating'),
    
    path('comments/', views.comment.as_view(),name='comments')
]