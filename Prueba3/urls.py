"""
URL configuration for Prueba3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
]

from firstApp.views import userRegistrationView, lista_clientes, eliminarCliente, actualizarCliente
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', lista_clientes, name='index'),
    path('registrar/', userRegistrationView),
    path('eliminar/<int:id>', eliminarCliente),
    path('actualizar/<int:id>', actualizarCliente)
]
