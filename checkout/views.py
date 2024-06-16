from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag right now")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PSDwORuwltIR9H7KNm7BMRI1MLMJD0FYamCQoMxBDyFZeWD4OY3IuKOMeFhookpF2TSDh7llupkmdXJjG6DwMwe00YIP6AK7o',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)