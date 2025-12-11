# ============================================
# TAREA SEMANA DOS
# ============================================
# EJEMPLO 2 - SISTEMA DE DESCRIPCIÓN DE VEHÍCULOS
# =============================================
# Clase base: Vehículo
# ============================================
# --------------------------------------------
# 1. ABSTRACCIÓN (Aplicada en la clase Vehículos)
# --------------------------------------------
# La abstracción en este enfoque, consiste en crear la
# clase Vehículo que contiene únicamente los atributos esenciales
# que definen su identidad. Ocultando cualquier lógica de funcionamiento interno
# (como arrancar o acelerar).
#
# La clase abstracta vehículo para establecer una descripción del
# vehículo, y luego  crearemos clases concretas como "coche y motocicleta".
# --------------------------------------------

class vehiculo:
    def __init__(self, tamaño, modelo, año):
        # =====================================================
        # 2. ENCAPSULAMIENTO (Protección de los datos)
        # -----------------------------------------------------
        # Además, se utilizan métodos getters y setters para
        # controlar el acceso a estos datos. Esto permite:
        # Validar valores antes de asignarlos
        # Proteger la integridad de la información
        # Evitar cambios directos no controlados
        # =====================================================
        self.__tamaño = tamaño
        self.__modelo = modelo
        self.__año = año
    # -------- MÉTODO DE ABSTRACCIÓN --------
    def mostrar_info(self):
        return f"{self.__tamaño} {self.__modelo} ({self.__año})"

    # -------- GETTERS Y SETTERS --------
    def get_tamaño(self):
        return self.__tamaño

    def get_modelo(self):
        return self.__modelo

    def get_año(self):
        return self.__año

    # SETTERS
    def set_tamaño(self, nuevo_tamaño):
        self.__tamaño = nuevo_tamaño

    def set_modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo

    def set_año(self, nuevo_año):
        self.__año = nuevo_año
# ============================================
#     HERENCIA: Coche y Motocicleta
# ============================================
# ---------------------------------------------------------
# 3. HERENCIA (Coche y Motocicleta heredan de Vehiculo)
# ---------------------------------------------------------
# La herencia permite crear nuevas clases basadas en una clase
# existente. En este ejemplo:
#
# • Coche(Vehiculo)
# • Motocicleta(Vehiculo)
# Gracias a la herencia:
# Se reutilizan los atributos tamaño, modelo, año
# ---------------------------------------------------------

class coche(vehiculo):
    # ---------------------------------------------
    # 4. POLIMORFISMO: método mostrar_info() redefinido
    # ---------------------------------------------
    # El polimorfismo permite que el mismo método (mostrar_info)
    # funcione diferente según el tipo de objeto.
    # Aquí, Coche redefine mostrar_info().
    # ---------------------------------------------
    def mostrar_info(self):
        return f"Descripción coche: {self.get_tamaño()} {self.get_modelo()} ({self.get_año()})"

class motocicleta(vehiculo):
    def __init__(self, tamaño, modelo, año):
        super().__init__(tamaño, modelo, año)

    def mostrar_info(self):
        return f"Descripción motocicleta: {self.get_tamaño()} {self.get_modelo()} ({self.get_año()})"
# ============================================
#     PROGRAMA PRINCIPAL (uso de las clases)
# ============================================

v1 = coche("Pequeño", "Toyota", "2026")
v2 = motocicleta("Pequeño", "Honda", "2020")

print(v1.mostrar_info())
print(v2.mostrar_info()) # ejemplo de polimorfismo

# =============================================
# EJEMPLO 2 - SISTEMA DE JUGUETES
# =============================================
# Clase base: Juguete
# =============================================
# ------------------------------------------------
# 1. ABSTRACCIÓN (Aplicada en la clase Juguete)
# ------------------------------------------------
# La abstracción consiste en crear la clase Juguete
# que representa las características esenciales de
# cualquier juguete: nombre, material y precio.
#
# Esta clase sirve de base para crear juguetes
# más específicos como Carro y Muñeca.
# ------------------------------------------------

class Juguete:
    def __init__(self, nombre, material, precio):
        # =====================================================
        # 2. ENCAPSULAMIENTO (Protección de los datos)
        # -----------------------------------------------------
        # Se usan atributos privados para evitar que sean
        # manipulados de forma directa desde fuera de la clase.
        # Los getters y setters permiten controlar el acceso.
        # =====================================================
        self.__nombre = nombre
        self.__material = material
        self.__precio = precio

    # -------- MÉTODO DE ABSTRACCIÓN --------
    def mostrar_info(self):
        return f"{self.__nombre} hecho de {self.__material}, precio: ${self.__precio}"

    # ------------ GETTERS ------------------
    def get_nombre(self):
        return self.__nombre

    def get_material(self):
        return self.__material

    def get_precio(self):
        return self.__precio

    # ------------ SETTERS ------------------
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_material(self, nuevo_material):
        self.__material = nuevo_material

    def set_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("El precio no puede ser negativo.")

# =============================================
# 3. HERENCIA: Carro Juguete y Muñeca Juguete
# =============================================
# Estas clases heredan los atributos de Juguete
# y agregan su propia implementación del método
# mostrar_info(), demostrando polimorfismo.
# =============================================

class CarroJuguete(Juguete):
    # ---------------------------------------------
    # 4. POLIMORFISMO: método mostrar_info redefinido
    # ---------------------------------------------
    def mostrar_info(self):
        return (
            f"Carro de juguete: {self.get_nombre()}, "
            f"Material: {self.get_material()}, Precio: ${self.get_precio()}"
        )

class MuñecaJuguete(Juguete):
    def __init__(self, nombre, material, precio):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, material, precio)

    def mostrar_info(self):
        return (
            f"Muñeca: {self.get_nombre()}, "
            f"Material: {self.get_material()}, Precio: ${self.get_precio()}"
        )

# =============================================
#     PROGRAMA PRINCIPAL (uso de las clases)
# =============================================

j1 = CarroJuguete("Auto de carreras", "Plástico", 15)
j2 = MuñecaJuguete("Sofia", "Tela", 7.50)

print(j1.mostrar_info())
print(j2.mostrar_info())   # Ejemplo de polimorfismo