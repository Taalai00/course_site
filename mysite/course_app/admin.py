from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin



admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Assignment)
admin.site.register(Question)
admin.site.register(Exam)
admin.site.register(Certificate)
admin.site.register(Review)
admin.site.register(Category)