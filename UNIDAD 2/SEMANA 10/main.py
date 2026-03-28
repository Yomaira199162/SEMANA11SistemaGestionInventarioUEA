import os


class Producto:
    def __init__(self, id_prod, nombre, cantidad, precio):
        self.id_prod = id_prod
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id_prod},{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        """Guarda todos los productos en el archivo de texto."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(str(p) + "\n")
            return True
        except PermissionError:
            print("❌ Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"❌ Error inesperado al guardar: {e}")
        return False

    def cargar_desde_archivo(self):
        """Carga los productos al iniciar el programa."""
        if not os.path.exists(self.archivo):
            # Si no existe, lo creamos vacío
            try:
                open(self.archivo, "w").close()
                print(f"ℹ️ Archivo '{self.archivo}' creado exitosamente.")
            except Exception as e:
                print(f"❌ No se pudo crear el archivo: {e}")
            return

        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    datos = linea.strip().split(',')
                    if len(datos) == 4:
                        id_p, nom, cant, prec = datos
                        self.productos.append(Producto(id_p, nom, int(cant), float(prec)))
            print(f"✅ Inventario cargado: {len(self.productos)} productos encontrados.")
        except FileNotFoundError:
            print("⚠️ Archivo no encontrado durante la carga.")
        except ValueError:
            print("⚠️ Error: El archivo contiene datos corruptos o con formato incorrecto.")
        except Exception as e:
            print(f"❌ Error crítico al cargar: {e}")

    def agregar_producto(self, producto):
        # Evitar IDs duplicados
        if any(p.id_prod == producto.id_prod for p in self.productos):
            print("❌ Error: Ya existe un producto con ese ID.")
            return

        self.productos.append(producto)
        if self.guardar_en_archivo():
            print(f"✨ Producto '{producto.nombre}' añadido y guardado con éxito.")

    def actualizar_producto(self, id_prod, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.id_prod == id_prod:
                if nueva_cantidad is not None: p.cantidad = nueva_cantidad
                if nuevo_precio is not None: p.precio = nuevo_precio
                if self.guardar_en_archivo():
                    print(f"✅ Producto ID {id_prod} actualizado en el archivo.")
                return
        print("❌ Error: Producto no encontrado.")

    def eliminar_producto(self, id_prod):
        original_count = len(self.productos)
        self.productos = [p for p in self.productos if p.id_prod != id_prod]

        if len(self.productos) < original_count:
            if self.guardar_en_archivo():
                print(f"🗑️ Producto ID {id_prod} eliminado permanentemente.")
        else:
            print("❌ Error: No se encontró el ID.")


# --- Interfaz de Usuario ---
def menu():
    inv = Inventario()
    while True:
        print("\n--- 📦 SISTEMA DE GESTIÓN DE INVENTARIOS PRO ---")
        print("1. Agregar Producto")
        print("2. Mostrar Inventario")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_p = input("ID: ")
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                prec = float(input("Precio: "))
                inv.agregar_producto(Producto(id_p, nom, cant, prec))
            except ValueError:
                print("❌ Error: Cantidad y Precio deben ser números.")

        elif opcion == "2":
            print("\nID | Nombre | Cantidad | Precio")
            print("-" * 30)
            for p in inv.productos:
                print(f"{p.id_prod} | {p.nombre} | {p.cantidad} | ${p.precio:.2f}")

        elif opcion == "3":
            id_p = input("ID del producto a actualizar: ")
            try:
                cant = input("Nueva cantidad (dejar vacío para no cambiar): ")
                prec = input("Nuevo precio (dejar vacío para no cambiar): ")
                inv.actualizar_producto(
                    id_p,
                    int(cant) if cant else None,
                    float(prec) if prec else None
                )
            except ValueError:
                print("❌ Error: Ingrese valores numéricos válidos.")

        elif opcion == "4":
            id_p = input("ID del producto a eliminar: ")
            inv.eliminar_producto(id_p)

        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")


if __name__ == "__main__":
    menu()
