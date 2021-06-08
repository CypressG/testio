from django.db import models
from django.db.models.base import Model

# Create your models here.

class Tags(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.CharField(max_length=20)


class Tests(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=200)
    #fk_user = models.ForeignKey()

class Question(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.TextField()
    #Tag can be also ManyToMany need to look up
    tags = models.ForeignKey(Tags,on_delete=models.CASCADE) 
    explanation = models.TextField()
    fk_tests = models.ForeignKey(Tests,on_delete=models.CASCADE)

class Answer(models.Model):
    id = models.BigAutoField(primary_key=True)
    fk_question = models.ForeignKey(Question,on_delete=models.CASCADE)
    right_answer = models.BooleanField(default=False)
    answer = models.CharField(max_length=200)
    
    def __str__(self):
        return self.id 

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.CharField(max_length=200)
    fk_tests = models.ForeignKey(Tests,on_delete=models.CASCADE)
