import logging
from cliente import Cliente

# Configuración de logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# Función de logging interactivo
def log_interactivo():
    print("Selecciona el nivel de logging:")
    print("1. DEBUG")
    print("2. INFO")
    print("3. WARNING")
    print("4. ERROR")
    print("5. CRITICAL")

    opcion = input("Ingresa el número del nivel de logging: ")

    niveles = {
        '1': logging.DEBUG,
        '2': logging.INFO,
        '3': logging.WARNING,
        '4': logging.ERROR,
        '5': logging.CRITICAL
    }

    nivel = niveles.get(opcion, logging.INFO)
    mensaje = input("Ingresa el mensaje a loggear: ")

    logging.log(nivel, mensaje)

# Crear un cliente de ejemplo
cliente1 = Cliente("Mara", "mara@example.com", 25, "C1234")
print(cliente1)
print(cliente1.actualizar_email("nuevoemail@example.com"))
print("¿Es mayor de edad?", cliente1.es_mayor_de_edad())

# Llamar al logging interactivo
log_interactivo()
