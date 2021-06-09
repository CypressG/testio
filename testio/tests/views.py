from django.http import response
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import render

# Importing models
from .models import Tags, Tests, Question, Answer, Comment, Rating

# Importing serializers
from .serializers import AnswerSerializer, CommentsSerializers, QuestionSerializer, RatingSerializer, TagsSerializer, TestsSerializer

# Create your views here.
from rest_framework import generics
from rest_framework import permissions

from rest_framework.decorators import APIView


'''
Tags:
    1. Vartotojas gali matyti visus tag'us
    2. Vartotojas gali matyti savo kurtus tag'us
    3. Vartotojas gali istrinti visus tag'us

Tests:
    1. Visi vartotojai gali matyti visus testus
    2. Vartotojas  gali sukurti savo testa
    3. Vartotojas gali istrinti savo testa
    4. Vartotojas gali papildyti savo testa
    5. Pasaliniai vartotojai gali spresti testa
    6. ... Matyti isprestus testus

Questions:
    1. Vartotojas gali ikelti klausima i testa
    2. Vartotojas gali istrinti klausima is testo
    3. Vartotojas gali redaguoti klausima
    
Answer:
    1. Vartotojas gali sukurti atsakymus priskirtus klausimui
    1. Vartotojas gali keisti atsakymus priskirtus klausimui
    1. Vartotojas gali istrinti atsakymus priskirtus klausimui

Comments:

Ratings:
'''


class tag(generics.ListCreateAPIView):
    kintamasis = Tags.objects.all()
    queryset = kintamasis
    serializer_class = TagsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    
class tagSingle(generics.RetrieveUpdateDestroyAPIView):
    kintamasis = Tags.objects.all()
    queryset = kintamasis
    serializer_class = TagsSerializer

class test(generics.ListAPIView):
    #
    kintamasis = Tests.objects.all()
    #
    queryset = kintamasis
    serializer_class = TestsSerializer
    permission_classes = [permissions.IsAuthenticated]

class testSingle(generics.ListAPIView):
    serializer_class = TestsSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Tests.objects.all().filter(fk_user=self.request.user)



class comment(generics.ListAPIView):
    kintamasis = Comment.objects.all()
    queryset = kintamasis
    serializer_class = CommentsSerializers

class question(generics.ListAPIView):
    kintamasis = Question.objects.all()
    queryset = kintamasis
    serializer_class = QuestionSerializer

class questionSingle(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Question.objects.all().filter(fk_user=self.request.user)

class answer(generics.ListAPIView):
    kintamasis = Answer.objects.all()
    queryset = kintamasis
    serializer_class = AnswerSerializer

class rating(generics.ListAPIView):
    kintamasis = Rating.objects.all()
    queryset = kintamasis
    serializer_class = RatingSerializer