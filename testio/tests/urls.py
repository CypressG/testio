from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('tags/', views.userCreatedTag.as_view(),name='tags'),
    path('tags/<int:pk>', views.tagSingle.as_view(),name='tags'),
    path('user/tests/',views.test.as_view(),name='tests'),
    path('user/tests/<int:id>',views.TestsUpdateDelete.as_view(),name='tests'),
    path('user/tests/<int:id>/questions',views.AllOneTestQuestions.as_view(),name='tests'),
    path('tests/',views.AllTests.as_view(),name='tests'),
    #path('test/',views.AllTests.as_view(),name='tests'),
    path('comments/',views.comment.as_view(),name='comments'),
    path('question/',views.question.as_view(),name='question'),
    path('question/<int:id>',views.QuestionsUpdateDelete.as_view(),name='question_single'),
    path('question/<int:id>/answer',views.AnswerToQuestion.as_view(),name='Answer_to_question_single'),
    path('answer/',views.answer.as_view(),name='answer'),
    path('answer/<int:id>/answerupdate',views.AnswerUpdateDelete.as_view(),name='answer'),
    path('rating/',views.rating.as_view(),name='rating'),
    
]