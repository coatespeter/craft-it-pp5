# interactions/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('faq/', views.faq_view, name='faq'),
    path('testimonials/', views.testimonial_view, name='testimonial'),
    path('contact/', views.contact_view, name='contact'),
]
