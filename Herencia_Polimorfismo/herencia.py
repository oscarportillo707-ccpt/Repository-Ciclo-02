class Vehiculo:
    def __init__(self, marca, velocidad_max):
        self.marca = marca
        self.velocidad_max = velocidad_max

    def info(self):
        return f"{self.marca} - Velocidad máxima: {self.velocidad_max} km/h"


class Coche(Vehiculo):  # Coche hereda de Vehiculo
    def __init__(self, marca, velocidad_max, num_puertas):
        super().__init__(marca, velocidad_max)  # Reutiliza el constructor del padre
        self.num_puertas = num_puertas


# Uso
mi_coche = Coche("Toyota", 180, 4)
print(mi_coche.info())         # Método heredado, no hubo que reescribirlo
print(mi_coche.num_puertas)    # Atributo propio de Coche