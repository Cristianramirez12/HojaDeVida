class Factura:
    def __init__(self):
        self.__fecha = []
        self.__total = []
        @property
        def fecha(self):
            return self.__fecha

        @fecha.setter
        def fecha(self, fecha):
            self.__fecha =fecha

        @property
        def total(self):
            return self.__total

        @total.setter
        def total(self, total):
            self.__total = total