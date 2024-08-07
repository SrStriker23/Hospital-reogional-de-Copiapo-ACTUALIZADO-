import pymysql
#-----------------------------------------------------------------------Conexion a la base de datos hospital----------------------------------------------------------------------------------  
class DataBase:
	def __init__(self):
		self.connection = pymysql.connect(
				host='localhost',
				user= 'root',
				password='',
				db='hospital'
			)
		self.cursor=self.connection.cursor()
#----------------------------------------------------------------------------------SQL PERSONAL----------------------------------------------------------------------------------  
class Personal(DataBase):

    def consulta_personal(self):
        sql = "SELECT * FROM `personal administrativo` ORDER BY id ASC"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
    

    def buscar_personal(self, documento):
        sql=f'SELECT id,Nombre,`Fecha de ingreso`,`Prevision de salud`,`Sueldo bruto`,`Unidad administrativa`,Cargo FROM `personal administrativo` WHERE Rut="{documento}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
    
    def Rutspersonal(self):
        sql=f'SELECT Rut FROM `personal administrativo`'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos

    def insertar_personal(self,documento,nombre,fecha,prevision,sueldo,unidad,cargo):
        
        sql=f'INSERT INTO `personal administrativo` (`Rut`, `Nombre`, `Fecha de ingreso`, `Prevision de salud`, `Sueldo bruto`, `Unidad administrativa`,`Cargo`) VALUES ("{documento}", "{nombre}", "{fecha}", "{prevision}", "{sueldo}", "{unidad}","{cargo}")'
        try:
            self.cursor.execute(sql)
            n = self.cursor.rowcount
            self.connection.commit()
            print("Datos Guardados Correctamente")
            return 1
        except Exception as ex:
            print(ex)
        return n
      
    def eliminar_personal(self,documento):
        sql=f'DELETE FROM `personal administrativo` WHERE `Rut`="{documento}"'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se elimino correctamente el personal")
            return 1
        except Exception as e:
            raise e  

    def modificar_personal(self,documento,fecha,prevision,sueldo,unidad,cargo):

        sql=f'UPDATE `personal administrativo` SET `Fecha de ingreso` = "{fecha}",`Prevision de salud` = "{prevision}", `Sueldo bruto` = "{sueldo}", `Unidad administrativa` = "{unidad}",`Cargo` = "{cargo}" WHERE `Rut` = "{documento}"'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se modifico correctamente [fecha de ingreso,prevision,sueldo,unidad,cargo] ....")
            return 1
        except Exception as e:
            raise e
        
#----------------------------------------------------------------------------------SQL PAGO PERSONAL----------------------------------------------------------------------------------       
class  PagoPersonal(DataBase):

    def consulta_pagos_personal(self):
        sql = "SELECT * FROM `pago personal` ORDER BY id ASC"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
    
    def eliminar_pago_personal(self,documento):
        sql=f'DELETE FROM `pago personal` WHERE `Rut`="{documento}"'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se elimino correctamente el pago personal")
        except Exception as e:
            raise e
        
    def buscar_pago_personal(self, documento):
        sql=f'SELECT * FROM `pago personal` WHERE Rut="{documento}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
    
    def Rutspagopersonal(self):
        sql=f'SELECT Rut FROM `pago personal`'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
    def modificar_pagopersonal(self,documento,sueldo,descuento,bonificacion,liquido):

        sql=f'UPDATE `pago personal` SET `Sueldo bruto` = "{sueldo}",`Descuentos` = "{descuento}", `Bonificaciones` = "{bonificacion}", `Sueldo liquido` = "{liquido}" WHERE `Rut` = "{documento}"'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se modifico correctamente ....")
            return 1
        except Exception as e:
            raise e
        
class Busquedas(DataBase):

    def Sueldos_ordenados(self):
        sql=f'SELECT id,Rut,Nombre,`Sueldo liquido` FROM `pago personal` ORDER BY `Sueldo liquido` DESC'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            return datos
        except Exception as ex:
            print(ex)
    
    def Fecha_ingreso_personal(self):
        sql=f'SELECT id,Rut, Nombre, `Fecha de ingreso` FROM ( SELECT id,Rut, Nombre, `Fecha de ingreso` FROM medico UNION ALL SELECT id,Rut, Nombre, `Fecha de ingreso` FROM tens UNION ALL SELECT id,Rut, Nombre, `Fecha de ingreso` FROM `personal administrativo` ) AS todas_las_tablas ORDER BY `Fecha de ingreso` ASC'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            return datos
        except Exception as ex:
            print(ex)

    def Medicos_x_Especialista(self,especialidad):
        sql=f'SELECT * FROM medico WHERE Especialidad="{especialidad}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            return datos
        except Exception as ex:
            print(ex)

    def Tens_x_Areas(self,area):
        sql=f'SELECT * FROM tens WHERE Area="{area}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            return datos
        except Exception as ex:
            print(ex)

    def Administrativos_x_cargo_unidad(self,unidad,cargo):
        sql=f'SELECT * FROM `personal administrativo` WHERE `Unidad administrativa`="{unidad}" AND Cargo="{cargo}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            return datos
        except Exception as ex:
            print(ex)

    def fechas_tramos(self,inicio,fin):
        sql=f'SELECT id,Rut,Nombre,`Fecha de ingreso` FROM medico WHERE `Fecha de ingreso` >= "{inicio}-01-01" AND `Fecha de ingreso` <= "{fin}-12-31" UNION SELECT id,Rut,Nombre,`Fecha de ingreso` FROM tens WHERE `Fecha de ingreso` >= "{inicio}-01-01" AND `Fecha de ingreso` <= "{fin}-12-31" UNION SELECT id,Rut,Nombre, `Fecha de ingreso` FROM `personal administrativo` WHERE `Fecha de ingreso` >= "{inicio}-01-01" AND `Fecha de ingreso` <= "{fin}-12-31" ORDER BY `Fecha de ingreso` ASC'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            return datos
        except Exception as ex:
            print(ex)

    def Cantidad_derivacion(self):
        sql='SELECT Derivacion, COUNT(*) as cantidad FROM pacientes GROUP BY Derivacion'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            return datos
        except Exception as ex:
            print(ex)

    def Cobros_Ordenados(self):
        sql='SELECT id,Rut,nombre,`Cobro total` FROM `cobro paciente` ORDER BY `Cobro total` DESC'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            return datos
        except Exception as ex:
            print(ex)
            
    def Prevision_cantidad(self):
        sql='SELECT `Prevision de salud`,COUNT(*) FROM ( SELECT `Prevision de salud` FROM medico UNION ALL SELECT `Prevision de salud` FROM tens UNION ALL SELECT `Prevision de salud` FROM `personal administrativo` UNION ALL SELECT `Prevision de salud` FROM pacientes ) AS Cantidad GROUP BY `Prevision de salud`'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            return datos
        except Exception as ex:
            print(ex)
      
