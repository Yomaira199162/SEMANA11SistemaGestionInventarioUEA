import time


class ExperimentoQuimico:
    """
    Clase que representa un experimento en un laboratorio.
    Demuestra la inicialización de recursos (init) y su liberación (del).
    """

    def __init__(self, nombre_sustancia, temperatura_inicial):
        """
        CONSTRUCTOR: Se activa al crear el objeto.
        Prepara el entorno del experimento.
        """
        self.nombre_sustancia = nombre_sustancia
        self.temperatura = temperatura_inicial
        self.contenedor_abierto = True

        print(f"\n>>> [CONSTRUCTOR]: Iniciando experimento con '{self.nombre_sustancia}'.")
        print(f">>> [ESTADO]: Contenedor abierto. Temperatura inicial: {self.temperatura}°C.")

    def calentar(self, grados):
        """Método para interactuar con el objeto."""
        if self.contenedor_abierto:
            self.temperatura += grados
            print(f"[ACCIÓN]: Calentando... Nueva temperatura: {self.temperatura}°C.")
        else:
            print("[ERROR]: No se puede calentar, el contenedor está sellado.")

    def registrar_datos(self):
        """Simula el guardado de información antes de destruir el objeto."""
        print(f"[DATOS]: Registrando valores finales de '{self.nombre_sustancia}' en la bitácora...")

    def __del__(self):
        """
        DESTRUCTOR: Se activa al finalizar el programa o usar 'del'.
        Es CRÍTICO para la seguridad: cierra el contenedor y limpia los residuos.
        """
        self.registrar_datos()  # Guardamos todo antes de borrar
        self.contenedor_abierto = False
        print(f"<<< [DESTRUCTOR]: Sellando contenedor de '{self.nombre_sustancia}'.")
        print(f"<<< [LIMPIEZA]: Liberando espacio en el mesón del laboratorio y eliminando residuos.")
        print("-" * 60)


# --- Bloque de ejecución principal ---
if __name__ == "__main__":
    print("=== SISTEMA DE GESTIÓN DE LABORATORIO INICIADO ===")

    # 1. Creamos el primer experimento (Llamada al Constructor)
    exp1 = ExperimentoQuimico("Nitrógeno Líquido", -196)
    exp1.calentar(50)

    # 2. Creamos un segundo experimento
    exp2 = ExperimentoQuimico("Ácido Sulfúrico", 25)
    exp2.calentar(15)

    # 3. Demostración de eliminación manual (Llamada al Destructor antes de tiempo)
    print("\n--- Terminando experimento 1 manualmente ---")
    del exp1

    print("\n[AVISO]: El experimento 2 sigue activo mientras el programa corre.")
    time.sleep(1)  # Pausa de 1 segundo para observar la consola

    print("\n=== CERRANDO SISTEMA CENTRAL ===")
    # Al terminar el programa, el recolector de basura llama automáticamente
    # al destructor de 'exp2'.