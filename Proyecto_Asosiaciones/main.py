#Victor Manuel - Cristian Orlando
from ui import Interface
from model import Cliente
antibioticos=[]
productos=[]
clientes=[]
option=0

cliente=Cliente.Cliente()
a=Interface.display_menu()
cliente.nombre=a[0]
cliente.cedula=a[1]
cliente.fecha=a[2]

while(option!="3"):
    option = Interface.display_compra()
    if (option=="1"):
        antibiotico=Interface.display_antibiotico()
        antibioticos.append(antibiotico)

    if (option=="2"):
        tipoproducto=Interface.display_tipoProducto()

        if(tipoproducto=="1"):
            producto=Interface.display_fertilizante()
            productos.append(producto)

        elif (tipoproducto == "2"):
            producto=Interface.display_plaguicida()
            productos.append(producto)

    if (option=="3"):
        tipofactura=Interface.Tipofactura()
        if ( tipofactura=="1"):
            Interface.imprimirFactura(antibioticos, productos, cliente)
        if (tipofactura == "2"):
            Interface.imprimirFacturaCompleta(antibioticos, productos, cliente)
clientes.append(cliente)
