from model.ProductoControl import ProductoControl as pc
class ProductoPlaga(pc):
    def __init__(self):
        self.__carencia = []
        super().__init__()

        @property
        def carencia(self):
            return self.__carencia

        @carencia.setter
        def carencia(self, llega):
            self.__carencia = llega