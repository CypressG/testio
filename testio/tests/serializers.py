from django.http import request
from rest_framework import serializers
from . models import Tag, Test, Question, Answer, Comment, Rating
from rest_framework import permissions

'''
 * Class, which processes the information and makes it visible to JSON format
 *
 * 
 * @author DevLab
 *  Since 1.0 
 * Version 1.0 
 * 
'''

'''
 * Class dedicated to serialize data to Tags json object for API  .
 *
 * 
 * @author DevLab
 *  Since 1.0 
 * Version 1.0 
 * 
 '''
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

'''
 * Class dedicated to serialize data to Tags json object for API  .
 *
 * 
 * @author DevLab
 *  Since 1.0 
 * Version 1.0 
 * 
 '''
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
'''
 * Class dedicated to serialize data to Comment json object for API  .
 *
 * 
 * @author DevLab
 *  Since 1.0 
 * Version 1.0 
 * 
 '''
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
'''
 * Class dedicated to serialize data to Question json object for API  .
 *
 * 
 * @author DevLab
 *  Since 1.0 
 * Version 1.0 
 * 
 '''
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','question','tags','explanation','fk_tests']
    def create(self,validated_data):
        user = self.context['request'].user
        questions = Question.objects.create(
            fk_user=user,**validated_data)
        return questions
'''
 * Class dedicated to serialize data to Answers json object for API  .
 *
 * 
 * @author DevLab
 *  Since 1.0 
 * Version 1.0 
 * 
 '''
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
'''
 * Class dedicated to serialize data to Rating json object for API .
 *
 * 
 * @author DevLab
 *  Since 1.0 
 * Version 1.0 
 * 
 '''
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id','rating']