class Figura:
    def area(self):
        pass  # Cada figura definirá su propia forma de calcular el área


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2


# Uso
figuras = [Rectangulo(4, 5), Circulo(3)]

print("Áreas de las figuras:")
for figura in figuras:
    print(f"{figura.__class__.__name__}: {figura.area()}")  # Llamada al método area() de cada figura