from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import  sys
import mysql.connector
import time
from Clases.ventanaBase import *
from Clases.ventanaBienvenido import *
from Clases.ventanaInAdmin import *
from Clases.ventanaInUser import *
from Clases.ventanaMenuPrincipal import *
from Clases.ventanaTipoUser import *
from Clases.ventanaregistro import *

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