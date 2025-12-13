# =========================================================
# TAREA SEMANA TRES
# =========================================================
# EJEMPLO  DE PRACTICA POO EN PYTHON
# =========================================================
# En este código se alican los principios de POO:
# Clase base: Registro de clima
# Encapsulamiento (atributo privado __temperatura)
# Herencia (ClimaSemanaExtendida)
# Polomorfismo (sobreescritura del método promedio_semanal)
# =========================================================
class RegistroClima:
    """
    Clase que representa un registro semanal de temperaturas en Ecuador
    provincia Azuay.
    """

    def __init__(self):
        # Atributo privado con temperaturas predefinidas
        self.__temperaturas = [22.5, 24.0, 23.3, 25.1, 26.0, 24.8, 23.9]
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def mostrar_temperaturas(self):
        """
        Muestra cada temperatura con su día correspondiente.
        """
        print("=== Temperatura semanal predifinidas ===")
        for dia, temp in zip(self.dias, self.__temperaturas):
            print(f"{dia}: {temp}°C")

    def obtener_temperaturas(self):
        """
        Retorna la lista de temperaturas predefinidas.
        """
        return self.__temperaturas

    def calcular_promedio(self):
        """
        Calcula el promedio de las temperaturas.
        """
        return sum(self.__temperaturas) / len(self.__temperaturas)

class RegistroClimaExtendido(RegistroClima):
    """
    Clase que represeta un día con su temperatura.
    """

    def mostrar_resumen(self):
        """
        Muestra el promedio semanal usando el método heredado.
        """
        print("\n" + "="*10+ " Promedio semanal de temperatura " + "="*10 + "\n")
        promedio = self.calcular_promedio()
        print(f"\nPromedio semanal: {promedio:.2f}°C")
# =================================================
# Arranque del Sistema de promedios de temperatura
# =================================================
if __name__ == "__main__":
    registro = RegistroClimaExtendido()

    # Mostrar temperaturas en consola
    registro.mostrar_temperaturas()

    # Mostrar el promedio
    registro.mostrar_resumen()
# ======================================================================================================================
# Programación Tradicional (sin uso de clases)
# Se trabaja con funciones y estructuras básicas
# Las temperaturas están predefinidas en el código
# ======================================================================================================================
print("\n" + "="*30 + " Con Programación Tradicional " + "="*30 + "\n")
# ======================================================================================================================

# ----------------------------------------------------------------------------------------------------------------------
#               Función que retorna las temperaturas predefinidas
# ----------------------------------------------------------------------------------------------------------------------
def obtener_temperaturas():
    """
    Retorna una lista de temperaturas predefinidas.
    """
    return [30, 24, 22, 21, 26, 28, 23]

# ----------------------------------------------------------------------------------------------------------------------
#               Función que retorna los días de la semana
# ----------------------------------------------------------------------------------------------------------------------
def obtener_dias():
    """
    Retorna la lista de días de la semana.
    """
    return ["Lunes", "Martes", "Miércoles", "Jueves",
            "Viernes", "Sábado", "Domingo"]

# ----------------------------------------------------------------------------------------------------------------------
#               Función para mostrar las temperaturas en consola
# ----------------------------------------------------------------------------------------------------------------------
def mostrar_temperaturas(dias, temperaturas):
    """
    Muestra las temperaturas asociadas a cada día.
    """
    for dia, temp in zip(dias, temperaturas):
        print(f"{dia}: {temp}°C")

# ----------------------------------------------------------------------------------------------------------------------
#               Función que calcula el promedio semanal
# ----------------------------------------------------------------------------------------------------------------------
def calcular_promedio(temperaturas):
    """
    Calcula el promedio de las temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)

# ----------------------------------------------------------------------------------------------------------------------
#               Función principal que organiza la ejecución del programa
# ----------------------------------------------------------------------------------------------------------------------
def main():
    # Obtener datos predefinidos
    dias = obtener_dias()
    temperaturas = obtener_temperaturas()

    # Mostrar temperaturas en consola
    mostrar_temperaturas(dias, temperaturas)
    print("\n" + "=" * 10 + " Promedio semanal de temperatura " + "=" * 10 + "\n")
    # Calcular y mostrar el promedio
    promedio = calcular_promedio(temperaturas)
    print(f"\nPromedio semanal: {promedio:.2f}°C")

# ----------------------------------------------------------------------------------------------------------------------
#               Ejecución del programa
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()