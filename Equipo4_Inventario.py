## Nombres de los integrantes del grupo:

# Integrante 1: Oscar Javier Portillo Tejada 
# Integrante 2: Cristopher David Salmeron Tejada
# Integrante 3: Diego Alexander Hernández Núñez
# Integrante 4: William Javier Chacon Calderon
# Integrante 5: Angel Josue Hernández Anzora 


class Producto:

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad

    # método para mostrar información
    def mostrar_informacion(self):
        print(f"Nombre Producto: {self.nombre}\nPrecio Producto: {self.__precio}\nCantidad Producto: {self.__cantidad}\n")

    # método calcular valor inventario
    def calcular_valor_inventario(self):
        valor_inventario = self.__precio * self.__cantidad
        print(f"El valor del producto {self.nombre} en el inventario es de: {valor_inventario}")
        return valor_inventario

    # método aplicar descuento (recibe el porcentaje como parámetro)
    def aplicar_descuento(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            print("Porcentaje de descuento no válido. Debe estar entre 0 y 100.")
            return

        precio_anterior = self.__precio
        self.__precio = self.__precio - (self.__precio * (porcentaje / 100))

        print(f"--- Descuento aplicado a {self.nombre} ---")
        print(f"Precio anterior: {precio_anterior}")
        print(f"Porcentaje de descuento: {porcentaje}%")
        print(f"Precio nuevo: {self.__precio}\n")

    # método actualizar cantidad (aumentar, disminuir, asignar)
    def actualizar_cantidad(self, cantidad, operacion):
        if cantidad < 0:
            print("Error: la cantidad ingresada no puede ser negativa.")
            return

        if operacion == "aumentar":
            self.__cantidad += cantidad
            print(f"Se aumentaron {cantidad} unidades a {self.nombre}. Nueva cantidad: {self.__cantidad}")

        elif operacion == "disminuir":
            if cantidad > self.__cantidad:
                print(f"Error: no hay suficiente stock de {self.nombre} para disminuir {cantidad} unidades (stock actual: {self.__cantidad}).")
            else:
                self.__cantidad -= cantidad
                print(f"Se disminuyeron {cantidad} unidades de {self.nombre}. Nueva cantidad: {self.__cantidad}")

        elif operacion == "asignar":
            self.__cantidad = cantidad
            print(f"Se asignó una nueva cantidad a {self.nombre}. Nueva cantidad: {self.__cantidad}")

        else:
            print("Operación no válida. Usa 'aumentar', 'disminuir' o 'asignar'.")


# ==========================================================
# PRUEBAS DEL PROGRAMA
# ==========================================================

# 1. Crear tres productos
producto1 = Producto("Camiseta", 20.0, 100)
producto2 = Producto("Pantalón", 30.0, 80)
producto3 = Producto("Zapatos", 50.0, 100)

# 2. Mostrar información inicial
print("========== INFORMACIÓN INICIAL ==========")
producto1.mostrar_informacion()
producto2.mostrar_informacion()
producto3.mostrar_informacion()

# 3. Calcular valor total del inventario
print("========== VALOR DE INVENTARIO ==========")
producto1.calcular_valor_inventario()
producto2.calcular_valor_inventario()
producto3.calcular_valor_inventario()
print()

# 4. Actualizar cantidades: aumentar, disminuir, asignar
print("========== ACTUALIZACIÓN DE CANTIDADES ==========")
producto1.actualizar_cantidad(15, "aumentar")   # 100 -> 115
producto2.actualizar_cantidad(5, "disminuir")   # 80 -> 75
producto3.actualizar_cantidad(150, "asignar")    # 100 -> 150
print()

# Prueba extra: validaciones (operación inexistente, cantidad negativa, exceso al disminuir)
print("========== PRUEBAS DE VALIDACIÓN ==========")
producto1.actualizar_cantidad(10, "cambiar")     # operación inválida
producto2.actualizar_cantidad(-5, "aumentar")    # cantidad negativa
producto3.actualizar_cantidad(160, "disminuir") # excede el stock
print()

# 5. Aplicar descuento a un producto
print("========== APLICACIÓN DE DESCUENTO ==========")
producto1.aplicar_descuento(10)  # 10% de descuento
print()

# 6. Mostrar información final para comprobar los cambios
print("========== INFORMACIÓN FINAL ==========")
producto1.mostrar_informacion()
producto2.mostrar_informacion()
producto3.mostrar_informacion()