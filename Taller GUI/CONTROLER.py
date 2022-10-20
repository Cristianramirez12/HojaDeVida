import sys
from PyQt5.QtWidgets  import  QMessageBox, QPushButton, QTableWidgetItem
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from GUI.InterfazHospital import *
from GUI.InterfazMedico import *
from GUI.Informacion import *
from Modelo.Hospital import *
from Modelo.Medico import *
from Modelo.msg import *




WindowPrincipal = "GUI/Principal.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(WindowPrincipal)

class Principal(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self):  
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.CrearHospital.clicked.connect(self.ventanaHospital)
        self.AgregarMedico.clicked.connect(self.ventanaMedico)
        self.ConsultarMedico.clicked.connect(self.ventanaInfo)
    
    def ventanaHospital(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_Hospital()
        self.ui.setupUi(self.ventana)
        self.ventana.show()        
        self.ui.AgregarHospital.clicked.connect(self.AgregarH)

    def ventanaMedico(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_Medico()
        self.ui.setupUi(self.ventana)
        self.ventana.show()        
        self.ui.GuardarM.clicked.connect(self.AgregarM)

    def ventanaInfo(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_Informacion()
        self.ui.setupUi(self.ventana)
        self.ventana.show()        
        self.ui.Buscar.clicked.connect(self.Info)
        
        

    def AgregarH(self):
        NomHospital = self.ui.NombreHospital.text()        
        AgrearHosp ital(NomHospital)
        self.ventana.close() 
        msgaddH() 

    def AgregarM(self):
        Nom = self.ui.Nombre.text()
        Esp = self.ui.Especialidad.text()
        Dni = self.ui.Dni.text()
        Hospital = self.ui.Hospital.text()
        NewMedico = CreateMedico(Nom, Esp, Dni)
        print(NewMedico.nombre)
        H = BuscarHospital(Hospital)
        H.plantel.append(NewMedico)
        print(H.plantel[0])
        self.ventana.close()
        msgaddM() 

    def Info(self):
        Dni = self.ui.dni.text()
        H, M = BuscarMedico(Dni)
        fila = 0

        for fila in range(len(H.plantel)):
            M = H.plantel[fila]
            nom = QTableWidgetItem(M.nombre)
            esp = QTableWidgetItem(M.especialidad)
            dni = QTableWidgetItem(M.dni)
            Hos = QTableWidgetItem(H.nombre)
            self.ui.tableWidget.insertRow(fila)
            self.ui.tableWidget.setItem(fila, 0, nom)
            self.ui.tableWidget.setItem(fila, 1, esp)
            self.ui.tableWidget.setItem(fila, 2, dni)
            self.ui.tableWidget.setItem(fila, 3, Hos)
            self.show()
            fila += 1
            
        
                  
 

        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Principal()
    window.show()
    sys.exit(app.exec_())

    