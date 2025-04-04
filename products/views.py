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
    return render(request, 'product-list.html')

# Checkout page view
def checkout_view(request):
    return render(request, 'checkout.html')

# Cart page view
def cart_view(request):
    return render(request, 'cart.html')

# Login and Registration page view
def login_registration_view(request):
    return render(request, 'login-registration.html')

# Contact page view
def contact_view(request):
    return render(request, 'contact.html')

# Blog single view
def blog_single_view(request):
    return render(request, 'blog-single.html')

# URL patterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('course-grid/', views.course_grid_view, name='course_grid_view'),
    path('products/', views.product_list_view, name='product_list_view'),
]
