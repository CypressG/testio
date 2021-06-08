from django.db import models

# Create your models here.
class Tests(models.Model):
    type = models.BooleanField()
    pass

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField()
    category = models.ForeignKey()
    explanation = models.CharField()
    type = models.BooleanField()
    pass

class Categories(models.Model):
    pass