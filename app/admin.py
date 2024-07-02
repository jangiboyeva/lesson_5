from django.contrib import admin
from .models import Courses,Teachers,Student
# Register your models here.

admin.site.register(Courses)
admin.site.register(Teachers)
admin.site.register(Student)