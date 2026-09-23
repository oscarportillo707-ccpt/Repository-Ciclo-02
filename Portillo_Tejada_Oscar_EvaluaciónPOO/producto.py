class Producto:

    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio unitario: ${self.precio:.2f}")
        print(f"Cantidad disponible: {self.cantidad}")

    def calcular_subtotal(self):
        return self.precio * self.cantidad

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad
        print(f"Cantidad de '{self.nombre}' actualizada a {self.cantidad} unidades.")