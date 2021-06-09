from django.shortcuts import render

# Importing models
from .models import Tags, Tests, Question, Answer, Comment

# Importing serializers
from .serializers import TagsSerializer,TestsSerializer

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@csrf_exempt
def tags(request):
    if request.method == 'GET':
        tags = Tags.objects.all()
        serializer = TagsSerializer(tags,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TagsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)



def tests(request):
    if request.method == 'GET':
        tags = Tests.objects.all()
        serializer = TestsSerializer(tags,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TestsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)


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
