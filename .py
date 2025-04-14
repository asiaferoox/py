import logging
import logging

# Configuración básica del logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# Función interactiva para obtener el nivel de log y mensaje
def log_interactivo():
    print("Selecciona el nivel de logging:")
    print("1. DEBUG")
    print("2. INFO")
    print("3. WARNING")
    print("4. ERROR")
    print("5. CRITICAL")

    # Opción seleccionada por el usuario
    opcion = input("Ingresa el número del nivel de logging: ")

    # Mapea la opción a un nivel de logging
    if opcion == '1':
        nivel = logging.DEBUG
    elif opcion == '2':
        nivel = logging.INFO
    elif opcion == '3':
        nivel = logging.WARNING
    elif opcion == '4':
        nivel = logging.ERROR
    elif opcion == '5':
        nivel = logging.CRITICAL
    else:
        print("Opción no válida. Usando nivel INFO por defecto.")
        nivel = logging.INFO

    # Mensaje que el usuario quiere loggear
    mensaje = input("Ingresa el mensaje a loggear: ")

    # Loggear el mensaje con el nivel seleccionado
    if nivel == logging.DEBUG:
        logging.debug(mensaje)
    elif nivel == logging.INFO:
        logging.info(mensaje)
    elif nivel == logging.WARNING:
        logging.warning(mensaje)
    elif nivel == logging.ERROR:
        logging.error(mensaje)
    elif nivel == logging.CRITICAL:
        logging.critical(mensaje)

# Llamada a la función interactiva
log_interactivo()
