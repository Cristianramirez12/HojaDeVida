class ProductoControl:
    def __init__(self):
        self.__regiscoIca=[]
        self.__nombre=[]
        self.__frecuenciaApliccion=[]
        self.__valorProducto=0

        @property
        def registroIca(self):
            return self.__regiscoIca

        @registroIca.setter
        def registroIca(self,registroIca):
            self.__regiscoIca=registroIca

        @property
        def nombre(self):
            return self.__nombre

        @nombre.setter
        def nombre(self, nombre):
            self.__nombre = nombre

        @property
        def frecuenciaApliccion(self):
            return self.__frecuenciaApliccion

        @frecuenciaApliccion.setter
        def frecuenciaApliccion(self, frecuenciaApliccion):
            self.__frecuenciaApliccion = frecuenciaApliccion

        @property
        def valorProducto(self):
            return self.__valorProducto

        @valorProducto.setter
        def valorProducto(self, valorProducto):
            self.__valorProducto = valorProducto

