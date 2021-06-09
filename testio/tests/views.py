from django.shortcuts import render

# Importing models
from .models import Tags, Tests, Question, Answer, Comment, Rating

# Importing serializers
from .serializers import AnswerSerializer, CommentsSerializers, QuestionSerializer, RatingSerializer, TagsSerializer, TestsSerializer

# Create your views here.
from rest_framework.parsers import DataAndFiles, JSONParser
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view
from rest_framework import status, generics, mixins


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def tags(request):
    if request.method == 'GET':
        tags = Tags.objects.all()
        serializer = TagsSerializer(tags, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class tagsList(mixins.ListModelMixin, 
                mixins.CreateModelMixin, 
                mixins.UpdateModelMixin, 
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args,**kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args,**kwargs)


class tagsListGeneric(generics.ListAPIView):
    kintamasis = Tags.objects.all()
    queryset = kintamasis
    serializer_class = TagsSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def tests(request):
    if request.method == 'GET':
        tests = Tests.objects.all()
        serializer = TestsSerializer(tests, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TestsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def comments(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentsSerializers(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializer = CommentsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def questions(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def answer(request):
    if request.method == 'GET':
        answer = Answer.objects.all()
        serializer = AnswerSerializer(answer, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AnswerListGeneric(generics.ListAPIView):
    kintamasis = Answer.objects.all()
    queryset = kintamasis
    serializer_class = AnswerSerializer


@api_view(['GET', 'POST'])
def rating(request):
    if request.method == 'GET':
        rating = Rating.object.all()
        serializer = RatingSerializer(rating, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RatingSerializer(data=request.data)



class RatingListGeneric(generics.ListAPIView):
    kintamasis = Rating.objects.all()
    queryset = kintamasis
    serializer_class = RatingSerializer


'''
@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        pass
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        '''
