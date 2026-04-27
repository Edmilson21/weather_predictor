import joblib
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictionSerializer
from django.shortcuts import render
import os
from predict.train import entrenar_modelo

# Cargar el modelo entrenado
if not os.path.exists('modelo/weather_model.pkl'):
    entrenar_modelo()

model = joblib.load('modelo/weather_model.pkl')

def index(request):
    return render(request, 'index.html')

class PredecirTiempo(APIView):
    def post(self, request): 
        serializer = PredictionSerializer(data=request.data)
        if serializer.is_valid():
            datos = serializer.validated_data
            entrada = np.array([[
                datos['humedad'],
                datos['velocidad_viento'],
                datos['wind_bearing'],
                datos['visibilidad'],
                datos['presion'],
                datos['mes'],
                datos['hora']
            ]])
            prediccion = model.predict(entrada)
            return Response({
                'temperatura': round(prediccion[0], 2)
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    