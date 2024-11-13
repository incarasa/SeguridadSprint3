from rest_framework import serializers
from .models import Estudiante, Pago

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'  # Incluye todos los campos del modelo

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'  # Incluye todos los campos del modelo