from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
import logging
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


logger = logging.getLogger(__name__)

# Home page view - now requires login
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
    return render(request, 'product-list-filter.html')

# Checkout page view
@login_required
def checkout_view(request):
    return render(request, 'checkout.html')

# Cart page view
@login_required
def cart_view(request):
    return render(request, 'cart.html')

# Login and Registration page view - now handles root URL

def login_registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form_type = request.GET.get('form', 'login')
    next_url = request.GET.get('next', '/home/')
    
    if request.method == 'POST':
        # Determine which form was submitted
        if 'login_submit' in request.POST:
            return handle_login(request, next_url)
        elif 'register_submit' in request.POST:
            return handle_register(request)
    
    return render(request, 'login_registration.html', {'form_type': form_type, 'next': next_url})

def handle_login(request, next_url):
    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '').strip()
    
    # Basic validation
    if not username or not password:
        messages.error(request, 'Both username and password are required')
        return render(request, 'login_registration.html', {'form_type': 'login', 'next': next_url})
    
    # Authenticate user
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return redirect(next_url)
    else:
        # More specific error messages
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username does not exist')
        else:
            messages.error(request, 'Incorrect password')
        return render(request, 'login_registration.html', {'form_type': 'login', 'next': next_url})

def handle_register(request):
    username = request.POST.get('username', '').strip()
    email = request.POST.get('email', '').strip()
    password1 = request.POST.get('password1', '').strip()
    password2 = request.POST.get('password2', '').strip()
    
    errors = []
    
    # Validate username
    if not username:
        errors.append("Username is required")
    elif len(username) < 4:
        errors.append("Username must be at least 4 characters")
    elif User.objects.filter(username=username).exists():
        errors.append("Username already exists")
    
    # Validate email
    if not email:
        errors.append("Email is required")
    else:
        try:
            validate_email(email)
            if User.objects.filter(email=email).exists():
                errors.append("Email already exists")
        except ValidationError:
            errors.append("Invalid email format")
    
    # Validate password
    if not password1 or not password2:
        errors.append("Both password fields are required")
    elif password1 != password2:
        errors.append("Passwords do not match")
    elif len(password1) < 8:
        errors.append("Password must be at least 8 characters")
    
    # Create user if no errors
    if errors:
        for error in errors:
            messages.error(request, error)
        return render(request, 'login_registration.html', {'form_type': 'register'})
    
    try:
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        
        # Auto-login after registration
        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect('home')
        else:
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
            
    except Exception as e:
        logger.error(f"Registration error: {str(e)}")
        messages.error(request, "An unexpected error occurred. Please try again.")
        return render(request, 'login_registration.html', {'form_type': 'register'})
# Contact page view
@login_required
def contact_view(request):
    return render(request, 'contact.html')

# Blog single view
@login_required
def blog_single_view(request):
    return render(request, 'blog-single.html')