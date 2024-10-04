import streamlit as st
import pandas as pd
import io  # Para capturar la salida de df.info()

# Función para mostrar el análisis del CSV
def mostrar_analisis_csv():
    st.title("Actividad 1, semana 9")
    
    # Cargar el CSV
    df = pd.read_csv('dat/datos_demograficos.csv')
    
    # Mostrar las primeras 5 filas del DataFrame
    st.subheader("Primeras 5 filas del DataFrame")
    st.dataframe(df.head())
    
    # Obtener la información general del DataFrame
    st.subheader("Información general del DataFrame")
    
    # Redirigir la salida de df.info() a un buffer de texto
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    
    # Mostrar el contenido del buffer en un área de texto
    st.text_area("Info del DataFrame", info_str, height=200)
    
    # Calcular las estadísticas descriptivas de las columnas numéricas
    st.subheader("Estadísticas descriptivas")
    st.dataframe(df.describe())
    
    # Encontrar los valores únicos de la columna "País"
    st.subheader("Valores únicos de la columna 'País'")
    paises_unicos = df["País"].unique()
    st.write(paises_unicos)
    
    # Contar la cantidad de ocurrencias de cada valor en la columna "Género"
    st.subheader("Conteo de ocurrencias en la columna 'Género'")
    conteo_genero = df["Género"].value_counts()
    st.bar_chart(conteo_genero)
