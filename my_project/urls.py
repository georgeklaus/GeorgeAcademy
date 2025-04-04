"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products import views  # Import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_registration_view, name='login'),  # Set login-registration as the homepage
    path('home/', views.home_view, name='home'),  # Main page (index-7.html)
    path('about/', views.about_view, name='about'),  # About page
    path('course-grid/', views.course_grid_view, name='course_grid_view'),  # Course grid page
    path('products/', views.product_list_view, name='product_list_view'),  # Products page
    path('checkout/', views.checkout_view, name='checkout'),  # Checkout page
    path('cart/', views.cart_view, name='cart'),  # Cart page
    path('contact/', views.contact_view, name='contact'),  # Contact page
    path('blog-single/', views.blog_single_view, name='blog_single'),  # Blog single page
]
