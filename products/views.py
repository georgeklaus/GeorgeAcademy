from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
import logging

logger = logging.getLogger(__name__)

# Home page view (index-7.html) which requires the user to be logged in
@login_required
def home_view(request):
    return render(request, 'index-7.html')

# About page view
@login_required
def about_view(request):
    return render(request, 'about.html')

# Course grid page view
@login_required
def course_grid_view(request):
    return render(request, 'course-grid.html')

# Product list page view
@login_required
def product_list_view(request):
    return render(request, 'product-list.html')

# Checkout page view
@login_required
def checkout_view(request):
    return render(request, 'checkout.html')

# Cart page view
@login_required
def cart_view(request):
    return render(request, 'cart.html')

# Login and Registration page view
def login_registration(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the homepage after login
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()  # Display an empty login form for GET requests
    return render(request, 'login-registration.html', {'form': form})

# Contact page view
@login_required
def contact_view(request):
    return render(request, 'contact.html')

# Blog single view
@login_required
def blog_single_view(request):
    return render(request, 'blog-single.html')
