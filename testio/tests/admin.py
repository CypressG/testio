from django.contrib import admin
from .models import Rating, Tag, Test, Question, Answer, Comment
# Register your models here.
admin.site.register(Tag)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Rating)



