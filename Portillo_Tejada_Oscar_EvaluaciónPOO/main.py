from producto import Producto
from utilidades import (
    calcular_total_inventario,
    buscar_producto,
    producto_mayor_valor,
)


def linea_separadora():
    print("-" * 40)


def main():
    producto1 = Producto("P001", "Teclado mecánico", 25.50, 10)
    producto2 = Producto("P002", "Mouse inalámbrico", 15.00, 20)
    producto3 = Producto("P003", "Monitor 24 pulgadas", 120.00, 5)
    producto4 = Producto("P004", "Audífonos Bluetooth", 35.75, 8)

    inventario = [producto1, producto2, producto3, producto4]

    print("=== INVENTARIO DE PRODUCTOS ===")
    for producto in inventario:
        linea_separadora()
        producto.mostrar_informacion()
        print(f"Subtotal: ${producto.calcular_subtotal():.2f}")

    linea_separadora()

    total = calcular_total_inventario(inventario)
    print(f"\nValor total del inventario: ${total:.2f}")

    codigo_buscado = "P003"
    linea_separadora()
    print(f"Buscando producto con código '{codigo_buscado}'...")
    encontrado = buscar_producto(inventario, codigo_buscado)
    if encontrado:
        print("Producto encontrado:")
        encontrado.mostrar_informacion()
    else:
        print("Producto no encontrado.")

    linea_separadora()

    print("Actualizando cantidad del producto 'P001'...")
    producto1.actualizar_cantidad(15)
    print(f"Nuevo subtotal de '{producto1.nombre}': ${producto1.calcular_subtotal():.2f}")

    linea_separadora()
    
    mejor_producto = producto_mayor_valor(inventario)
    print("Producto con mayor valor de inventario:")
    mejor_producto.mostrar_informacion()
    print(f"Valor total de este producto: ${mejor_producto.calcular_subtotal():.2f}")


if __name__ == "__main__":
    main()