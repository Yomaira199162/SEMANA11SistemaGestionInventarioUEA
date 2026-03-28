# Tarea: Aplicación de Conceptos de POO en Python
# Autor: [Yomaira Guaycha]

class Empleado:
    """Clase Base que representa a un empleado genérico."""

    def __init__(self, nombre, salario_base):
        # ENCAPSULACIÓN: Usamos doble guion bajo (__) para que los atributos sean privados
        self.__nombre = nombre
        self.__salario_base = salario_base

    # Métodos Getter para acceder a atributos encapsulados
    def obtener_nombre(self):
        return self.__nombre

    def obtener_salario_base(self):
        return self.__salario_base

    def calcular_pago(self):
        """Método que será sobrescrito (Polimorfismo)"""
        return self.__salario_base

    def mostrar_informacion(self):
        print(f"Empleado: {self.__nombre} | Pago total: ${self.calcular_pago()}")


class Desarrollador(Empleado):
    """CLASE DERIVADA (Herencia) que extiende de Empleado."""

    def __init__(self, nombre, salario_base, lenguaje_dominante):
        # Llamada al constructor de la clase base
        super().__init__(nombre, salario_base)
        self.lenguaje = lenguaje_dominante

    # POLIMORFISMO: Sobrescritura del método calcular_pago
    def calcular_pago(self):
        # Los desarrolladores reciben un bono fijo de $500 por proyectos
        bono = 500
        return self.obtener_salario_base() + bono


class Vendedor(Empleado):
    """CLASE DERIVADA (Herencia) que extiende de Empleado."""

    def __init__(self, nombre, salario_base, ventas_realizadas):
        super().__init__(nombre, salario_base)
        self.ventas = ventas_realizadas

    # POLIMORFISMO: Sobrescritura del método calcular_pago
    def calcular_pago(self):
        # Los vendedores reciben una comisión del 10% de sus ventas
        comision = self.ventas * 0.10
        return self.obtener_salario_base() + comision


# --- DEMOSTRACIÓN DEL PROGRAMA ---
if __name__ == "__main__":
    print("--- Sistema de Gestión de RRHH ---")

    # Creación de instancias (Objetos)
    dev = Desarrollador("Ana García", 2500, "Python")
    vendedor = Vendedor("Carlos Pérez", 1800, 5000)
    empleado_comun = Empleado("Luis Soto", 1500)

    # Lista de empleados para demostrar polimorfismo en un ciclo
    nomina = [dev, vendedor, empleado_comun]

    for persona in nomina:
        # Se llama al mismo método, pero cada objeto reacciona de forma distinta (Polimorfismo)
        persona.mostrar_informacion()