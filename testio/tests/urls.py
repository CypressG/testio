from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('tags/', views.UserCreatedTag.as_view(),name='tags'),
    path('tags/<int:pk>', views.TagSingle.as_view(),name='tags'),
    path('tags/<int:id>/tagsupdate', views.TagUpdateDelete.as_view(),name='tags'),
    path('user/tests/', views.TestView.as_view(),name='tests'),
    path('user/tests/<int:id>', views.TestUpdateDelete.as_view(),name='tests'),
    path('user/tests/<int:id>/questions', views.AllOneTestQuestions.as_view(),name='tests'),
    path('tests/', views.AllTests.as_view(),name='tests'),
    path('tests/<int:id>/comment', views.CommentTest.as_view(),name='comments'),
    path('question/', views.Question.as_view(),name='question'),
    path('question/<int:id>', views.QuestionsUpdateDelete.as_view(),name='question_single'),
    path('question/<int:id>/answer', views.AnswerToSingleQuestion.as_view(),name='answer_to_single_question'),
    path('answer/', views.Answer.as_view(),name='answer'),
    path('answer/<int:id>/answerupdate', views.AnswerUpdateDelete.as_view(),name='answer'),
    path('rating/', views.Rating.as_view(),name='rating'),
    path('comments/', views.Comment.as_view(),name='comments')
]