class FiguraGeometrica:
    def __init__(self, ancho, alto):
        if ancho > 0 and alto > 0:
            self._ancho = ancho
            self._alto = alto
        else:
            self._ancho = 0
            self._alto = 0

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    def __str__(self):
        return f'FiguraGeometrica[Alto:{self._alto}, Ancho:{self._ancho}]'
