import MySQLdb as dbapi #importar libreria python
import sys #importar metodos del systema
from Tkinter import *

vent=Tk()
vent.title("Guardado de imagenes")
vent.geometry("400x400")
Boton = Button(vent,text="Guaradar imagenes en la Base ").place(x=100,y=100)
vent.mainloop()
def con():
    try:
        fin = open("ejercicio01.png","rb")#abre archivo ingresar a base de datos
        img = fin.read()#lee el archivo 
        fin.close() #cierra el archivo
     
    except : #excepcion en caso de error
        print ("Error")

    try:
        conn = dbapi.connect(host='localhost',user='root', passwd='200388', db='tecnologico')#conexion con base de datos
        cursor = conn.cursor()#declara cursor
        n=dbapi.escape_string(img)
        cursor.execute("INSERT INTO images SET img = '%s'" % \
            n)#ejecuta sentencia de ingreso de imagen
        conn.commit()#cierra transaccion
        cursor.close()#cierra cursor
        conn.close()#cierra conexion

    except : #genera excepcion en caso de error
        print ("Error ")
   