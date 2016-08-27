import mysql.connector as dbapi#importar libreria mysql
import sys#importar metodos del sistema
try:
    fout =open('algo.png','wb')#nombre archivo que se guardar (cualquier nombre) en el archivo de salida
    conn = dbapi.connect(host='localhost',user='root', passwd='200388', db='tecnologico')#conexion a la base de datos
    c = conn.cursor()#creacion cursor (puntero)
    c.execute ("select img from images where id = 1")#sentencia que recupera la foto a travez de una id de la tabla de la base de datos
    fout.write(c.fetchone()[0])#escribe el resultado en el archivo de salida
    fout.close()#cerrar archivo
    c.close()#cerrar cursor
    conn.close()#cerrar conexion
except Exception as e:
	print (e.args)
   