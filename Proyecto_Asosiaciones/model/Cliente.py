from model.Factura import Factura
class Cliente(Factura):
    def __init__(self):
        super().__init__()
        self.__facturas=[]
        self.__nombre=[]
        self.__cedula=[]

        @property
        def nombre(self):
            return self.__nombre

        @nombre.setter
        def nombre(self, nombre):
            self.__nombre = nombre

        @property
        def cedula(self):
            return self.__cedula

        @cedula.setter
        def cedula(self, cedula):
            self.__cedula = cedula

        @property
        def Asociar(self):
            return (self.__facturas)

