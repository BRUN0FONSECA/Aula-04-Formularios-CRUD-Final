"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from appdobruno import views

urlpatterns = [
  path("", views.home, name="home"),
  path('admin/', admin.site.urls),
  path("surfistas",views.create_surfista),
  path("lugares",views.create_lugar),
  path("Fsurf",views.create_f),
  path("surfistas/update/<id>",views.update_surfista),
  path("Fsurf/update/<id>",views.update_fsurfista),
  path("lugares/update/<id>",views.update_lugar),
  path("surfistas/delete/<id>",views.delete_surfista),
  path("Fsurf/delete/<id>",views.delete_fsurfista),
  path("lugares/delete/<id>",views.delete_lugar),
