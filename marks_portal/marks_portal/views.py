from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Notice

def school_landing(request):
    return render(request, 'landing1.html')

def about(request):
    return render(request, 'about.html')

def morning_school_landing(request):
    return render(request, 'morning_school_landing1.html')

def day_school_landing(request):
    return render(request, 'day_school_landing1.html')

def vocational_landing(request):
    return render(request, 'vocational_landing1.html')

def notice(request):
    filter_category = request.GET.get('filter', 'all')
    notices = Notice.objects.filter(is_active=True)
    
    if filter_category != 'all' and filter_category:
        notices = notices.filter(category=filter_category.upper())
    
    context = {
        'notices': notices,
        'current_filter': filter_category,
        'total_notices': Notice.objects.filter(is_active=True).count(),
        'urgent_notices': Notice.objects.filter(is_active=True, is_urgent=True).count(),
        'this_month_notices': Notice.objects.filter(
            is_active=True, date_posted__month=8, date_posted__year=2025).count(),
    }
    
    return render(request, 'notice.html', context)


def contact(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        subject_mapping = {
            'admission': 'Admission Inquiry',
            'academic': 'Academic Information Request',
            'general': 'General Inquiry',
            'complaint': 'Complaint/Feedback',
            'other': 'Other Inquiry'
        }
        
        email_subject = f"New Contact Form: {subject_mapping.get(subject)}"
        email_message = f"""
New contact form submission from Murari Pukur School website:

Name: {first_name} {last_name}
Email: {email}
Phone: {phone if phone else 'Not provided'}
Subject: {subject_mapping.get(subject)}

Message:
{message}

---
This email was sent from the school website contact form.
        """
        
        try:
            send_mail(
                subject=email_subject,
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['to-email.com'],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully! We'll get back to you soon.")
        except Exception as e:
            messages.error(request, "Sorry, there was an error sending your message. Please try again or contact us directly.")
        
        return redirect('contact')
        
    return render(request, 'contact.html')


def gallery(request):
    return render(request,'gallery.html')