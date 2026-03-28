from PRODUCTO import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        # Validación de ID ÚNICO (Requisito indispensable)
        if any(p.id == producto.id for p in self.productos):
            print("❌ Error: Ya existe un producto con ese ID.")
            return
        self.productos.append(producto)
        print("✅ Producto registrado con éxito.")

    def eliminar_producto(self, id_p: str):
        self.productos = [p for p in self.productos if p.id != id_p]
        print("🗑️ Proceso de eliminación completado.")

    def actualizar_producto(self, id_p: str, n_cant=None, n_prec=None):
        for p in self.productos:
            if p.id == id_p:
                if n_cant is not None: p.cantidad = n_cant
                if n_prec is not None: p.precio = n_prec
                print("🔄 Producto actualizado.")
                return
        print("❌ ID no encontrado.")

    def buscar_por_nombre(self, nombre: str):
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]

    def mostrar_todo(self):
        if not self.productos:
            print("📭 Inventario vacío.")
        else:
            print("\n" + "="*50)
            for p in self.productos: print(p)
            print("="*50)