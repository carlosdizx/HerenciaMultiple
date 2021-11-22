from Color import Color
from FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'Cuadrado[{FiguraGeometrica.__str__(self)}, Area: {self.calcular_area()}, {Color.__str__(self)}]'
