from django.db import models




# Create your models here.
class Teacher(models.Model):
    teacher = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True, blank=True)
    img = models.ImageField(upload_to='teacher_image', null=True, blank=True)
    pdf_document = models.FileField(upload_to='teacher_cv', null=True, blank=True)



    def __str__(self):
        return f"Teacher:{self.teacher} PASSWORD:{self.password}"
