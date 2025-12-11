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