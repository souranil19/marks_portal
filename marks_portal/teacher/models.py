from django.db import models




# Create your models here.
class Teacher(models.Model):
    teacher = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True, blank=True)
    img = models.ImageField(upload_to='teacher_image', null=True, blank=True)
    pdf_document = models.FileField(upload_to='teacher_cv', null=True, blank=True)
    designation=models.CharField(max_length=10, null=True, blank=True)
    qualification=models.CharField(max_length=20, null=True, blank=True)
    department=models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"Teacher:{self.teacher} PASSWORD:{self.password}"


class ClassAccess(models.Model):
    class_number = models.IntegerField(unique=True)
    class_password = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Class {self.class_number}"
