class Antibiotico:
    def __init__(self):
        self.__nombre = []
        self.__dosis = []
        self.__tipo = []
        self.__precio = 0
        @property
        def nombre(self):
            return self.__nombre
        @nombre.setter
        def nombre(self, nombre):
            self.__nombre = nombre
        @property
        def dosis(self):
            return self.__dosis
        @dosis.setter
        def dosis(self, dosis):
            self.__dosis = dosis
        @property
        def tipo(self):
            return self.__tipo
        @tipo.setter
        def tipo(self, tipo):
            self.__tipo = tipo
        @property
        def precio(self):
            return self.__precio
        @precio.setter
        def precio(self, precio):
            self.__precio = precio