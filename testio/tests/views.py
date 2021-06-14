from django.http import response
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import render

# Importing models
from .models import Tag, Test, Question, Answer, Comment, Rating

# Importing serializers
from .serializers import AnswerSerializer, CommentsSerializer, QuestionSerializer, RatingSerializer, TagsSerializer, TestsSerializer

# Creating views
from rest_framework import generics, serializers, status, permissions, mixins
from rest_framework.decorators import APIView


'''
Tags:
    1. Vartotojas gali matyti visus tag'us                      /done 
    2. Vartotojas gali matyti savo kurtus tag'us                /done
    3. Vartotojas gali istrinti visus tag'us                    /done

Tests:
    1. Visi vartotojai gali matyti visus testus                 /done 
    2. Vartotojas  gali sukurti savo testa                      /done
    3. Vartotojas gali istrinti savo testa                      /done
    4. Vartotojas gali papildyti savo testa                     /done
    5. Pasaliniai vartotojai gali spresti testa 
    6. ... Matyti isprestus testus

Questions:
    1. Vartotojas gali ikelti klausima i testa                  /done reikia prafiltruoti FK pasirinkimus kad galima butu ikelt tik i savo.
    2. Vartotojas gali istrinti klausima is testo               /done
    3. Vartotojas gali redaguoti klausima                       /done
    4. Vartotojas gali matyti visus klausimus is testo          /done
    
Answer:
    1. Vartotojas gali sukurti atsakymus priskirtus klausimui   /done bet neranda fk_user
    1. Vartotojas gali keisti atsakymus priskirtus klausimui    /done bet neranda testo pagal id
    1. Vartotojas gali istrinti atsakymus priskirtus klausimui  /done kai veiks update

Comments:
    1.Vartotojas gali rasyti komenta prie testo                 /done

'''

class UserCreatedTag(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return Tag.objects.all().filter(fk_user=self.request.user)

class TagSingle(generics.ListCreateAPIView):
    kintamasis = Tag.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    def get_queryset(self):
        return Tag.objects.all().filter(fk_user=self.request.user)

class TagUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagsSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return Tag.objects.all().filter(fk_user=self.request.user)

class TestView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestsSerializer
    #permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]
    def get_queryset(self):
        return Test.objects.all().filter(fk_user=self.request.user)

class AnswerToSingleQuestion(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    lookup_field='id'
    def get_queryset(self):
        return Answer.objects.all().filter(fk_question=self.kwargs['id'])

class AnswerUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return Answer.objects.all().filter(fk_question=self.kwargs['id'])

class CommentTest(generics.ListCreateAPIView):
    serializer_class = CommentsSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return Comment.objects.all().filter(fk_user=self.kwargs['id'])

class AllTests(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestsSerializer
    #permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]

class AllOneTestQuestions(generics.ListAPIView):
    serializer_class = QuestionSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return Question.objects.all().filter(fk_tests=self.kwargs['id'])    

class TestUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TestsSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return Test.objects.all().filter(id=self.kwargs['id'])

class QuestionsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    lookup_field = 'id'
    permission_classes =[IsOwnerOrReadOnly]
    def get_queryset(self):
        return Question.objects.all().filter(id=self.kwargs['id'])

class Comment(generics.ListAPIView):
    kintamasis = Comment.objects.all()
    queryset = kintamasis
    serializer_class = CommentsSerializer

class Question(generics.ListAPIView):
    kintamasis = Question.objects.all()
    queryset = kintamasis
    serializer_class = QuestionSerializer

class QuestionSingle(generics.ListAPIView):
    serializer_class = QuestionSerializer
    def get_queryset(self):
        return Question.objects.all().filter(fk_tests=self.kwargs['pk'])

class Answer(generics.ListAPIView):
    kintamasis = Answer.objects.all()
    queryset = kintamasis
    serializer_class = AnswerSerializer

class Rating(generics.ListAPIView):
    kintamasis = Rating.objects.all()
    queryset = kintamasis
    serializer_class = RatingSerializer