from django.db import models

class FAQ(models.Model):
    """model representing a frequently asked question and its answer"""
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Testimonial(models.Model):
    """ Model representing a testimonial from a customer or user."""
    name = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f"Testimonial from {self.name}"


class Contact(models.Model):
    """Model representing a contact message sent by a user."""
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.name} ({self.email})"
