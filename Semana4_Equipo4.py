## Nombres de los integrantes del grupo:

# Integrante 1: Oscar Javier Portillo Tejada 
# Integrante 2: Cristopher David Salmeron Tejada
# Integrante 3: Diego Alexander Hernández Núñez
# Integrante 4: William Javier Chacon Calderon
# Integrante 5: Angel Josue Hernández Anzora 



## Ejercicios 

print("Bienvenido")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

persona1 = Persona("Juan", 30)
persona1.mostrar_datos()

print("---")

persona2 = Persona("María", 25)
persona2.mostrar_datos()

print("----------------------")

print("Bienvenido al sistema de rectángulos.")

class Rectángulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
base = float(input("\nIngrese la base del rectángulo: "))
altura = float(input("\nIngrese la altura del rectángulo: "))

rectangulo1 = Rectángulo(base, altura)

print(f"\nEl área del rectángulo es: {rectangulo1.calcular_area()}")
print(f"El perímetro del rectángulo es: {rectangulo1.calcular_perimetro()}")

print("----------------------")

print("Bienvenido al sistema de estudiantes.")

class Estudiante:
    def __init__(self, nombre, nota1, nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_promedio(self):
        return (self.nota1 + self.nota2) / 2

    def estado_aprobacion(self):
        promedio = self.calcular_promedio()
        if promedio >= 6:
            return "Aprobado"
        else:
            return "Reprobado"

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")
        print(f"Promedio: {self.calcular_promedio()}")
        print(f"Estado de aprobación: {self.estado_aprobacion()}")

estudiante1 = Estudiante("Pedro", 7, 8)
estudiante1.mostrar_datos()
print("---")
estudiante2 = Estudiante("Ana", 5, 6)
estudiante2.mostrar_datos()

print("---")

estudiante3 = input("\nIngrese el nombre del estudiante: ")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
estudiante3 = Estudiante(estudiante3, nota1, nota2)
estudiante3.mostrar_datos()

print("----------------------")

print("Bienvenido al sistema de cuenta bancaria.")

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado con éxito.")
        else:
            print("La cantidad a depositar debe ser mayor a 0.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor a 0.")
        elif cantidad > self.saldo:
            print("Fondos insuficientes. No se puede realizar el retiro.")
        else:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado con éxito.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo disponible: {self.saldo}")

titular = input("\nIngrese el nombre del titular: ")

cuenta = CuentaBancaria(titular, 1000)

print("------")

cuenta.mostrar_saldo()

monto_deposito = float(input("\n¿Cuánto desea depositar?: "))
cuenta.depositar(monto_deposito)

print("\nSaldo después del depósito:")
cuenta.mostrar_saldo()

monto_retiro = float(input("\n¿Cuánto desea retirar?: "))
cuenta.retirar(monto_retiro)

print("\nSaldo final.")
cuenta.mostrar_saldo()