from django.db import models

# Create your models here.
class Student(models.Model):
    student=models.CharField(max_length=20, null=True, blank=True)
    student_name=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    mobile=models.IntegerField(null=True, blank=True)
    address=models.CharField(max_length=100,null=True, blank=True)
    std=models.IntegerField(null=True, blank=True)
    father=models.CharField(max_length=20,null=True, blank=True)
    dob=models.DateField(null=True, blank=True)
    img=models.ImageField(upload_to='student_image',null=True, blank=True)
