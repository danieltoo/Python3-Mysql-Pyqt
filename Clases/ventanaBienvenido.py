from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import  sys
import mysql.connector
import time
class Bienvenido(QMainWindow):
	"""docstring for Vbienvenido"""
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("/home/deadpool/Escritorio/Practica 2/xml/Vbienvenido.ui",self)
		self.BotonBase.clicked.connect(self.Base)
		self.BotonRegresar.clicked.connect(self.Regresa)
	def Regresa(self):
		self.tipo.show()
		self.setVisible(False)

	def Base(self):
		self.base.show()
		self.base.user(self.admin,self.name)
		self.admin=False
		self.setVisible(False)

	def user(self,adm,_name):
		self.admin=adm
		self.name=_name
		self.usuario.setText(_name)

	def antTipo(self,_tipo):
		self.tipo=_tipo
	def sigBase(self,_base):
		self.base=_base