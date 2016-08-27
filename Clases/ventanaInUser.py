from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import  sys
import mysql.connector
import time
class IngresoUser(QMainWindow):
	"""docstring for IngresoUser"""
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("/home/deadpool/Escritorio/Practica 2/xml/VingresoUsuario.ui",self)
		self.BotonIngresar.clicked.connect(self.valUser)
		self.BotonRegresar.clicked.connect(self.Regresa)
	def Regresa (self):
		self.tipo.show()
		self.setVisible(False)

	def Ingresar(self):
		self.bienvenido.show()
		self.bienvenido.user(True,self.name)
		self.setVisible(False)
		
	def valUser(self):
		user=self.CajaUser.text()
		passw=self.CajaContra.text()

		conn=mysql.connector.Connect(host='localhost',user='root',password='200388',database='Curso')
		cursor=conn.cursor()
		Userboo=False
		try:
			cursor.execute("select user from Usuario")
			for i in cursor:
				if str(i[0])==user :
					Userboo=True
		except :
			Userboo=False
		passwboo=self.valPass(user,passw)
		if Userboo and passwboo:
			self.name=user;
			self.Ingresar()
		else :
			if Userboo==False:
				reply =QMessageBox.information(self, 'Error',"Usuario Incorrecto")
			elif passwboo==False:
				reply =QMessageBox.information(self, 'Error',"Aun no esta dado de alta")
			else:
				reply =QMessageBox.information(self, 'Error',"Aun no esta dado de alta")
		self.CajaUser.setText("")
		self.CajaContra.setText("")

	def valPass(self,user,passw):
		boo=False
		try:
			conn=mysql.connector.Connect(host='localhost',user=user,password=passw,database='Curso')
			cursor=conn.cursor()
			boo=True
		except:
			boo=False
		return boo
	def antTipo(self,_tipo):
		self.tipo=_tipo

	def sigBienvenido(self,_bienvenido):
		self.bienvenido=_bienvenido
