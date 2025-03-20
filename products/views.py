from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

# Home page view (index-7.html) which requires the user to be logged in
@login_required
def home_view(request):
    return render(request, 'index-7.html')

# About page view
def about_view(request):
    return render(request, 'about.html')

# Course grid page view
def course_grid_view(request):
    return render(request, 'course-grid.html')

# Product list page view
def product_list_view(request):
    return render(request, 'product-list-filter.html')

# Checkout page view
def checkout_view(request):
    return render(request, 'checkout.html')

# Cart page view
def cart_view(request):
    return render(request, 'cart.html')

# Login and Registration page view with authentication logic
def login_registration_view(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            # Get the username and password from the form submission
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log in the user
                login(request, user)
                # Redirect to the home page (index-7.html) after successful login
                return redirect('home')
            else:
                # If login fails, return the same page with an error message
                messages.error(request, 'Invalid credentials')
                return render(request, 'login-registration.html')

        elif 'register' in request.POST:
            # Get registration details from the form
            username = request.POST.get('user-name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                # Create a new user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('login')  # Redirect to the login page after successful registration

    # If it's a GET request, just show the login-registration page
    return render(request, 'login-registration.html')

# Contact page view
def contact_view(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Construct the full message
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            # Send the email
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,  # Use the email from settings
                ['georgerubinga@gmail.com'],  # Replace with the actual recipient email
                fail_silently=False,
            )
            # Return success response
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            # Log the error and return error response
            logger.error(f"Error sending email: {e}")
            messages.error(request, f"An error occurred: {str(e)}")

        # Redirect back to the contact page
        return redirect('contact')

    # If it's a GET request, render the contact page
    return render(request, 'contact.html')

# Blog single view
def blog_single_view(request):
    return render(request, 'blog-single.html')
