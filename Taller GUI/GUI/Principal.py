# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Principal(object):
    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.resize(399, 212)
        Principal.setStyleSheet("background-color: rgb(120, 120, 120);")
        self.centralwidget = QtWidgets.QWidget(Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 30, 192, 95))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.CrearHospital = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CrearHospital.setFont(font)
        self.CrearHospital.setObjectName("CrearHospital")
        self.gridLayout.addWidget(self.CrearHospital, 0, 0, 1, 1)
        self.AgregarMedico = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AgregarMedico.setFont(font)
        self.AgregarMedico.setObjectName("AgregarMedico")
        self.gridLayout.addWidget(self.AgregarMedico, 1, 0, 1, 1)
        self.ConsultarMedico = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ConsultarMedico.setFont(font)
        self.ConsultarMedico.setObjectName("ConsultarMedico")
        self.gridLayout.addWidget(self.ConsultarMedico, 2, 0, 1, 1)
        Principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 399, 21))
        self.menubar.setObjectName("menubar")
        Principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Principal)
        self.statusbar.setObjectName("statusbar")
        Principal.setStatusBar(self.statusbar)

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "MainWindow"))
        self.CrearHospital.setText(_translate("Principal", "CREAR HOSPITAL"))
        self.AgregarMedico.setText(_translate("Principal", "AGREGAR UN MEDICO"))
        self.ConsultarMedico.setText(_translate("Principal", "CONSULTAR MEDICOS"))