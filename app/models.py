from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    duration = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
class Teachers(models.Model):
    full_name = models.CharField(max_length=100)
    experince = models.CharField(max_length=100)
    course = models.OneToOneField(Courses,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.full_name
    
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(max_length=13)
    parents_phone_number = models.IntegerField(max_length=13)
    telegram_link = models.CharField(max_length=200)
    address = models.CharField(max_length=150)
    course = models.OneToOneField(Courses,on_delete=models.CASCADE)
    teacher = models.OneToOneField(Teachers,on_delete=models.CASCADE)    

    def __str__(self) -> str:
        return self.full_name
