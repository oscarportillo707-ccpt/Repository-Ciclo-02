def calcular_total_inventario(productos):

    total = 0

    for producto in productos:
        total += producto.calcular_subtotal()
    return total


def buscar_producto(productos, codigo):
   
    for producto in productos:
        if producto.codigo == codigo:
            return producto
    return None


def producto_mayor_valor(productos):
   
    if not productos:
        return None

    mayor = productos[0]
    for producto in productos[1:]:
        if producto.calcular_subtotal() > mayor.calcular_subtotal():
            mayor = producto
    return mayor