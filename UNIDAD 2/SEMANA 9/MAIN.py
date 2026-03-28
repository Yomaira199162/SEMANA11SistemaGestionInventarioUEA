from PRODUCTO import Producto
from INVENTARIO import Inventario


def ejecutar_sistema():
    mi_inventario = Inventario()

    while True:
        print("\n--- 🛒 GESTIÓN DE INVENTARIO (SEMANA 9) ---")
        print("1. Añadir | 2. Eliminar | 3. Actualizar | 4. Buscar | 5. Mostrar | 6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_p = input("ID (Ej: A01): ")
                nom = input("Nombre: ")
                can = int(input("Cantidad: "))
                pre = float(input("Precio: "))
                mi_inventario.agregar_producto(Producto(id_p, nom, can, pre))
            except ValueError:
                print("⚠️ Error: Cantidad y Precio deben ser números.")

        elif opcion == "2":
            mi_inventario.eliminar_producto(input("ID a borrar: "))

        elif opcion == "3":
            id_p = input("ID: ")
            c = input("Nueva Cantidad (vacío para omitir): ")
            p = input("Nuevo Precio (vacío para omitir): ")
            mi_inventario.actualizar_producto(id_p, int(c) if c else None, float(p) if p else None)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = mi_inventario.buscar_por_nombre(nombre)
            for r in resultados: print(r)

        elif opcion == "5":
            mi_inventario.mostrar_todo()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break


if __name__ == "__main__":
    ejecutar_sistema()