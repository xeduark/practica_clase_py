def saludar(nombre):
    """
    Función que saluda a una persona.

    Args:
        nombre: El nombre de la persona a la que se saluda.

    Returns:
        Un mensaje de saludo.
    """
    return f"¡Hola, {nombre}!"

def despedirse(nombre):
    """
    Función que se despide de una persona.

    Args:
        nombre: El nombre de la persona a la que se despide.

    Returns:
        Un mensaje de despedida.
    """
    return f"¡Adiós, {nombre}!"

def preguntar_como_esta(nombre):
    """
    Función que pregunta cómo está la persona.

    Args:
        nombre: El nombre de la persona a la que se pregunta.

    Returns:
        Un mensaje preguntando cómo está.
    """
    return f"¿Cómo estás, {nombre}?"

def felicitar_cumpleanos(nombre):
    """
    Función que felicita a una persona por su cumpleaños.

    Args:
        nombre: El nombre de la persona a la que se felicita.

    Returns:
        Un mensaje de felicitación por el cumpleaños.
    """
    return f"¡Feliz cumpleaños, {nombre}!"

def preguntar_dia_semana():
    """
    Función que pregunta por el día de la semana.

    Returns:
        Un mensaje preguntando por el día de la semana.
    """
    import datetime
    dia_semana = datetime.datetime.now().strftime("%A")
    return f"Hoy es {dia_semana}. ¿Cómo va tu día?"

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    saludo = saludar(nombre)
    print(saludo)

    estado = preguntar_como_esta(nombre)
    print(estado)

    cumpleaños = input("¿Es tu cumpleaños hoy? (sí/no): ").strip().lower()
    if cumpleaños == "sí":
        print(felicitar_cumpleanos(nombre))

    dia_semana_mensaje = preguntar_dia_semana()
    print(dia_semana_mensaje)

    despedida = despedirse(nombre)
    print(despedida)
