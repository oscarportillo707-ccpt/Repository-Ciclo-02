class Producto: 
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.precio * self.cantidad

    def mostrar(self):
        print("-----------------")
        print(f"Nombre: {self.nombre}\nPrecio: {self.precio}\nCantidad: {self.cantidad}")

