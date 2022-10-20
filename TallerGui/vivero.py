import sys
from PyQt5.QtWidgets  import  QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5 import uic, QtCore, QtGui, QtWidgets
#from ui.interfaz import ui_interfaz



qtCreatorFile = "TallerQt/Interfaz.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):  
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Agregarpropietario.clicked.connect(self.add_pro)
        self.Agregarfinca.clicked.connect(self.add_pro)

        
    def add_pro(self):

        identificacion = self.id.text()
        nombre = self.Nombre.text()
        apellido =  self.Apellido.text()
        correo =  self.Correo.text()
        tel = self.Tel.text()

        print(identificacion)

        if identificacion and nombre and apellido and correo and tel  != "":
            msgadd()            
        else:
            msgError() 
              
            
            
           


def msgError():
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Debe completar todos los campos!")
    msgBox.setWindowTitle("Error!")
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgBox.buttonClicked.connect(msgButtonClick)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print('OK clicked')

def msgButtonClick(i):
   print("Button clicked is:",i.text())

def msgadd():
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Productor agregado!")
    msgBox.setWindowTitle("Éxito!")
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgBox.buttonClicked.connect(msgButtonClick)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print('OK clicked')

def msgButtonClick(i):
   print("Button clicked is:",i.text())
    
    

        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

    