from django.http import JsonResponse
from .models import Estudiante, Pago
# Descomentar cuando se cree el archivo ofiSecurity/auth0backend.py
#from monitoring.auth0backend import getRole

def estudiante_list(request):
    # Ensure the request method is GET
    if request.method == 'GET':
        # Fetch data from the database (assuming a model named Estudiante)
        estudiantes = Estudiante.objects.all().values()  # Get all records as a queryset of dictionaries
        estudiantes_list = list(estudiantes)  # Convert queryset to list for JSON serialization
        return JsonResponse(estudiantes_list, safe=False)  # Return JSON response
    
def pago_list(request):
    if request.method == 'GET':
        pagos = Pago.objects.all().values()
        pagos_list = list(pagos)
        return JsonResponse(pagos_list, safe=False)
