from model.ProductoControl import ProductoControl as pc
class ProductoFertilizante(pc):
    def __init__(self):
        self.__aplicacion = []
        super().__init__()

        @property
        def aplicacion(self):
            return self.__apliacacion
        @aplicacion.setter
        def aplicacion(self,llega):
            self.__aplicacio=llega

