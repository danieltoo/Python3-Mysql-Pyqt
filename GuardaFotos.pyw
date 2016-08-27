import MySQLdb as dbapi #importar libreria python
import sys #importar metodos del systema
from Tkinter import *
def sacarfotos():
	fotos ,usuarios=nombredefotos()
	for i in range(len(fotos)):
		try:
		    fout =open("imagen"+str(i),'wb')#nombre archivo que se guardar (cualquier nombre) en el archivo de salida
		    conn = dbapi.connect(host='localhost',user='root', passwd='200388', db='tecnologico')#conexion a la base de datos
		    c = conn.cursor()#creacion cursor (puntero)
		    c.execute ("select img from images where user='"+usuarios[i]+"'")#sentencia que recupera la foto a travez de una id de la tabla de la base de datos
		    fout.write(c.fetchone()[0])#escribe el resultado en el archivo de salida
		    fout.close()#cerrar archivo
		    c.close()#cerrar cursor
		    conn.close()#cerrar conexion
		except :
			print ("Error","Fotos imposibles de crear")
def nombredefotos():
	fotos=[]
	usuarios=[]
	try:
		conn = dbapi.connect(host='localhost',user='root', passwd='200388', db='Curso')#conexion con base de datos
		cur = conn.cursor()#declara cursor
		sentencia="select user,foto from Usuario "
		
		cur.execute(sentencia)
		
	
		for i in cur:
			usuarios.append(i[0])
			fotos.append(i[1])
			
		cur.close()
		conn.close()
	except :
		print ("Error en la base")
	return fotos ,usuarios

def guardausfotos():
	fotos ,usuarios=nombredefotos()
	for i in range(len(fotos)):
		try:
			fin = open(str(fotos[i]),"rb")
			print 1
			img = fin.read()
			print 2
			fin.close() #cierra el archivo
			print 3
			n=dbapi.escape_string(img)
			conn = dbapi.connect(host='localhost',user='root', passwd='200388', db='Curso')#conexion con base de datos
			cursor = conn.cursor()
			print 4
			sentencia=("INSERT INTO Usuario SET img = '%s'" % \
            n)#ejecuta sentencia de ingreso de imagen

			cursor.execute

			print 5
			conn.commit()#cierra transaccion
			cursor.close()#cierra cursor
			conn.close()
		except :
			print("Imagenes imposibles de guardar")
vent=Tk()
vent.title("Guardado de imagenes")
vent.geometry("400x400")
Boton = Button(vent,text="Guaradar imagenes en la Base ",command=guardausfotos).place(x=100,y=100)
boton2=Button(vent,text="Sacar Fotos de la base",command=sacarfotos).place(x=150,y=150)
vent.mainloop()

