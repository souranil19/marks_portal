from django.contrib import admin
from .models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'posted_by', 'date_posted', 'is_urgent', 'is_active']
    list_filter = ['category', 'is_urgent', 'is_active']
    search_fields = ['title', 'content', 'posted_by']
    list_editable = ['is_urgent', 'is_active']
