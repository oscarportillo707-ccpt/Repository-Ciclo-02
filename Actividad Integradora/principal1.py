# principal.py
from producto import Producto
from calculos import calcular_total, aplicar_descuento

# Registrar productos
p1 = Producto("Manzana", 0.5, 10)
p2 = Producto("Pan", 1.2, 5)
p3 = Producto("Leche", 0.9, 3)

productos = [p1, p2, p3]

# Mostrar subtotales
print("--- Detalle de productos ---")
for p in productos:
    p.mostrar()

# Calcular total y aplicar descuento
total = calcular_total(productos)
descuento_porcentaje = 10  # ejemplo: 10%
total_con_descuento = aplicar_descuento(total, descuento_porcentaje)

print(f"\nTotal sin descuento: ${total:.2f}")
print(f"Descuento aplicado: {descuento_porcentaje}%")
print(f"Total a pagar: ${total_con_descuento:.2f}")