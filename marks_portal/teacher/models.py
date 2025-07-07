from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher = models.CharField(max_length=20, null=True, blank=True)
    teacher_name = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    qualification = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    img = models.ImageField(upload_to='teacher_image', null=True, blank=True)

    def __str__(self):
        return self.teacher_name
