from django.shortcuts import render
from .models import FAQ, Testimonial, Contact  # Ensure all models are imported

def faq_view(request):
    faqs = FAQ.objects.all()
    return render(request, 'interactions/faq.html', {'faqs': faqs})

def testimonial_view(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'interactions/testimonial.html', {'testimonials': testimonials})

def contact_view(request):
    return render(request, 'interactions/contact.html')
