import firebase_admin
from firebase_admin import credentials, firestore

# Inicializar Firebase solo si no está ya inicializado
def obtener_firestore():
    if not firebase_admin._apps:
        cred = credentials.Certificate("C:/Users/2811750/Downloads/practicapython-9823d-firebase-adminsdk-94nzy-31185a8ebe.json")
        firebase_admin.initialize_app(cred)
    return firestore.client()
