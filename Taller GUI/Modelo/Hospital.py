import sys
from PyQt5.QtWidgets  import  QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5 import uic, QtCore, QtGui, QtWidgets



ListHospitals = []


class Hospital():
    
    def __init__(self):
        self.nombre = ""
        self.plantel = []
   
       
    def mostrar(self):
        i = 0
        for i in range(len(self.plantel)):
            M = self.plantel[i]
            print(M.nombre,"\n", M.especialidad,"\n", M.dni)


        
        
def AgrearHospital(Nom):
    Nombre = Nom
    Nombre = Hospital()
    Nombre.nombre = Nom
    ListHospitals.append(Nombre)
    print(ListHospitals)
    mostrar(ListHospitals)


def mostrar (list):
    i = 0
    while i < len(ListHospitals):
        objeto = ListHospitals[i]
        print("\n",objeto.nombre)
        i += 1

def BuscarHospital(Nom):
    i = 0
    for i in range(len(ListHospitals)):
        H = ListHospitals[i]
        if H.nombre == Nom:
            return H

def BuscarMedico(dni):
    i = 0
    j = 0
    for i in range(len(ListHospitals)):
        H = ListHospitals[i]
        for j in range(len(H.plantel)):
            M = H.plantel[j]
            if M.dni == dni:
                return H, M
            j += 1
        i += 1


    

