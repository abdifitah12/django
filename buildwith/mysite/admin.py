from django.contrib import admin

from .models import Person,Course,Lesson, Section


# Register your models here.
admin.site.register(Person)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lesson)

