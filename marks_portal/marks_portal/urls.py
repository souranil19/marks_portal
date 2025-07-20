"""
URL configuration for marks_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.school_landing, name='landing_page'),
    path('morning_school/', views.morning_school_landing, name='morning_school_landing'),
    path('day_school/', views.day_school_landing, name='day_school_landing'),
    path('vocational/', views.vocational_landing, name='vocational_landing'),
    path('login/', include('student_front_login.urls')),
    path('teacher/', include('teacher.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
