def calcular_subtotal_general(productos):
    subtotal_general = 0
    for producto in productos:
        subtotal_general += producto.calcular_subtotal()
    return subtotal_general

def calcular_descuento(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)

def calcular_total_final(subtotal, descuento):
    return subtotal - descuento