from rest_framework import serializers
from .models import Tags, Tests, Question, Answer, Comment

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = [
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