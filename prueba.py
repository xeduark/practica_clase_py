import firebase_admin
from firebase_admin import credentials, firestore

# Ruta al archivo JSON de la cuenta de servicio
cred = credentials.Certificate("C:/Users/2811750/Downloads/practicapython-9823d-firebase-adminsdk-94nzy-31185a8ebe.json")

# Inicializar la app de Firebase
try:
    firebase_admin.initialize_app(cred)
except ValueError:
    print("La app de Firebase ya está inicializada.")

# Conectar a la base de datos Firestore
db = firestore.client()

# Referencia a la colección
usuarios_ref = db.collection('usuarios')

# Consultar todos los documentos en la colección "usuarios"
usuarios = usuarios_ref.get()

# Imprimir los datos de cada documento
for usuario in usuarios:
    print(f'{usuario.id} => {usuario.to_dict()}')
