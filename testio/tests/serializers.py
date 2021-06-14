from django.http import request
from rest_framework import serializers
from . models import Tag, Test, Question, Answer, Comment, Rating
from rest_framework import permissions

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','tag']
    def create(self, validated_data):
        user = self.context['request'].user
        tags = Tag.objects.create(
            fk_user=user, **validated_data
        )
        return tags

class TestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id','type']
    def create(self, validated_data):
        user = self.context['request'].user
        tests = Test.objects.create(
            fk_user=user, **validated_data
        )
        return tests

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','comment', 'fk_tests']
    def create(self, validated_data):
        user = self.context['request'].user
        comment = Comment.objects.create(
            fk_user=user, **validated_data
        )
        return comment

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','question','tags','explanation','fk_tests']
    def create(self,validated_data):
        user = self.context['request'].user
        questions = Question.objects.create(
            fk_user=user,**validated_data)
        return questions

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id','right_answer','answer','fk_question']
        def create(self,validated_data):
            user = self.context['request'].user
            answers = Answer.objects.create(
                fk_user=user, **validated_data
            )
            return answers

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id','rating']