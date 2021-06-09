from django.contrib import admin
from .models import Rating, Tags, Tests, Question, Answer, Comment
# Register your models here.
admin.site.register(Tags)
admin.site.register(Tests)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Rating)



