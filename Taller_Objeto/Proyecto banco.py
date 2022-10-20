# Cristian Orlando Ramirez
# 1088539121
class Cuenta:
    def __init__(self,cuenta,cedula,propietario,saldo):
        self.cuenta= cuenta 
        self.propietario=propietario
        self.cedula=cedula
        self.saldo=saldo
        
    #Metodos modificadores
    def consignar(self,ingreso):
        self.saldo=self.saldo+ingreso

    def retirar(self,cantidad):
        if ((self.saldo-cantidad)>0):
            self.saldo=self.saldo-cantidad
            
    #Metodos Accesores
    def cuenta(self):
        return self.cuenta
    
    def propietario(self):
        return self.propietario
    
    def cedula(self):
        return self.cedula
    
    def saldo(self):
        return self.saldo

    def mostrar_Cuenta(self):
        print("Cuenta ",(self.cuenta))
        print("Propietario ",self.propietario)
        print("cedula ",self.cedula)
        print("Saldo ",self.saldo)
        print("")

def save_cuenta_list(cuenta,donde_Guardar):
    donde_Guardar.append(e)
    return cuentas

# Guardar_cuentas y brir_cuentas manejo de archivo
def Guardar_cuentas(cuentas):
    cadena=""
    for index in cuentas:
        cadena = (cadena + str(index.cuenta)+ " ")
        cadena =(cadena + str(index.propietario)+ " ")
        cadena =(cadena+ str(index.cedula)+ " ")
        cadena =(cadena + str(index.saldo)+ "\n")
    archi1=open("Cuentas.txt","w") 
    archi1.write(cadena)   
    archi1.close()
    
def abrir_cuentas(cuentas):
    archivo=open("Cuentas.txt")
    cuentas_load=(archivo.readlines())
    archivo.close()
    for texto in cuentas_load:
        texto=texto.split(" ")
        e=Cuenta(texto[0],texto[1],texto[2],int(texto[3]))
        cuentas.append(e)
    return(cuentas)

def crear_cuentas(cuentas):
    
    num_Cuentas=int(input("Cuantas cuentas desea agregar"))
    for index in range(0,num_Cuentas):
        cuenta=input("Introduce numero de cuenta")
        propietario=input("Introduce nombre del propietario")
        cedula=input("Ingrese su cedula ")
        dinero=int(input("Ingrese Saldo"))
        e=Cuenta(cuenta,cedula,propietario,dinero)
        save_cuenta_list(cuentas,e)
    return cuentas
    
def display_cuentas():
    print("\t __Banco__")
    print("1. Ingresar cuentas: ")
    print("2. Cargar cuentas: ")
    option=int(input("Opcion:"))
    print("")
    return  option



def display_edit():
    print("___SERVICIO BANCARIOS___")
    print ("1. Para retirar")
    print ("2. Para consignar")
    opcion=int (input("Opcion: "))
    cantidad=int(input("Ingrese el valor $ "))
    print("")
    return  cantidad,opcion

def menu():
    cuentas=[]
    option=display_cuentas()
    if (option==1):
        cuentas=crear_cuentas(cuentas)
        
    elif(option==2):
        cuentas=abrir_cuentas(cuentas)
    print("Introduce numero de cuenta para continuar")    
    cuenta_a_procesar=input("Numero de cuenta: ")
    print("")
    for usuario in cuentas:
        if (usuario.cuenta==cuenta_a_procesar):
            print("___Tu cuenta actual___")
            usuario.mostrar_Cuenta()
            valor_modificador,accion=display_edit()
            
            if(accion==1):
                usuario.retirar(valor_modificador)
                Guardar_cuentas(cuentas)
                print("___Tu cuenta actual___")
                usuario.mostrar_Cuenta()
                
            elif(accion==2):
                usuario.consignar(valor_modificador)
                Guardar_cuentas(cuentas)
                print("___Tu cuenta actual___")
                usuario.mostrar_Cuenta()
menu()








            
