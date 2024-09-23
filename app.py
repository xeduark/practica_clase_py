import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# Inicializar Firebase
cred = credentials.Certificate("C:/Users/2811750/Downloads/practicapython-9823d-firebase-adminsdk-94nzy-31185a8ebe.json")
firebase_admin.initialize_app(cred)

# Conectar a Firestore
db = firestore.client()
usuarios_ref = db.collection('usuarios')

# Título de la aplicación
st.title("Visualización de Usuarios en Firestore")

# Consultar todos los documentos en la colección "usuarios"
usuarios = usuarios_ref.get()

# Crear una lista para almacenar los datos
data = []

# Agregar los datos a la lista
for usuario in usuarios:
    user_data = usuario.to_dict()
    user_data['ID'] = usuario.id  # Agregar el ID del documento
    data.append(user_data)

# Convertir la lista a un DataFrame de pandas
df = pd.DataFrame(data)

# Mostrar datos en una tabla de Streamlit
if not df.empty:
    st.dataframe(df)  # o st.table(df) para una tabla estática
else:
    st.write("No se encontraron usuarios.")
#streamlit run app.py para arrancar la app
