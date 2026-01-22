from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Scheme


def index(request):
    """Home page view"""
    return render(request, 'website/index.html')


def about(request):
    """About page view"""
    return render(request, 'website/about.html')


def schemes(request):
    """Schemes page view - displays all active schemes"""
    schemes_list = Scheme.objects.filter(is_active=True).order_by('created_at')
    return render(request, 'website/schemes.html', {'schemes': schemes_list})


def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message')
        
        # Here you can add logic to save the contact form data
        # For example, create a Contact model and save it
        # Or send an email notification
        
        messages.success(request, 'Thank you! Your message has been sent successfully. We\'ll get back to you soon.')
        return redirect('contact')
    
    return render(request, 'website/contact.html')

