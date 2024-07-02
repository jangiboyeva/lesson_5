from django.shortcuts import render

from .models import Courses,Teachers,Student
from .serializers import CourseSerializer,TeacherSerializer,StudentSerializers

from rest_framework.permissions import DjangoModelPermissions
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class CourseAPICreateView(ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [DjangoModelPermissions]

class CourseAPIUpdateDeleteDetail(RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [DjangoModelPermissions]

class TeacherAPICreateView(ListCreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [DjangoModelPermissions]

class TeacherAPIUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [DjangoModelPermissions]

class StudentAPICreateView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [DjangoModelPermissions]

class StudentAPIUpdateDeleteDetail(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [DjangoModelPermissions]

