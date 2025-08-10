from django.core.management.base import BaseCommand
from marks_portal.models import Notice
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    help = 'Create sample notices for testing'

    def handle(self, *args, **options):
        # Clear existing notices
        Notice.objects.all().delete()
        
        # Sample notices data
        notices_data = [
            {
                'title': 'Admission Forms for Class XI - Last Date Extended',
                'content': 'The last date for submission of admission forms for Class XI has been extended to August 15, 2025. Students who haven\'t submitted their forms yet can visit the school office between 10 AM to 4 PM.',
                'category': 'URGENT',
                'posted_by': 'Principal\'s Office',
                'is_urgent': True,
                'button_text': 'Read More',
                'date_posted': timezone.now() - timedelta(days=6)
            },
            {
                'title': 'Class XII Final Examination Schedule Released',
                'content': 'The examination schedule for Class XII final examinations has been published. Students can download the schedule from the student portal or collect hard copies from the office.',
                'category': 'ACADEMIC',
                'posted_by': 'Examination Cell',
                'button_text': 'Download',
                'date_posted': timezone.now() - timedelta(days=8)
            },
            {
                'title': 'Annual Cultural Program - Auditions Open',
                'content': 'Auditions for the annual cultural program will be held on August 10, 2025. Students interested in participating can register with their respective class teachers.',
                'category': 'EVENT',
                'posted_by': 'Cultural Committee',
                'button_text': 'Register',
                'date_posted': timezone.now() - timedelta(days=11)
            },
            {
                'title': 'Class XI First Terminal Results Published',
                'content': 'First terminal examination results for Class XI are now available. Students can check their results through the marks portal using their roll numbers.',
                'category': 'RESULTS',
                'posted_by': 'Result Section',
                'button_text': 'Check Results',
                'date_posted': timezone.now() - timedelta(days=13)
            },
            {
                'title': 'Independence Day Celebration & Holiday Notice',
                'content': 'School will remain closed on August 15, 2025, for Independence Day. Special celebration program will be held on August 14, 2025, at 10 AM.',
                'category': 'HOLIDAY',
                'posted_by': 'Administration',
                'button_text': 'View Details',
                'date_posted': timezone.now() - timedelta(days=16)
            },
            {
                'title': 'Monthly Fee Payment Reminder - August 2025',
                'content': 'Monthly fees for August 2025 are due by August 10, 2025. Late payment will incur a fine of ₹50. Payment can be made at the school office or online.',
                'category': 'FEE',
                'posted_by': 'Accounts Section',
                'button_text': 'Pay Online',
                'date_posted': timezone.now() - timedelta(days=21)
            },
        ]
        
        # Create notices
        for notice_data in notices_data:
            Notice.objects.create(**notice_data)
            
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {len(notices_data)} sample notices')
        )
