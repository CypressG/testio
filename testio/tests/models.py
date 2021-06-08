from django.db import models
from django.db.models.base import Model

# Create your models here.

class Tests(models.Model):
    type = models.CharField()
    #fk_user = models.ForeignKey()

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField()
    #Tag can be also ManyToMany need to look up
    tags = models.ForeignKey() 
    explanation = models.CharField()
    #right_answer = models.CharField()
    fk_tests = models.ForeignKey()

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    fk_question = models.ForeignKey()
    #right_answer = models.BooleanField()
    right_answer = models.CharField()
    answer = models.CharField()

class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField()

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField()
    fk_tests = models.ForeignKey(Tests)
    #fk_user = models.ForeignKey(User)
