# Crear una clase llamada Producto.

class Producto:

    DESCUENTO = 0.10

    # agregar los atributos: nombre, precio, cantidad
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad

    # método para mostrar información
    def mostrar_informacion(self):
        print(f"Nombre Producto: {self.nombre}\nPrecio Producto: {self.__precio}\nCantidad Producto: {self.__cantidad}")

    # método calcular valor inventario
    def calcular_valor_inventario(self):
        valor_inventario = self.__precio * self.__cantidad
        print(f"El valor del producto {self.nombre} en el inventario es de: {valor_inventario}")

    # método aplicar descuento
    def aplicar_descuento(self):
        resultado = self.__precio * self.DESCUENTO
        print(f"El descuento para el producto {self.nombre} es de: {resultado}") 

    # método actualizar cantidad
    def actualizar_cantidad(self, cantidad, operacion="agregar"):
        if operacion == "agregar":
            self.__cantidad += cantidad
            print(f"Se agregaron {cantidad} unidades a {self.nombre}. Nueva cantidad: {self.__cantidad}")
        elif operacion == "quitar":
            if cantidad > self.__cantidad:
                print(f"No hay suficiente stock de {self.nombre} para quitar {cantidad} unidades.")
            else:
                self.__cantidad -= cantidad
                print(f"Se quitaron {cantidad} unidades de {self.nombre}. Nueva cantidad: {self.__cantidad}")
        else:
            print("Operación no válida. Usa 'agregar' o 'quitar'.")


# 1. Crear tres productos diferentes
producto1 = Producto("Camiseta", 20.0, 100)
producto2 = Producto("Pantalón", 30.0, 80)
producto3 = Producto("Zapatos", 50.0, 100)

# 2. Mostrar la información de cada producto
producto1.mostrar_informacion()
producto2.mostrar_informacion()
producto3.mostrar_informacion()

# 3. Calcular el valor total del inventario de cada producto
producto1.calcular_valor_inventario()
producto2.calcular_valor_inventario()
producto3.calcular_valor_inventario()

# 4. Aplicar descuento a un producto
descuento1 = producto1.aplicar_descuento()

# 5. Crear un método adicional llamado actualizar_cantidad
producto1.actualizar_cantidad(15, "agregar")
producto2.actualizar_cantidad(5, "quitar")
producto3.actualizar_cantidad(20, "quitar")