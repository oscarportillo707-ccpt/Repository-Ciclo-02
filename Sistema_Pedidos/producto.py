class Producto:  
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.precio * self.cantidad

    def mostrar(self):
        print(
            f"Nombre: {self.nombre}\nPrecio: ${self.precio:.2f}\nCantidad: {self.cantidad}\nSubtotal: ${self.calcular_subtotal():.2f}"
        )
       


    