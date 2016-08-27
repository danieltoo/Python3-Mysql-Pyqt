from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import  sys
import mysql.connector
import time
class Tipo(QMainWindow):
	"""docstring for tipo"""
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("/home/deadpool/Escritorio/Practica 2/xml/Vtipousuario.ui",self)
		self.BotonAdmin.clicked.connect(self.admin)
		self.BotonUser.clicked.connect(self.user)
		self.BotonRegresa.clicked.connect(self.Regresa)


	def Regresa(self):
		self.menu.show()
		self.setVisible(False)

	def admin(self):
		self.ingadmin.show()
		self.setVisible(False)

	def user(self):
		self.inguser.show()
		self.setVisible(False)

	def antMenu(self,_menu):
		self.menu=_menu

	def sigIngadmin(self,_ingadmin):
		self.ingadmin=_ingadmin

	def sigIngUser(self,_inguser):
		self.inguser=_inguser