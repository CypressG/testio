from rest_framework import serializers
from .models import Tags, Tests, Question, Answer, Comment

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

<<<<<<< HEAD
class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id','comment', 'fk_tests'
=======
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
>>>>>>> 0452d719065953461e0f5be869fef3db2be5fe81
        ]