from django.urls import path
from apps.predict import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predecir/', views.PredecirTiempo.as_view(), name='predecir_tiempo'),

] 