"""Heredar de la clase Auto una clase Marca, que agregue el atributo Modelo. 
Instanciar en  el programa principal (una sola línea en total). La salida debe ser por ejemplo: Auto: VW Modelo: Gol"""


class Auto():
    def __init__ (self, color, marca):
        self.color = color
        self.marca = marca

class Marca(Auto):
    def __init__ (self, modelo):
        self.modelo = modelo
        return "Auto: " + str (self.marca) + "Modelo: " + str (self.modelo)



unAuto = Auto("Rojo", "Ford")
print(unAuto)