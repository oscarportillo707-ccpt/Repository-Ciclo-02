## EJERCICIO 1 - CLASIFICACIÓN DE TRIANGULOS

def clasificar_triangulo(lado1, lado2, lado3):
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        return "Los lados deben ser mayores que cero."

    if (lado1 + lado2 <= lado3) or (lado1 + lado3 <= lado2) or (lado2 + lado3 <= lado1):
        return "Estos lados no forman un triángulo válido."
    
    if lado1 == lado2 == lado3:
        return "El triángulo es equilátero."
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "El triángulo es isósceles."
    else:
        return "El triángulo es escaleno."

try:

    lado1 = float(input("Ingrese el primer lado del triángulo: "))
    lado2 = float(input("Ingrese el segundo lado del triángulo: "))
    lado3 = float(input("Ingrese el tercer lado del triángulo: "))

    resultado = clasificar_triangulo(lado1, lado2, lado3)
    print(resultado)

except ValueError:
    print("Por favor, ingrese valores numéricos válidos para los lados del triángulo.")



## EJERCICIO 2 - VERIFICACIÓN DE CONTRASEÑA

CONTRASEÑA_CORRECTA = "secreto123"

contraseña = input("Ingrese la contraseña: ")

if contraseña == CONTRASEÑA_CORRECTA:
    print("Acceso permitido")
else:
    print("Acceso denegado")



## EJERCICIO 3 - CÁLCULO DE DESCUENTO ADICIONAL

try:
    precio = float(input("Ingrese el precio del artículo: "))
    descuento = float(input("Ingrese el porcentaje de descuento: "))

    porcentaje_total = descuento

    print(f"\nDescuento ingresado: {descuento}%")

    # Se usa un operador lógico (and) para verificar ambas condiciones
    if precio >= 1000 and descuento >= 10:
        porcentaje_total += 5
        print("Descuento adicional aplicado: 5%")

    precio_final = precio * (1 - porcentaje_total / 100)

    print(f"Precio final: ${precio_final:.2f}")

except ValueError:
    print("Error: debe ingresar valores numéricos.")



## EJERCICIO 4 - COMPARACIÓN DE NÚMEROS

try:
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    print()
    if numero1 > numero2:
        print(f"El número {numero1} es mayor que {numero2}.")
    elif numero2 > numero1:
        print(f"El número {numero2} es mayor que {numero1}.")
    else:
        print(f"Los números son iguales: {numero1} = {numero2}.")

except ValueError:
    print("Error: debe ingresar números enteros.")
