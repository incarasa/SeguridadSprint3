# urls.py
from django.urls import path
from .views import EstudianteListView, PagoListView

urlpatterns = [
    path('estudiantes/', EstudianteListView.as_view(), name='estudiante-list'),
    path('pagos/', PagoListView.as_view(), name='pago-list'),
]