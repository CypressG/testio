from rest_framework import serializers
from .models import Tags, Tests, Question, Answer, Comment, Rating

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = [
            'id',
            'tag',
        ]

class TestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tests
        fields = [
            'id','type'
        ]

class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id','comment', 'fk_tests'
        ]    
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id','question','tags','explanation'
        ]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id','right_answer','answer'
        ]
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = [
            'id','rating']
