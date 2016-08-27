from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import  sys
import mysql.connector
import time
class IngresoAdmin(QMainWindow):
	"""docstring for IngresoAdmin"""
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("/home/deadpool/Escritorio/Practica 2/xml/VIngresoAdmin.ui",self)
		self.BotonIngresar.clicked.connect(self.Ingresar)
		self.BotonRegresa.clicked.connect(self.Regresa)
	def Regresa(self):
		self.tipo.show()
		self.setVisible(False)

	def Ingresar(self):
		if self.ValAdmin(self.CajaAdmin.text(),self.CajaContra.text()):
			self.bienvenido.show()
			self.bienvenido.user(False,self.CajaAdmin.text())
			self.setVisible(False)
			
		else :
			reply =QMessageBox.information(self, 'Error',"Datos Incorrectos")
		self.CajaAdmin.setText("")
		self.CajaContra.setText("")

	def ValAdmin(self,admin,passw):
		boo=False
		try:
			conn=mysql.connector.Connect(host='localhost',user=admin,password=passw,database='Curso')
			cursor=conn.cursor()
			boo=True
		except :
			boo=False
		return boo

	def antTipo(self,_tipo):
		self.tipo=_tipo
	def sigBienvenido(self,_bienvenido):
		self.bienvenido=_bienvenido
