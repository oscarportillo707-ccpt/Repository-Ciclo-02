import math as m

# clase padre
class FiguraGeometrica:
    # metodo para calcular el area
    def calcular_area(self):
        pass

# crear nuestras clases hijas (aplicando herencia)
class Cuadrado(FiguraGeometrica):

    def __init__(self, lado):
        self.lado = lado

    # aplicar el polimorfismo
    def calcular_area(self):
            area = self.lado * self.lado
            print(f"El area del cuadrado es: {area}")

class Triangulo(FiguraGeometrica):

     def __init__(self, base, altura):
          self.base = base
          self.altura = altura

     # aplicar el polimorfismo
     def calcular_area(self):
            area = (self.base * self.altura)/2
            print(f"El area del triangulo es: {area}")

class Circulo(FiguraGeometrica):

     def __init__(self, radio):
        self.radio = radio

    # aplicar el polimorfismo
     def calcular_area(self):
            area = m.pi * m.pow(self.radio, 2)
            print(f"El area del circulo es: {area}")


# crear un objeto que hereda de una clase padre
cuadrado_1 = Cuadrado(2)
cuadrado_1.calcular_area()

triangulo_1 = Triangulo(2,3)
triangulo_1.calcular_area()

circulo_1 = Circulo(3)
circulo_1.calcular_area()