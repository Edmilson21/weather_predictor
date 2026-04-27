import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os


def entrenar_modelo():
    df = pd.read_csv('dataset/weatherHistory.csv')
    
    df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
    df['mes'] = df['Formatted Date'].dt.month
    df['hora'] = df['Formatted Date'].dt.hour
    
    df = df.drop(columns=['Formatted Date', 'Summary', 'Daily Summary', 
                           'Precip Type', 'Loud Cover', 'Apparent Temperature (C)'])
    
    X = df.drop('Temperature (C)', axis=1)
    y = df['Temperature (C)']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    
    os.makedirs('modelo', exist_ok=True)
    joblib.dump(model, 'modelo/weather_model.pkl')
    print("Modelo entrenado y guardado") 