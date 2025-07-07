from django.contrib import admin
from .models import Teacher

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_name', 'teacher', 'subject', 'mobile', 'qualification']
    list_filter = ['subject', 'qualification']
    search_fields = ['teacher_name', 'teacher', 'subject']
    ordering = ['teacher_name']
