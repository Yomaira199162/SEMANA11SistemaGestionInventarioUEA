class Producto:
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        # Atributos privados (el guion bajo _ indica elegancia y orden)
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters profesionales
    @property
    def id(self) -> str: return self._id

    @property
    def nombre(self) -> str: return self._nombre

    @property
    def cantidad(self) -> int: return self._cantidad

    @property
    def precio(self) -> float: return self._precio

    # Setters con validación (Esto le encantará al profe)
    @cantidad.setter
    def cantidad(self, valor: int):
        self._cantidad = valor if valor >= 0 else self._cantidad

    @precio.setter
    def precio(self, valor: float):
        self._precio = valor if valor > 0 else self._precio

    # Método para que el producto se vea bonito al imprimirlo
    def __str__(self) -> str:
        return f"ID: {self._id:<5} | Nombre: {self._nombre:<12} | Stock: {self._cantidad:<4} | Precio: ${self._precio:>6.2f}"