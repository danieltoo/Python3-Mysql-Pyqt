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

class IngresoUser(QMainWindow):
	"""docstring for IngresoUser"""
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("VingresoUsuario.ui",self)
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

class Base(QMainWindow):
	"""docstring for Vbase"""
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("/home/deadpool/Escritorio/Practica 2/xmlVconsultas.ui",self)
		self.BotonEnabled.clicked.connect(self.habilita)
		self.BotonDisEnabled.clicked.connect(self.deshabilita)
		self.BotonSalir.clicked.connect(self.Regresar)
		self.checkTodos.clicked.connect(self.Todos)
		self.BotonVer.clicked.connect(self.Vertodo)
		self.BotonAltas.clicked.connect(self.darAlta)
		self.BotonBajas.clicked.connect(self.darBaja)
		self.BotonBuscar.clicked.connect(self.Busqueda)
		self.BotonActualizar.clicked.connect(self.Actualizar)

	def Actualizar(self):
		for row in range(self.tableConsultas.rowCount()):
			conn=mysql.connector.Connect(host='localhost',user='root',password='200388',database='Curso')
			cursor=conn.cursor()
			arr=["user","nombre",
			"paterno","materno","sexo","nacimiento"
			,"telefono","direccion","email","foto","registro"]
			sentencia="update Usuario set "
			
			for column in range (self.tableConsultas.columnCount()):
				if column==0:
					sentencia=sentencia+arr[column]+"='"+self.tableConsultas.item(row,column).text()+"'"
				else :
					sentencia=sentencia+","+arr[column]+"='"+self.tableConsultas.item(row,column).text()+"' "
			sentencia=sentencia+"where "+arr[0]+"='"+self.tableConsultas.item(row,0).text()+"'"
			try:
				cursor.execute(sentencia)
			
			except :
				QMessageBox.information(self, 'Error',"Error al actualizar datos")
			conn.commit()
			cursor.close()
			conn.close()

	def Busqueda(self):
		self.limpia()
		camp=""
		if self.checkTodos.isChecked():
			camp="*"
			columnas=["Usuario","Nombre",
		"Paterno","Materno","Sexo","Nacimiento"
		,"Telefono","Direccion","Email","Foto","Registro"]
		else:	
			columnas, campos=self.arreglo()
			for i in range (len (campos)):
				if i==0:
					camp=campos[i]
				else:
					camp=camp+","+campos[i]
		conn=mysql.connector.Connect(host='localhost',user='root',password='200388',database='Curso')
		cursor=conn.cursor()
		where=self.where()
		sentencia="select "+camp+" from Usuario where "+ where
		#hacer conexion busquda y todo metodo actualizar 
		row=0
		try:
			cursor.execute(sentencia)

			self.tableConsultas.setColumnCount(len(columnas))
			self.tableConsultas.setHorizontalHeaderLabels(columnas)
			
			
			for ncontrol in cursor:
				self.tableConsultas.insertRow(row)	
				for co in range(len(ncontrol)):
					nco=QTableWidgetItem(str(ncontrol[co]))
					self.tableConsultas.setItem(row,co,nco)
				row=row+1
			
		except:
			QMessageBox.information(self, 'Error',"Busqueda sin resultados")

	def limpia(self):
		self.tableConsultas.setRowCount(0)

	def where(self):
		where =""
		if self.CajaUser.isEnabled():
			if where=="":
				where="user='"+self.CajaUser.text()+"'"
			else :
				where=where+",user='"+self.CajaUser.text()+"'"

		if self.CajaNombre.isEnabled():
			if where=="":
				where="nombre='"+self.CajaNombre.text()+"'"
			else :
				where=where+",nombre='"+self.CajaNombre.text()+"'"
		if self.CajaPaterno.isEnabled():
			if where=="":
				where="paterno='"+self.CajaPaterno.text()+"'"
			else :
				where=where+",paterno='"+self.CajaPaterno.text()+"'"
		if self.CajaMaterno.isEnabled():
			if where=="":
				where="materno='"+self.CajaMaterno.text()+"'"
			else :
				where=where+",'"+self.CajaMaterno.text()+"'"	
		dateN=self.dateNacimiento.date().toPyDate()
		dateN=dateN.strftime('%Y-%m-%d')	
		if self.dateNacimiento.isEnabled():
			if where=="":
				where="nacimiento='"+str(dateN)+"'"
			else :
				where=where+"nacimiento=,'"+self.dateNacimiento.text()+"'"

		if self.CajaTelefono.isEnabled():
			if where=="":
				where="telefono='"+self.CajaTelefono.text()+"'"
			else :
				where=where+",telefono='"+self.CajaTelefono.text()+"'"

		if self.CajaDireccion.isEnabled():
			if where=="":
				where="direccion='"+self.CajaDireccion.text()+"'"
			else :
				where=where+",direccion='"+self.CajaDireccion.text()+"'"

		if self.comboSexo.isEnabled():
			if where=="":
				where="sexo='"+self.comboSexo.currentText()+"'"
			else :
				where=where+",sexo='"+self.comboSexo.currentText()+"'"

		if self.CajaFoto.isEnabled():
			if where=="":
				where="foto='"+self.CajaFoto.text()+"'"
			else :
				where=where+",foto='"+self.CajaFoto.text()+"'"
		dateR=self.dateRegistro.date().toPyDate()
		dateR=dateR.strftime('%Y-%m-%d')
		if self.dateRegistro.isEnabled():
			if where=="":
				where="registro='"+str(dateR)+"'"
			else :
				where=where+",registro='"+str(dateR)+"'"
		return where;

	def arreglo (self):	
		
		arr =[]
		campos=[]

		
		if self.checkUser.isChecked():
			campos.append("user")
			arr.append(self.checkUser.text())
	
		if self.checkNombre.isChecked():
			campos.append("nombre")
			arr.append(self.checkNombre.text())
		
		if self.checkPaterno.isChecked():
			campos.append("paterno")
			arr.append(self.checkPaterno.text())
			
		if self.checkMaterno.isChecked():
			campos.append("materno")
			arr.append(self.checkMaterno.text())
			
		if self.checkSexo.isChecked():
			campos.append("sexo")
			arr.append(self.checkSexo.text())
			
		if self.checkNacimiento.isChecked():
			campos.append("nacimiento")
			arr.append(self.checkNacimiento.text())
		
		if self.checkTelefono.isChecked():
			campos.append("telefono")
			arr.append(self.checkTelefono.text())
		
		if self.checkDireccion.isChecked():
			campos.append("direccion")
			arr.append(self.checkDireccion.text())
			
		if self.checkEmail.isChecked():
			campos.append("email")
			arr.append(self.checkEmail.text())
			
		if self.checkFotos.isChecked():
			campos.append("foto")
			arr.append(self.checkFotos.text())
			
		if self.checkRegistro.isChecked():
			campos.append("registro")
			arr.append(self.checkRegistro.text())
		return arr , campos
			
	def darBaja(self):
		corrent=str(self.tableConsultas.currentItem().text())
		print(corrent)
		responder =QMessageBox.question (self, 'Mensaje',
			"¿Desea dar e baja a este usuario?",QMessageBox.Yes | 
			QMessageBox.No,QMessageBox.No)
		if responder==QMessageBox.Yes:
			self.borrarUsuario()
			self.borrarRegistro()

	def borrarUsuario(self):
		corrent=str(self.tableConsultas.currentItem().text())
		conn=mysql.connector.Connect(host='localhost',user='root',password='200388',database='Curso')
		cursor=conn.cursor()
		sentencia="drop user '"+corrent+"'@'localhost'";
		try:
				cursor.execute(sentencia)
		except :
			QMessageBox.information(self, 'Error',"Error usuario no Existente")
		conn.close()

	def borrarRegistro(self):
		corrent=str(self.tableConsultas.currentItem().text())
		conn=mysql.connector.Connect(host='localhost',user='root',password='200388',database='Curso')
		cursor=conn.cursor()
		sentencia="delete from Usuario where user='"+corrent+"'";
		try:
				cursor.execute(sentencia)
		except :
			QMessageBox.information(self, 'Error',"Selecionar toda la Fila 2")
		conn.commit()
		cursor.close()
		conn.close()

	def darAlta(self):
		corrent=str(self.tableConsultas.currentItem().text())
		responder = QMessageBox.question (self, 'Mensaje',
			"¿Desea dar de alta a este usuario?",QMessageBox.Yes | 
			QMessageBox.No, QMessageBox.No)
		if responder==QMessageBox.Yes:
			conn=mysql.connector.Connect(host='localhost',user='root',password='200388',database='Curso')
			cursor=conn.cursor()
			sentencia="grant select  on Curso.Usuario to '"+corrent+"'@'localhost'";
			try:
				cursor.execute(sentencia)
			except :
				QMessageBox.information(self, 'Error',"Selecionar toda la Fila")
			conn.close()

	def Vertodo (self):
		self.checkTodos.setChecked(True)
		self.checkUser.setEnabled(False)
		self.checkUser.setChecked(False)
		self.checkNombre.setEnabled(False)
		self.checkNombre.setChecked(False)
		self.checkPaterno.setEnabled(False)
		self.checkPaterno.setChecked(False)
		self.checkMaterno.setEnabled(False)
		self.checkMaterno.setChecked(False)
		self.checkNacimiento.setEnabled(False)
		self.checkNacimiento.setChecked(False)
		self.checkTelefono.setEnabled(False)
		self.checkTelefono.setChecked(False)
		self.checkDireccion.setEnabled(False)
		self.checkDireccion.setChecked(False)
		self.checkSexo.setEnabled(False)
		self.checkSexo.setChecked(False)
		self.checkFotos.setEnabled(False)
		self.checkFotos.setChecked(False)
		self.checkRegistro.setEnabled(False)
		self.checkRegistro.setChecked(False)
		self.checkEmail.setEnabled(False)
		self.checkEmail.setChecked(False)
		self.limpia()
		arr=["Usuario","Nombre",
		"Paterno","Materno","Sexo","Nacimiento"
		,"Telefono","Direccion","Email","Foto","Registro"]
		conn=mysql.connector.Connect(host='localhost',user='root',password='200388',database='Curso')
		cursor=conn.cursor()
		sentencia=("select * from Usuario")
		row=0
		try:
			cursor.execute(sentencia)
			self.tableConsultas.setColumnCount(11)
			self.tableConsultas.setHorizontalHeaderLabels(arr)
			
			for ncontrol in cursor:
				self.tableConsultas.insertRow(row)	
				for co in range(len(ncontrol)):
					nco=QTableWidgetItem(str(ncontrol[co]))
					self.tableConsultas.setItem(row,co,nco)
				row=row+1
		except:
			QMessageBox.information(self, 'Error',"Error en la Base de Datos")
		
		conn.close()

	def Todos(self):
		if self.checkTodos.isChecked():
			self.checkUser.setEnabled(False)
			self.checkUser.setChecked(False)
			self.checkNombre.setEnabled(False)
			self.checkNombre.setChecked(False)
			self.checkPaterno.setEnabled(False)
			self.checkPaterno.setChecked(False)
			self.checkMaterno.setEnabled(False)
			self.checkMaterno.setChecked(False)
			self.checkNacimiento.setEnabled(False)
			self.checkNacimiento.setChecked(False)
			self.checkTelefono.setEnabled(False)
			self.checkTelefono.setChecked(False)
			self.checkDireccion.setEnabled(False)
			self.checkDireccion.setChecked(False)
			self.checkSexo.setEnabled(False)
			self.checkSexo.setChecked(False)
			self.checkFotos.setEnabled(False)
			self.checkFotos.setChecked(False)
			self.checkRegistro.setEnabled(False)
			self.checkRegistro.setChecked(False)
			self.checkEmail.setEnabled(False)
			self.checkEmail.setChecked(False)
		else :
			self.checkUser.setEnabled(True)
			self.checkNombre.setEnabled(True)
			self.checkPaterno.setEnabled(True)
			self.checkMaterno.setEnabled(True)
			self.checkNacimiento.setEnabled(True)
			self.checkTelefono.setEnabled(True)
			self.checkDireccion.setEnabled(True)
			self.checkSexo.setEnabled(True)
			self.checkFotos.setEnabled(True)
			self.checkRegistro.setEnabled(True)
			self.checkEmail.setEnabled(True)
	def Regresar(self):
		self.checkUser.setEnabled(False)
		self.checkUser.setChecked(False)
		self.checkNombre.setEnabled(False)
		self.checkNombre.setChecked(False)
		self.checkPaterno.setEnabled(False)
		self.checkPaterno.setChecked(False)
		self.checkMaterno.setEnabled(False)
		self.checkMaterno.setChecked(False)
		self.checkNacimiento.setEnabled(False)
		self.checkNacimiento.setChecked(False)
		self.checkTelefono.setEnabled(False)
		self.checkTelefono.setChecked(False)
		self.checkDireccion.setEnabled(False)
		self.checkDireccion.setChecked(False)
		self.checkSexo.setEnabled(False)
		self.checkSexo.setChecked(False)
		self.checkFotos.setEnabled(False)
		self.checkFotos.setChecked(False)
		self.checkRegistro.setEnabled(False)
		self.checkRegistro.setChecked(False)
		self.checkEmail.setEnabled(False)
		self.checkEmail.setChecked(False)
		self.tableConsultas.setRowCount(0)
		self.tableConsultas.setColumnCount(0)
		self.checkTodos.setChecked(True)
		self.CajaUser.setEnabled(False)
		self.CajaNombre.setEnabled(False)
		self.CajaPaterno.setEnabled(False)
		self.CajaMaterno.setEnabled(False)
		self.dateNacimiento.setEnabled(False)
		self.CajaTelefono.setEnabled(False)
		self.CajaDireccion.setEnabled(False)
		self.comboSexo.setEnabled(False)
		self.CajaFoto.setEnabled(False)
		self.Botonfoto.setEnabled(False)
		self.dateRegistro.setEnabled(False)
		self.bienvenido.show()
		self.setVisible(False)

	def habilita(self):
		if self.comboBox.currentText()=='user':
			self.CajaUser.setEnabled(True)
		elif self.comboBox.currentText()=='nombre':
			self.CajaNombre.setEnabled(True)
		elif self.comboBox.currentText()=='paterno':
			self.CajaPaterno.setEnabled(True)
		elif self.comboBox.currentText()=='materno':
			self.CajaMaterno.setEnabled(True)
		elif self.comboBox.currentText()=='nacimiento':
			self.dateNacimiento.setEnabled(True)
		elif self.comboBox.currentText()=='telefono':
			self.CajaTelefono.setEnabled(True)
		elif self.comboBox.currentText()=='direccion':
			self.CajaDireccion.setEnabled(True)
		elif self.comboBox.currentText()=='sexo':
			self.comboSexo.setEnabled(True)
		elif self.comboBox.currentText()=='foto':
			self.CajaFoto.setEnabled(True)
			self.Botonfoto.setEnabled(True)
		elif self.comboBox.currentText()=='registro':
			self.dateRegistro.setEnabled(True)
	
	def deshabilita(self):
		if self.comboBox.currentText()=='user':
			self.CajaUser.setEnabled(False)
		elif self.comboBox.currentText()=='nombre':
			self.CajaNombre.setEnabled(False)
		elif self.comboBox.currentText()=='paterno':
			self.CajaPaterno.setEnabled(False)
		elif self.comboBox.currentText()=='materno':
			self.CajaMaterno.setEnabled(False)
		elif self.comboBox.currentText()=='nacimiento':
			self.dateNacimiento.setEnabled(False)
		elif self.comboBox.currentText()=='telefono':
			self.CajaTelefono.setEnabled(False)
		elif self.comboBox.currentText()=='direccion':
			self.CajaDireccion.setEnabled(False)
		elif self.comboBox.currentText()=='sexo':
			self.comboSexo.setEnabled(False)
		elif self.comboBox.currentText()=='foto':
			self.CajaFoto.setEnabled(False)
			self.Botonfoto.setEnabled(False)
		elif self.comboBox.currentText()=='registro':
			self.dateRegistro.setEnabled(False)

	def otorgaperomiso(self):
		conn=mysql.connector.Connect(host='localhost',user='root',password='200388',database='Curso')
		cursor=conn.cursor()
		sentencia=("grant select on Curso.Usuario to '"+self.CajaNombreU.text()+"'@'localhost'")
		try:
			cursor.execute(sentencia)
		except :
			reply =QMessageBox.information(self, 'Error',"NO hay nombre de usuario")

	def user(self,_admin,_name):
		self.admin=_admin
		self.name=_name
		self.derechos()

	def derechos(self):
		if self.admin:
			self.BotonAltas.setEnabled(False)
			self.BotonBajas.setEnabled(False)
			self.BotonActualizar.setEnabled(False)
	
	def antBienvenido(self,_bienvenido):
		self.bienvenido=_bienvenido

app=QApplication(sys.argv)
_menu=Menu()
_registro=Registro()
_tipo=Tipo()
_ingadmin=IngresoAdmin()
_inguser=IngresoUser()
_bienvenido=Bienvenido()
_base=Base()

_menu.sigRegistro(_registro)
_menu.sigIngreso(_tipo)

_registro.antMenu(_menu)

_tipo.antMenu(_menu)
_tipo.sigIngadmin(_ingadmin)
_tipo.sigIngUser(_inguser)

_ingadmin.antTipo(_tipo)
_ingadmin.sigBienvenido(_bienvenido)

_inguser.antTipo(_tipo)
_inguser.sigBienvenido(_bienvenido)

_bienvenido.antTipo(_tipo)
_bienvenido.sigBase(_base)

_base.antBienvenido(_bienvenido)



_menu.show()
app.exec_()
		