# ======================================
# CLASE ASIENTO
# ======================================

class Asiento:
    def __init__(self, numero: int):
        self.numero = numero
        self.disponible = True  # El asiento inicia disponible

    def reservar(self):
        if self.disponible:
            self.disponible = False
            print(f"Asiento {self.numero} reservado correctamente.")
        else:
            print(f"Asiento {self.numero} no está disponible.")

    def liberar(self):
        self.disponible = True
        print(f"Asiento {self.numero} ahora está disponible.")


# ======================================
# CLASE FUNCION (PELÍCULA)
# ======================================

class Funcion:
    def __init__(self, pelicula: str, horario: str, total_asientos: int):
        self.pelicula = pelicula
        self.horario = horario
        self.asientos = []

        # Crear los asientos automáticamente
        for i in range(1, total_asientos + 1):
            self.asientos.append(Asiento(i))

    def mostrar_asientos(self):
        print(f"\nAsientos para '{self.pelicula}' a las {self.horario}:")
        for asiento in self.asientos:
            estado = "Disponible" if asiento.disponible else "Ocupado"
            print(f"Asiento {asiento.numero}: {estado}")

    def buscar_asiento(self, numero: int):
        for asiento in self.asientos:
            if asiento.numero == numero:
                return asiento
        return None


# ===============================
# PROGRAMA PRINCIPAL
# ===============================

# Crear una función de cine
funcion = Funcion("Avengers", "7:00 PM", 5)

while True:
    print("\n===== SISTEMA DE RESERVAS DE CINE =====")
    print("1. Ver asientos")
    print("2. Reservar asiento")
    print("3. Liberar asiento")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        funcion.mostrar_asientos()

    elif opcion == "2":
        numero = int(input("Ingrese el número del asiento a reservar: "))
        asiento = funcion.buscar_asiento(numero)

        if asiento:
            asiento.reservar()
        else:
            print("Asiento no encontrado.")

    elif opcion == "3":
        numero = int(input("Ingrese el número del asiento a liberar: "))
        asiento = funcion.buscar_asiento(numero)

        if asiento:
            asiento.liberar()
        else:
            print("Asiento no encontrado.")

    elif opcion == "4":
        print("Gracias por usar el sistema de reservas de cine.")
        break

    else:
        print("Opción no válida.")