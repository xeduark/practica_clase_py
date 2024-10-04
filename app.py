import streamlit as st
from views import gestion_usuarios, analisis_csv  # Importa los módulos correctos

# Configuración de la página del dashboard
st.set_page_config(page_title="Dashboard Actividades", layout="wide")

# Menú en la barra lateral
menu = st.sidebar.selectbox("Seleccione una opción", ["Inicio", "Gestión de Usuarios", "Análisis de CSV"])

# Página de inicio
if menu == "Inicio":
    st.title("Bienvenido a mis actividades 3 nivel")
    st.write("Aquí encontrarás las actividades que realizo para la asignatura de nuevas tecnologías.")

# Página de gestión de usuarios
elif menu == "Gestión de Usuarios":
    gestion_usuarios.mostrar_gestion_usuarios()  # Llama a la función del módulo gestion_usuarios

# Página de análisis del CSV
elif menu == "Análisis de CSV":
    analisis_csv.mostrar_analisis_csv()  # Llama a la función del módulo analisis_csv  quiero usar esta modlaidad de sidebar pero solo el gestion de usuarios quiero que sea un submenu para acceder a agregar o eliminar usuarios
