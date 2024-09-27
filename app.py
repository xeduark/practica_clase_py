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

# Función para agregar un nuevo usuario
def agregar_usuario(nombre, edad, ciudad):
    usuarios_ref.add({"nombre": nombre, "edad": edad, "ciudad": ciudad})
    st.success("Usuario agregado exitosamente")

# Función para eliminar un usuario
def eliminar_usuario(user_id):
    usuarios_ref.document(user_id).delete()
    st.success(f"Usuario con ID {user_id} eliminado exitosamente")

# Función para editar un usuario existente
def editar_usuario(user_id, nombre, edad, ciudad):
    usuarios_ref.document(user_id).set({"nombre": nombre, "edad": edad, "ciudad": ciudad})
    st.success(f"Usuario con ID {user_id} actualizado exitosamente")

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

# Formulario para agregar un nuevo usuario
st.subheader("Agregar nuevo usuario")
with st.form("Agregar usuario"):
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", min_value=1)
    ciudad = st.text_input("Ciudad")
    submit_agregar = st.form_submit_button("Agregar")
    if submit_agregar:
        agregar_usuario(nombre, edad, ciudad)

# Formulario para editar un usuario existente
st.subheader("Editar usuario existente")
with st.form("Editar usuario"):
    user_id = st.selectbox("Selecciona el ID del usuario", df["ID"] if not df.empty else [])
    nombre = st.text_input("Nuevo nombre")
    edad = st.number_input("Nueva edad", min_value=1)
    ciudad = st.text_input("Nueva ciudad")
    submit_editar = st.form_submit_button("Editar")
    if submit_editar:
        editar_usuario(user_id, nombre, edad, ciudad)

# Formulario para eliminar un usuario
st.subheader("Eliminar usuario")
with st.form("Eliminar usuario"):
    user_id = st.selectbox("Selecciona el ID del usuario a eliminar", df["ID"] if not df.empty else [])
    submit_eliminar = st.form_submit_button("Eliminar")
    if submit_eliminar:
        eliminar_usuario(user_id)
#streamlit run app.py para arrancar la app
