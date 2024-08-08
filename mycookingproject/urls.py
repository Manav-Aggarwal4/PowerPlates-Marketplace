from django.contrib import admin
from django.urls import path, include
from two_factor.urls import urlpatterns as tf_urls
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include(tf_urls)),  # Ensure this includes two-factor auth URLs
    path('', include('myapp.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),
]
