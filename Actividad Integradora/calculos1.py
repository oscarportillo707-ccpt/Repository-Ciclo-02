# calculos.py

def calcular_total(lista_productos):
    return sum(p.calcular_subtotal() for p in lista_productos)

def aplicar_descuento(total, porcentaje):
    descuento = total * (porcentaje / 100)
    return total - descuento
