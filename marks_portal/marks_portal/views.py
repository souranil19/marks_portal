from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def school_landing(request):
    return render(request,'landing1.html')

def about(request):
    return render(request, 'about.html')


def morning_school_landing(request):
    return render(request,'morning_school_landing1.html')

def day_school_landing(request):
    return render(request,'day_school_landing1.html')

def vocational_landing(request):
    return render(request,'vocational_landing1.html')


def notice(request):
    return render(request,'notice.html')


def contact(request):
    if request.method=="POST":
        print("POST request received")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        
        # Subject mapping for better email subjects
        subject_mapping = {
            'admission': 'Admission Inquiry',
            'academic': 'Academic Information Request',
            'general': 'General Inquiry',
            'complaint': 'Complaint/Feedback',
            'other': 'Other Inquiry'
        }
        
        print(f"Final values: {first_name}, {last_name}, {email}, {phone}, {subject}, {message}")
        
        # Prepare email content
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
            # Send email to your school email address
            send_mail(
                subject=email_subject,
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['to-email.com'],  # Replace with where you want to receive emails
                fail_silently=False,
            )
            
            # Add success message and redirect to clean URL
            messages.success(request, "Your message has been sent successfully! We'll get back to you soon.")
            print("Email sent successfully")
            
        except Exception as e:
            print(f"Error sending email: {e}")
            messages.error(request, "Sorry, there was an error sending your message. Please try again or contact us directly.")
        
        return redirect('contact')
        
    return render(request,'contact.html')


def gallery(request):
    return render(request,'gallery.html')