from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import  sys
import mysql.connector
import time
class Menu(QMainWindow):
	"""docstring for ventana"""
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("/home/deadpool/Escritorio/Practica 2/xml/Vmenu.ui",self)
		self.BotonSalir.clicked.connect(self.cerrar)
		self.BotonRegistrarse.clicked.connect(self.Registro)
		self.BotonIngresar.clicked.connect(self.TipoUser)
	
	def Registro(self):
		self.setVisible(False)
		self.registro.show()
	def TipoUser(self):
		self.setVisible(False)
		self.tipo.show()
	def cerrar(self):
		self.destroy()
	def sigRegistro(self,_registro):
		self.registro=_registro
	def sigIngreso(self,_tipo):
		self.tipo=_tipo