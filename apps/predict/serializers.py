# Aqui estaré creando mi API REST para el modelo de predicción de clima
from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    humedad = serializers.FloatField()
    velocidad_viento = serializers.FloatField()
    wind_bearing = serializers.FloatField()
    visibilidad = serializers.FloatField()
    presion = serializers.FloatField()
    mes = serializers.IntegerField()
    hora = serializers.IntegerField() 