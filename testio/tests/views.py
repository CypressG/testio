from .permissions import IsOwnerOrReadOnly
from django.shortcuts import render

# Importing models
from .models import Tags, Tests, Question, Answer, Comment, Rating

# Importing serializers
from .serializers import AnswerSerializer, CommentsSerializers, QuestionSerializer, RatingSerializer, TagsSerializer, TestsSerializer

# Create your views here.
from rest_framework import generics
from rest_framework import permissions



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
    kintamasis = Tests.objects.all()
    queryset = kintamasis
    serializer_class = TestsSerializer
    permission_classes = [permissions.IsAuthenticated]

class comment(generics.ListAPIView):
    kintamasis = Comment.objects.all()
    queryset = kintamasis
    serializer_class = CommentsSerializers

class question(generics.ListAPIView):
    kintamasis = Question.objects.all()
    queryset = kintamasis
    serializer_class = QuestionSerializer

class answer(generics.ListAPIView):
    kintamasis = Answer.objects.all()
    queryset = kintamasis
    serializer_class = AnswerSerializer

class rating(generics.ListAPIView):
    kintamasis = Rating.objects.all()
    queryset = kintamasis
    serializer_class = RatingSerializer