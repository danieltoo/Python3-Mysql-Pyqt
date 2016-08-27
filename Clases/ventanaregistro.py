from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import  sys
import mysql.connector
import time
class Registro(QMainWindow):
	"""docstring for VentRegistro"""
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("/home/deadpool/Escritorio/Practica 2/xml/VRegistroAlumn.ui",self)
		self.BotonValidar.clicked.connect(self.Validar)
		self.BotonResgitro.clicked.connect(self.Registra)
		self.BotonFile.clicked.connect(self.file)

	def file(self):
		fileName, _ = QFileDialog.getOpenFileName(self, "Foto",'/home',"Images (*.png *.xpm *.jpg)")
		if fileName:
			image = QImage(fileName)
			if image.isNull():
				QMessageBox.information(self, "Image Viewer","Nose puede cargar %s." % fileName)
				return
			self.imagen.setPixmap(QPixmap.fromImage(image))
			self.cajaFoto.setText(fileName)	

	def Registra(self):
		conn=mysql.connector.Connect(host='localhost',user='root',password='200388',database='Curso')
		cursor=conn.cursor()
		dateN=self.dateNacer.date().toPyDate()
		sentencia=("insert into Usuario(user,nombre,paterno,materno,sexo,nacimiento,telefono,direccion,email,foto,registro) values('"
			+self.CajaNombreU.text()+"','"+self.cajaNombre.text()+"','"+self.cajaPaterno.text()+"','"+self.cajaMaterno.text()+"','"+self.comboSexo.currentText()+"',"+
			str(dateN)+",'"+self.cajaTelefono.text()+"','"+self.cajaDireccion.text()+"','"+self.cajaEmail.text()+"','"+self.cajaFoto.text()+"',"+str(time.strftime("%Y-%m-%d"))+");")
		try:
			cursor.execute(sentencia)
		except :
			QMessageBox.information(self, "Error Nombre","Nombre de Usuario Existente")
		conn.commit()
		cursor.close()
		conn.close()
		self.creausuario()
		self.Regresa()

	def Regresa(self):
		self.menu.show()
		self.setVisible(False)

	def creausuario(self):
		conn=mysql.connector.Connect(host='localhost',user='root',password='200388',database='Curso')
		cursor=conn.cursor()
		sentencia=("Create user '"+self.CajaNombreU.text()+"'@'localhost' identified by '"+
			self.CajaPass.text()+"'")
		try:
			cursor.execute(sentencia)
		except :
			reply =QMessageBox.information(self, 'Error',"Datos Incorrectos")


	def Validar(self):
		if self.CajaPass.text()==self.CajaRep.text():
			self.ValidarContra.setText("OK")
			self.ValidarContra_2.setText("OK")
			self.ValidarUsuario()
		else :
			self.ValidarContra.setText("X")
			self.ValidarContra_2.setText("X")

	def ValidarUsuario(self):
		conn=mysql.connector.Connect(host='localhost',user='root',password='200388',database='Curso')
		cursor=conn.cursor()
		boo=False
		try:
			cursor.execute("select user from Usuario")
			for i in cursor:
				if str(self.CajaNombreU.text())==str(i[0]):
					boo=True
		except :
			boo=False
		if boo:
			self.ValidarUser.setText("X")
		else:
			self.ValidarUser.setText("OK")
		conn.commit()
		cursor.close()
		conn.close()

	def antMenu(self,_menu):
		self.menu=_menu
