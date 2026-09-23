## Nombres de los integrantes del grupo:

# Integrante 1: Oscar Javier Portillo Tejada 
# Integrante 2: Cristopher David Salmeron Tejada
# Integrante 3: Diego Alexander Hernández Núñez
# Integrante 4: William Javier Chacon Calderon
# Integrante 5: Angel Josue Hernández Anzora 



from producto import Producto
from calculos import calcular_subtotal_general, calcular_descuento, calcular_total_final

def ejecutar():
    productos = []

    while True:
        try:
            cantidad_productos = int(input("¿Cuántos productos deseas registrar?: "))
            break
        except ValueError:
            print("Cantidad inválida, vuelve a intentarlo.")

    for i in range(cantidad_productos):
        print(f"\n--- Producto {i + 1} ---")
        nombre = input("Nombre del producto: ")

        while True:
            try:
                precio = float(input("Precio unitario: $"))
                break
            except ValueError:
                print("Precio inválido, ingresa un número (ejemplo: 4.50)")

        while True:
            try:
                cantidad = int(input("Cantidad: "))
                break
            except ValueError:
                print("Cantidad inválida, ingresa un número entero.")

        nuevo_producto = Producto(nombre, precio, cantidad)
        productos.append(nuevo_producto)

    print("\n========== SISTEMA DE PEDIDOS ==========\n")
    for i, producto in enumerate(productos, start=1):
        print(f"Producto {i}")
        producto.mostrar()
        print("----------------------------------------")

    subtotal_general = calcular_subtotal_general(productos)
    print(f"\nSubtotal general: $ {subtotal_general:.2f}\n")

    while True:
        try:
            porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
            break
        except ValueError:
            print("Porcentaje inválido, ingresa un número (ejemplo: 15)")

    monto_descuento = calcular_descuento(subtotal_general, porcentaje_descuento)
    total_a_pagar = calcular_total_final(subtotal_general, monto_descuento)

    print("\n========== RESUMEN FINAL ==========")
    print(f"Subtotal: $ {subtotal_general:.2f}")
    print(f"Descuento: {porcentaje_descuento:.1f} %")
    print(f"Descuento aplicado: $ {monto_descuento:.2f}")
    print(f"Total a pagar: $ {total_a_pagar:.2f}")

if __name__ == "__main__":
    ejecutar()


#¿Qué ventaja encontraron al separar la clase Producto, 
# las funciones de cálculo y el programa principal en diferentes archivos?

# La principal ventaja de dividir el programa en producto.py, calculos.py y principal.py o modulos es que, 
# se logra un código mucho más ordenado, fácil de entender y de mantener. 
# Al darle un "trabajo" específico a cada archivo uno para manejar los datos del producto,
# otro para hacer la matemática y otro para ejecutar el programa evitas el desorden de tener todo amontonado. 
# Esto te permite solucionar fallas de forma más rápida sin arruinar otras partes del código, 
# además de hacer posible reutilizar esas funciones de cálculo en futuros proyectos sin tener que escribir todo desde cero.