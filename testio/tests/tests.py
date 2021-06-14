
# Create your tests here.
from django.test import TestCase
from .models import Tag, Test, Question, Answer, Comment, Rating
from django.contrib.auth.models import User
# Create your tests here.
'''
 * Test case class
 *
 * 
 * @author DevLab
 *  Since 1.0 
 * Version 1.0 
 * 
'''

class TestTestCase(TestCase):
    def setUp(self):
        self.username = 'Jacob'
        user = User.objects.create(username="TestUser",password="test")
        test = Test.objects.create(type="Pabandymas veikia", id = 44, fk_user=user)

 
    def TestIfWorks(self):
        testui = Test.objects.get(type="Pabandymas veikia")
        self.assertEqual(testui.type, "Pabandymas veikia")
 
class QuestionTestCase(TestCase):
    def setUp(self):
        return super().setUp()
 
class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(id = 1, fk_question = 1, fk_user=1, right_answer = True, answer = "Protokolas buvo parasytas")
 
class AnswerTestCase(TestCase):
    def setUp(self):
        Answer.objects.create(id = 1, tag = "Mokomasis", fk_user=1)
 
class CommentTestCase(TestCase):
    def setUp(self):
        return super().setUp() 
