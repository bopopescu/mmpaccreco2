from Conexion import Conexion

#main
oConexion = Conexion().miconexion

#select
cursorSelect =oConexion.cursor()
cursorSelect.execute("select * from bibliotecario")
for fila in cursorSelect:
    print(fila)

#insert
cursorInsert = oConexion.cursor()
sql="insert into bibliotecario(id,nombre,clave) values(%s,%s,%s)"

insert0=(0,"nombre insertado 0","clave insertada 0")
cursorInsert.execute(sql, insert0)
#oConexion.commit()
insert1=(0,"nombre insertado 1","clave insertada 1")
cursorInsert.execute(sql, insert1)

insert2=(0,"nombre insertado 2","clave insertada 2")
cursorInsert.execute(sql, insert2)

#update
cursorUpdate = oConexion.cursor()
sql="update bibliotecario set nombre=%s where id=%s"
update0=("nombre modificado",12)
cursorUpdate.execute(sql,update0)
#oConexion.commit()
#delete
cursorDelete = oConexion.cursor()
sql="delete from bibliotecario where id = %s"
delete0=(13,)   #id es int, pero al ser python y ser un parámetros, hay que ponerlo así
cursorDelete.execute(sql,delete0)


cursorSelect = oConexion.cursor()
cursorSelect.execute("select * from bibliotecario")
for fila in cursorSelect:
    print(fila)

oConexion.commit()
oConexion.close()