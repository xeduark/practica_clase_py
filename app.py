import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# Inicializar Firebase
# cred = credentials.Certificate("C:/Users/2811750/Downloads/practicapython-9823d-firebase-adminsdk-94nzy-31185a8ebe.json")
# firebase_admin.initialize_app(cred)

# Verificar si la app ya está inicializada
if not firebase_admin._apps:
    cred = credentials.Certificate("C:/Users/2811750/Downloads/practicapython-9823d-firebase-adminsdk-94nzy-31185a8ebe.json")
    firebase_admin.initialize_app(cred)

# Conectar a Firestore
db = firestore.client()
usuarios_ref = db.collection('usuarios')

# Título de la aplicación
st.title("Gestión de Usuarios")

# Funciones de agregar, eliminar y editar usuario
def agregar_usuario(nombre, edad, ciudad):
    usuarios_ref.add({"nombre": nombre, "edad": edad, "ciudad": ciudad})
    st.success("Usuario agregado exitosamente")

def eliminar_usuario(user_id):
    usuarios_ref.document(user_id).delete()
    st.success(f"Usuario con ID {user_id} eliminado exitosamente")

def editar_usuario(user_id, nombre, edad, ciudad):
    usuarios_ref.document(user_id).set({"nombre": nombre, "edad": edad, "ciudad": ciudad})
    st.success(f"Usuario con ID {user_id} actualizado exitosamente")

# Consultar usuarios y mostrarlos en una tabla
usuarios = usuarios_ref.get()
data = []
for usuario in usuarios:
    user_data = usuario.to_dict()
    user_data['ID'] = usuario.id
    data.append(user_data)

df = pd.DataFrame(data)

if not df.empty:
    st.dataframe(df)
else:
    st.write("No se encontraron usuarios.")

# Formularios para agregar, editar y eliminar usuarios
st.subheader("Agregar nuevo usuario")
with st.form("Agregar usuario"):
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", min_value=1)
    ciudad = st.text_input("Ciudad")
    submit_agregar = st.form_submit_button("Agregar")
    if submit_agregar:
        agregar_usuario(nombre, edad, ciudad)

st.subheader("Editar usuario existente")
with st.form("Editar usuario"):
    user_id = st.selectbox("Selecciona el ID del usuario", df["ID"] if not df.empty else [])
    nombre = st.text_input("Nuevo nombre")
    edad = st.number_input("Nueva edad", min_value=1)
    ciudad = st.text_input("Nueva ciudad")
    submit_editar = st.form_submit_button("Editar")
    if submit_editar:
        editar_usuario(user_id, nombre, edad, ciudad)

st.subheader("Eliminar usuario")
with st.form("Eliminar usuario"):
    user_id = st.selectbox("Selecciona el ID del usuario a eliminar", df["ID"] if not df.empty else [])
    submit_eliminar = st.form_submit_button("Eliminar")
    if submit_eliminar:
        eliminar_usuario(user_id)
#streamlit run app.py para arrancar la app
