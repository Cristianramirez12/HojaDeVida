from model import Antibiotico
from model import ProductoFertilizante
from model import ProductoPlaga

def display_menu():
    print("____________________________________________")
    print("\t CENTRO DE FACTURACION AGROYA")
    print("____________________________________________")
    nombre=input("Ingrese nombre: ")
    cedula=input("Ingrese cedula: ")
    fecha = input("Ingrese fecha: ")
    return [nombre,cedula,fecha]

def display_usuario(cliente):
    print("el nombre del cliente es ", cliente.nombre)
    print("La cedula del usuario es ", cliente.cedula)

def display_antibiotico():
    compra = Antibiotico.Antibiotico()
    compra.nombre = input("Ingrese nombre del antibiotico: ")
    compra.dosis = input("Ingrese dosis a aplicar: ")
    compra.tipo = input("Ingrese tipo de animal: ")
    compra.precio = input("Ingrese precio del antibiotico: ")
    print("Antibiotico registrado")
    return compra

def display_compra():
    print("")
    print("________________________________________")
    print("\t Variedades Disponibles")
    print("________________________________________")
    print("1 Compra de antibiotico ")
    print("2 Compra de producto ")
    print("3 Finalizar compra ")
    option=input("Opcion:")
    return option

def display_tipoProducto():
    print("_____________________________________________")
    print("Tipos De Productos ")
    print("_____________________________________________")
    print("1 Fertilizante")
    print("2 Plaguisidas ")
    print("3 Atras ")
    option = input("Opcion:")
    return option

def display_fertilizante():
    print("")
    compra = ProductoFertilizante.ProductoFertilizante()
    compra.regiscoIca = input("Ingrese registro ica del producto: ")
    compra.nombre = input("Ingrese nombre del producto: ")
    compra.frecuenciaApliccion = input("Ingrese frecuencia de aplicacion: ")
    compra.valorProducto = input("Ingrese precio del producto: ")
    compra.aplicacion = input("Fecha de ultima aplicacio: ")
    print("Fertilizante registrado")
    return compra

def display_plaguicida():
    print("")
    compra = ProductoPlaga.ProductoPlaga()
    compra.regiscoIca = input("Ingrese registro ica del producto: ")
    compra.nombre = input("Ingrese nombre del producto: ")
    compra.frecuenciaApliccion = input("Ingrese frecuencia de aplicacion: ")
    compra.valorProducto = input("Ingrese precio del producto: ")
    compra.carencia = input("Fecha de carencia: ")
    print("plaguisida registrado")
    return compra

def Tipofactura():
    print("_____________________________________________")
    print("Tipos De Factura ")
    print("_____________________________________________")
    print("1 Sencilla")
    print("2 Completa")
    print("3 Atras ")
    option = input("Opcion:")
    return option


def imprimirFactura(antibioticos,productos,cliente):
    print("")
    total=0
    print("_____________________________________________")
    print("\t\t\t FACTURA AGROYA       ", cliente.fecha)
    print("{0:30s} {1:8s}".format("Producto", "Precio"))
    print("-------------              ------------------")
    for index in antibioticos:
        print("{0:30s} {1:20s}".format((index.nombre), (index.precio)))
        total += int(index.precio)
    for index in productos:
        print("{0:30s} {1:20s}".format((index.nombre), (index.valorProducto)))
        total += int(index.valorProducto)
    print("---------------------------------------------")
    print("Valor a pagar $", total)
    print("")
    print("Cliente: ", cliente.nombre)
    print("Registro: ", cliente.cedula)
    cliente.total=total;

def imprimirFacturaCompleta(antibioticos,productos,cliente):
    print("")
    total=0
    print("__________________________________________________________________")
    print("\t\t\t\t\t\t FACTURA AGROYA       ", cliente.fecha)
    print("--------------------------ANTIBIOTICOS----------------------------")
    print("{0:20s} {1:8s} {2:20s} {3:8s}".format("Producto","Dosis","Tipo", "Precio"))
    for index in antibioticos:
        print("{0:20s} {1:8s}".format((index.nombre), (index.dosis)),end="")
        print("{0:20s} {1:8s}".format((index.tipo), (index.precio)))
        total += int(index.precio)
    print("---------------------------PRODUCTOS-------------------------------")
    print("{0:20s} {1:18s} {2:21s} {3:8s}".format("RegistroIca", "Nombre", "FrecuenciaAplicacion", "Precio"))
    for index in productos:
        print("{0:20s} {1:20s}".format((index.regiscoIca), (index.nombre)),end="")
        print("{0:22s} {1:8s}".format((index.frecuenciaApliccion), (index.valorProducto)))
        total += int(index.valorProducto)
    print("---------------------------------------------")
    print("Valor a pagar $", total)
    print("")
    print("Cliente: ", cliente.nombre)
    print("Registro: ", cliente.cedula)
    cliente.total=total

