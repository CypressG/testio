from django.http import response
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import render

# Importing models
from .models import Tags, Tests, Question, Answer, Comment, Rating

# Importing serializers
from .serializers import AnswerSerializer, CommentsSerializers, QuestionSerializer, RatingSerializer, TagsSerializer, TestsSerializer

# Create your views here.
from rest_framework import generics, serializers, status
from rest_framework import permissions
from rest_framework import mixins
from rest_framework.decorators import APIView


'''
Tags:
    1. Vartotojas gali matyti visus tag'us /done 
    2. Vartotojas gali matyti savo kurtus tag'us /done
    3. Vartotojas gali istrinti visus tag'us /done

Tests:
    1. Visi vartotojai gali matyti visus testus /done 
    2. Vartotojas  gali sukurti savo testa  /done
    3. Vartotojas gali istrinti savo testa /done
    4. Vartotojas gali papildyti savo testa /done
    5. Pasaliniai vartotojai gali spresti testa 
    6. ... Matyti isprestus testus

Questions:
    1. Vartotojas gali ikelti klausima i testa /done reikia prafiltruoti FK pasirinkimus kad galima butu ikelt tik i savo.
    2. Vartotojas gali istrinti klausima is testo /done
    3. Vartotojas gali redaguoti klausima/done
    4. Vartotojas gali matyti visus klausimus is testo /done
    
Answer:
    1. Vartotojas gali sukurti atsakymus priskirtus klausimui /done bet neranda fk_user
    1. Vartotojas gali keisti atsakymus priskirtus klausimui /done bet neranda testo pagal id
    1. Vartotojas gali istrinti atsakymus priskirtus klausimui/done kai veiks update

Comments:
    1.Vartotojas gali rasyti komenta prie testo /done

'''


class userCreatedTag(generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return Tags.objects.all().filter(fk_user=self.request.user)
    
class tagSingle(generics.ListCreateAPIView):
    kintamasis = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    def get_queryset(self):
        return Tags.objects.all().filter(fk_user=self.request.user)

class TagsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagsSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return Tags.objects.all().filter(fk_user=self.request.user)

class test(generics.ListCreateAPIView):
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Tests.objects.all().filter(fk_user=self.request.user)

class AnswerToQuestion(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    lookup_field='id'
    def get_queryset(self):
        return Answer.objects.all().filter(fk_question=self.kwargs['id'])
        
class AnswerUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSerializer
    lookup_field='id'
    def get_queryset(self):
        return Answer.objects.all().filter(fk_question=self.kwargs['id'])

class commenttest(generics.ListCreateAPIView):
    serializer_class = CommentsSerializers
    lookup_field = 'id'
    def get_queryset(self):
        return Comment.objects.all().filter(fk_user=self.kwargs['id'])


class AllTests(generics.ListAPIView):
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer
    permission_classes = [permissions.IsAuthenticated]


class AllOneTestQuestions(generics.ListAPIView):
    serializer_class=QuestionSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return Question.objects.all().filter(fk_tests=self.kwargs['id'])    


class TestsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TestsSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return Tests.objects.all().filter(id=self.kwargs['id'])

class QuestionsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return Question.objects.all().filter(id=self.kwargs['id'])
    

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