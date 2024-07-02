from rest_framework import serializers

from .models import Courses,Teachers,Student

class CourseSerializer(serializers.ModelSerializer):
    model = Courses
    field = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    model =Teachers
    field = '__all__'

class StudentSerializers(serializers.ModelSerializer):
    model = Student
    field = '__all__'

    