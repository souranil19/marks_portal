from django.db import models
from django.utils import timezone


class Notice(models.Model):
    CATEGORY_CHOICES = [
        ('URGENT', 'Urgent'),
        ('ACADEMIC', 'Academic'),
        ('EVENT', 'Event'),
        ('ADMISSIONS', 'Admissions'),
        ('RESULTS', 'Results'),
        ('HOLIDAY', 'Holiday'),
        ('FEE', 'Fee'),
        ('GENERAL', 'General'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='GENERAL')
    posted_by = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    is_urgent = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    button_text = models.CharField(max_length=50, blank=True, null=True)
    pdf_file = models.FileField(upload_to='notices/', blank=True, null=True)
    
    class Meta:
        ordering = ['-is_urgent', '-date_posted']
    
    def __str__(self):
        return self.title
    
    def get_badge_color(self):
        color_map = {
            'URGENT': '#dc3545',
            'ACADEMIC': 'var(--primary-blue)',
            'EVENT': 'var(--secondary-blue)',
            'ADMISSIONS': 'var(--royal-blue)',
            'RESULTS': 'var(--light-blue)',
            'HOLIDAY': 'var(--royal-blue)',
            'FEE': 'var(--electric-blue)',
            'GENERAL': 'var(--primary-blue)',
        }
        return color_map.get(self.category, 'var(--primary-blue)')
