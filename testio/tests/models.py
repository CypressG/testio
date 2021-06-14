from django.db import models
from django.db.models.base import Model

# Create your models here.

class Tag(models.Model):
    id = models.BigAutoField(primary_key = True)
    tag = models.CharField(max_length = 20)
    fk_user = models.ForeignKey('auth.User',on_delete = models.CASCADE)
    
    def __str__(self):
        return self.tag

class Test(models.Model):
    id = models.BigAutoField(primary_key = True)
    type = models.CharField(max_length = 200)
    fk_user = models.ForeignKey('auth.User',on_delete = models.CASCADE)
    
    def __str__(self):
        return self.type

class Question(models.Model):
    id = models.BigAutoField(primary_key = True)
    question = models.TextField()
    #Tag can be also ManyToMany need to look up
    tags = models.ForeignKey(Tag,on_delete = models.CASCADE) 
    explanation = models.TextField()
    fk_tests = models.ForeignKey(Test,on_delete = models.CASCADE,null = True,blank = True)
    fk_user = models.ForeignKey('auth.User',on_delete = models.CASCADE)

    def __str__(self):
        return self.question

class Answer(models.Model):
    id = models.BigAutoField(primary_key = True)
    fk_question = models.ForeignKey(Question ,on_delete = models.CASCADE)
    fk_user = models.ForeignKey('auth.User',on_delete = models.CASCADE, null = True, blank = True)
    right_answer = models.BooleanField(default = False)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.fk_question.question

class Comment(models.Model):
    id = models.BigAutoField(primary_key = True)
    comment = models.CharField(max_length = 200)
    fk_tests = models.ForeignKey(Test,on_delete = models.CASCADE)
    fk_user = models.ForeignKey('auth.User',on_delete = models.CASCADE)
    
    def __str__(self):
        return self.fk_tests.type

class Rating(models.Model):
    id = models.BigAutoField(primary_key = True)
    rating = models.FloatField()
    fk_tests = models.ForeignKey(Test,on_delete = models.CASCADE)
    fk_user = models.ForeignKey('auth.User',on_delete = models.CASCADE)
