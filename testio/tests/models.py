from django.db import models

# Create your models here.
class Tests(models.Model):
    type = models.CharField()
    fk_user = models.ForeignKey()

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField()
    #Tag can be also ManyToMany need to look up
    tags = models.ForeignKey() 
    explanation = models.CharField()
    fk_tests = models.ForeignKey()

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    fk_question = models.ForeignKey()
    right_answer = models.BooleanField()
    answer = models.CharField()



class Categories(models.Model):
    pass