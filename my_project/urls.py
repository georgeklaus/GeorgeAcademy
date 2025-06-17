from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from products import views

urlpatterns = [
    # Root URL now points to login/registration
    path('', views.login_registration, name='login'),
    path('admin/', admin.site.urls),
    
    # Authentication URLs
    path('login/', views.login_registration, name='login'),  # Keep this as alias
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Application URLs
    path('home/', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('course-grid/', views.course_grid_view, name='course_grid'),
    path('products/', views.product_list_view, name='product_list'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('cart/', views.cart_view, name='cart'),
    path('contact/', views.contact_view, name='contact'),
    path('blog-single/', views.blog_single_view, name='blog_single'),

    # Debug route
    path('debug/', views.debug_info),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
