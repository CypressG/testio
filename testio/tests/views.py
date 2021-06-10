import tests
from django.http import response
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import render

# Importing models
from .models import Tags, Tests, Question, Answer, Comment, Rating

# Importing serializers
from .serializers import AnswerSerializer, CommentsSerializers, QuestionSerializer, RatingSerializer, TagsSerializer, TestsSerializer

# Create your views here.
from rest_framework import generics, status
from rest_framework import permissions

from rest_framework.decorators import APIView


'''
Tags:
    1. Vartotojas gali matyti visus tag'us /done 
    2. Vartotojas gali matyti savo kurtus tag'us /done
    3. Vartotojas gali istrinti visus tag'us

Tests:
    1. Visi vartotojai gali matyti visus testus /done 
    2. Vartotojas  gali sukurti savo testa 
    3. Vartotojas gali istrinti savo testa
    4. Vartotojas gali papildyti savo testa
    5. Pasaliniai vartotojai gali spresti testa
    6. ... Matyti isprestus testus

Questions:
    1. Vartotojas gali ikelti klausima i testa
    2. Vartotojas gali istrinti klausima is testo
    3. Vartotojas gali redaguoti klausima
    4. Vartotojas gali matyti visus klausimus is testo
    
Answer:
    1. Vartotojas gali sukurti atsakymus priskirtus klausimui
    1. Vartotojas gali keisti atsakymus priskirtus klausimui
    1. Vartotojas gali istrinti atsakymus priskirtus klausimui

Comments:

Ratings:
'''


class userCreatedTag(generics.ListCreateAPIView):
    kintamasis = Tags.objects.all()
    queryset = kintamasis
    serializer_class = TagsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    
class tagSingle(generics.ListCreateAPIView):
    kintamasis = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    def get_queryset(self):
        return Tags.objects.all().filter(fk_user=self.request.user)

class test(generics.ListAPIView):
    #
    kintamasis = Tests.objects.all()
    #
    queryset = kintamasis
    serializer_class = TestsSerializer
    permission_classes = [permissions.IsAuthenticated]

    

class testSingle(APIView):
    serializer_class = TestsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, user):
        try:
            return Tests.objects.all().filter(fk_user=user)
        except Tests.DoesNotExist:
            return response.Http404

    def get(self, request, format=None):
        tests = self.get_object(request.user)
        serializer = TestsSerializer(tests, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TestsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        snippet = self.get_object()
        serializer = TestsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    #permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Question.objects.all().filter(fk_tests=self.kwargs['pk'])

class answer(generics.ListAPIView):
    kintamasis = Answer.objects.all()
    queryset = kintamasis
    serializer_class = AnswerSerializer

class rating(generics.ListAPIView):
    kintamasis = Rating.objects.all()
    queryset = kintamasis
    serializer_class = RatingSerializer