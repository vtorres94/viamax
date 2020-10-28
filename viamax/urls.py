"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from polls.views import index, date, calcularEdad, pagadores_list, pagador_view, pagador_create, pagador_update, pagador_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('pagadores/', pagadores_list),
    path('pagadores/<int:id>', pagador_view),
    path('pagadores/save/', pagador_create),
    path('pagadores/edit/<int:pk>/', pagador_update),
    path('pagadores/delete/<int:pk>', pagador_delete),
    path('fecha/', date),
    path('edad/<int:edad>/<int:year>/', calcularEdad),
]


