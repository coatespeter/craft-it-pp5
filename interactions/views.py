from django.shortcuts import render
from .models import FAQ, Testimonial, Contact 
from .forms import ContactForm 
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
# Ensure all models are imported

def faq_view(request):
    faqs = FAQ.objects.all()
    return render(request, 'interactions/faq.html', {'faqs': faqs})

def testimonial_view(request):
    """"a view to display all testimonials"""
    testimonials = Testimonial.objects.all()
    return render(request, 'interactions/testimonial.html', {'testimonials': testimonials})

def contact_view(request):
    """a view to handle the contact form and send an email to the admin"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # Send an email (optional, if you want email notifications)
            send_mail(
                'New Contact Form Submission',
                f'Message from {contact.name}: {contact.message}',
                'webmaster@example.com',
                ['admin@example.com'],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'interactions/contact.html', {'form': form})