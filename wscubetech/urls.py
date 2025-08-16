"""
URL configuration for wscubetech project.

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
from wscubetech import views
from django.contrib import admin
from django.urls import path
from wscubetech import views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('about/', views.aboutUs, name='about'),
    path('services/', views.services, name='services'),
    path('submitform/', views.submitform, name='submitform'),
    path('contact/', views.contact, name='contact'),
    path('course/', views.course, name='course'),  # Updated view reference
    path('course/<int:courseid>/', views.courseDetails, name='course-details'),
    path('userform', views.userform),
]
