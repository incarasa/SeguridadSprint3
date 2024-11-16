# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('estudiantes/', views.estudiante_list, name='estudiante_list'),
    path('pagos/', views.pago_list, name='pago_list'),
]