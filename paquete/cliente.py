class Cliente:
    # Atributo de clase opcional
    empresa = "FrutillaCorp"

    def __init__(self, nombre, email, edad, cliente_id):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.cliente_id = cliente_id

    def __str__(self):
        return f"Cliente: {self.nombre} (ID: {self.cliente_id})"

    # Método 1: Actualizar el email
    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email
        return f"Email actualizado a {self.email}"

    # Método 2: Verificar si es mayor de edad
    def es_mayor_de_edad(self):
        return self.edad >= 18
