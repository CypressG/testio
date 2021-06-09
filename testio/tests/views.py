from django.shortcuts import render

# Importing models
from .models import Tags, Tests, Question, Answer, Comment

# Importing serializers
from .serializers import CommentsSerializers, TagsSerializer,TestsSerializer

# Create your views here.
from rest_framework.parsers import DataAndFiles, JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET','POST','PUT','DELETE'])
def tags(request):
    if request.method == 'GET':
        tags = Tags.objects.all()
        serializer = TagsSerializer(tags,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

        

    

@api_view(['GET','POST','PUT','DELETE'])
def tests(request):
    if request.method == 'GET':
        tags = Tests.objects.all()
        serializer = TestsSerializer(tags,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TestsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','PUT','DELETE'])
def comments(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentsSerializers(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializer = CommentsSerializers(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


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
