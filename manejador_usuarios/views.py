from rest_framework import generics
from .models import Estudiante, Pago
from .serializers import EstudianteSerializer, PagoSerializer

class EstudianteListView(generics.ListAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class PagoListView(generics.ListAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer