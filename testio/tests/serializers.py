from django.http import request
from rest_framework import serializers
from .models import Tags, Tests, Question, Answer, Comment, Rating
from rest_framework import permissions

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id','tag']

class TestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tests
        fields = ['id','type']
    def create(self, validated_data):
        user = self.context['request'].user
        tests = Tests.objects.create(
        fk_user=user, 
        **validated_data
        )
        return tests

class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','comment', 'fk_tests']    

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','question','tags','explanation','fk_tests']
    def create(self,validated_data):
        user = self.context['request'].user
       # questions2 = Tests.objects.all().filter(fk_user=user.

        questions = Question.objects.create(fk_user=user,
        **validated_data)
        return questions

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id','right_answer','answer']
        def create(self,validated_data):
         user = self.context['request'].user         
         answers = Answer.objects.create(
         fk_user=user, 
         **validated_data
         )
         return answers
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id','rating']

