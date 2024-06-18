from django.shortcuts import render

def faq(request):
    return render(request, 'faq.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    return render(request, 'contact.html')
