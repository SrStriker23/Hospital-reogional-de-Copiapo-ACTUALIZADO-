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
                
#----------------------------------------------------------------------------------SQL MEDICOS----------------------------------------------------------------------------------   
class Medicos(DataBase):
     
    def consulta_medicos(self):
        sql = "SELECT * FROM medico ORDER BY id ASC"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
    
    def medico_paciente(self):

        sql = "SELECT Nombre,Especialidad FROM medico "
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos

    def buscar_medico(self, documento):
        sql=f'SELECT id,Nombre,`Fecha de ingreso`,`Prevision de salud`,`Sueldo bruto`,Especialidad FROM medico WHERE Rut="{documento}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
    
    def Ruts(self):
        sql=f'SELECT Rut FROM medico'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos

    def insertar_medico(self,documento,nombre,fecha,prevision,sueldo,especialidad):
        
        sql=f'INSERT INTO `medico` (`Rut`, `Nombre`, `Fecha de ingreso`, `Prevision de salud`, `Sueldo bruto`, `Especialidad`) VALUES ("{documento}", "{nombre}", "{fecha}", "{prevision}", "{sueldo}", "{especialidad}")'
        try:
            self.cursor.execute(sql)
            n = self.cursor.rowcount
            self.connection.commit()
            print("Datos Guardados Correctamente")
            return 1
        except Exception as ex:
            print(ex)
        return n  
      
    def eliminar_medico(self,documento):
        sql=f'DELETE FROM `medico` WHERE `Rut`="{documento}"'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se elimino correctamente el medico")
            return 1
        except Exception as e:
            raise e 

    def modificar_medicos(self,documento,fecha,prevision,sueldo,especialidad):

        sql=f'UPDATE `medico` SET `Fecha de ingreso` = "{fecha}",`Prevision de salud` = "{prevision}", `Sueldo bruto` = "{sueldo}", `Especialidad` = "{especialidad}" WHERE `Rut` = "{documento}"'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se modifico correctamente [fecha de ingreso,prevision,sueldo,especialidad] ....")
            return 1
        except Exception as e:
            raise e
        
#----------------------------------------------------------------------------------SQL TENS----------------------------------------------------------------------------------         
class Tens(DataBase):

    def Rutstens(self):
        sql=f'SELECT Rut FROM tens'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
        
    def consulta_tens(self):
        sql = "SELECT * FROM tens ORDER BY id ASC"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
    
    def buscar_tens(self, documento):
        sql=f'SELECT id,Nombre,`Fecha de ingreso`,`Prevision de salud`,`Sueldo bruto`,Area FROM tens WHERE Rut="{documento}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
    
    def insertar_tens(self,documento,nombre,fecha,prevision,sueldo,area):
        
        sql=f'INSERT INTO `tens` (`Rut`, `Nombre`, `Fecha de ingreso`, `Prevision de salud`, `Sueldo bruto`, `Area`) VALUES ("{documento}", "{nombre}", "{fecha}", "{prevision}", "{sueldo}", "{area}")'
        try:
            self.cursor.execute(sql)
            n = self.cursor.rowcount
            self.connection.commit()
            print("Datos Guardados Correctamente")
            return 1
        except Exception as ex:
            print(ex)
        return n  
      
    def eliminar_tens(self,documento):
        sql=f'DELETE FROM `tens` WHERE `Rut`="{documento}"'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se elimino correctamente el medico")
            return 1
        except Exception as e:
            raise e  

    def modificar_tens(self,documento,fecha,prevision,sueldo,area):

        sql=f'UPDATE `tens` SET `Fecha de ingreso` = "{fecha}",`Prevision de salud` = "{prevision}", `Sueldo bruto` = "{sueldo}", `Area` = "{area}" WHERE `Rut` = "{documento}"'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se modifico correctamente [prevision,sueldo,area] ....")
            return 1
        except Exception as e:
            raise e

#----------------------------------------------------------------------------------SQL PACIENTES----------------------------------------------------------------------------------            
class Pacientes(DataBase):
  
    def suma_de_box(self):
        sql="SELECT SUM(box) FROM pacientes"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            suma = datos[0]
            if suma is None:
                return "0"
            else:
                return str(suma)
        except Exception as ex:
            print(ex)

    def consulta_paciente(self):
        sql = "SELECT * FROM pacientes ORDER BY id ASC"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
    
    def buscar_paciente(self, documento):
        sql=f'SELECT id,Nombre,`Fecha de ingreso`,`Prevision de salud`,`Motivo de ingreso`,Derivacion,`Medico atencion`,Box FROM pacientes WHERE Rut="{documento}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
    
    def Rutspacientes(self):
        sql=f'SELECT Rut FROM pacientes'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
 
    def insertar_paciente(self,documento,nombre,fecha,prevision,motivo,derivacion,medico,box):
        
        sql=f'INSERT INTO `pacientes` (`Rut`, `Nombre`, `Fecha de ingreso`, `Prevision de salud`, `Motivo de ingreso`, `Derivacion`,`Medico atencion`,`Box`) VALUES ("{documento}", "{nombre}", "{fecha}", "{prevision}", "{motivo}", "{derivacion}","{medico}","{box}")'
        try:
            self.cursor.execute(sql)
            n = self.cursor.rowcount
            self.connection.commit()
            print("Datos Guardados Correctamente")
            return 1
        except Exception as ex:
            print(ex)
      
    def eliminar_paciente(self,documento):
        sql=f'DELETE FROM `pacientes` WHERE `Rut`="{documento}"'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se elimino correctamente el paciente")
            return 1
        except Exception as e:
            raise e  

    def modificar_paciente(self,documento,fecha,prevision,motivo,derivacion,medico,box):

        sql=f'UPDATE `pacientes` SET `Fecha de ingreso` = "{fecha}",`Prevision de salud` = "{prevision}", `Motivo de ingreso` = "{motivo}", `Derivacion` = "{derivacion}",`Medico atencion` = "{medico}",`Box` = "{box}" WHERE `Rut` = "{documento}"'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se modifico correctamente [fecha,prevision,sueldo,area,medico] ....")
            return 1
        except Exception as e:
            raise e
        
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
 #----------------------------------------------------------------------------------PAGO MEDICOS----------------------------------------------------------------------------------  
    def descuento_AFP_medico(self,rut):
        sql=f'SELECT `Sueldo bruto`*0.1  FROM `medico` WHERE Rut="{rut}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            valor = int(datos[0])
        except Exception as ex:
            print(ex)
        return valor 
    
    def descuento_Salud_medico(self,rut):
        sql=f'SELECT `Sueldo bruto`*0.07  FROM `medico` WHERE Rut="{rut}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            valor  = int(datos[0])
        except Exception as ex:
            print(ex)
        return valor 
    
    def bonificacion_20años_medico(self,rut):
        sql=f'SELECT DATEDIFF(CURRENT_DATE, `Fecha de ingreso`) / 365  FROM medico WHERE Rut="{rut}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            valor = int(datos[0])
            if(valor >=20):
                sql2=f'SELECT `Sueldo bruto`*0.05  FROM `medico` WHERE Rut="{rut}"'
                self.cursor.execute(sql2)
                datos2 = self.cursor.fetchone()
                valor2 = int(datos2[0])
            else:
                valor2=0

        except Exception as ex:
            print(ex)
        return valor2
    
    def bonificacion_30años_medico(self,rut):
        sql=f'SELECT DATEDIFF(CURRENT_DATE, `Fecha de ingreso`) / 365  FROM medico WHERE Rut="{rut}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            valor = int(datos[0])
            if(valor >=30):
                sql2=f'SELECT `Sueldo bruto`*0.07  FROM `medico` WHERE Rut="{rut}"'
                self.cursor.execute(sql2)
                datos2 = self.cursor.fetchone()
                valor2 = int(datos2[0])
            else:
                valor2=0

        except Exception as ex:
            print(ex)
        return valor2
    
    def bonificacion_medico(self,rut):
        sql=f'SELECT `Sueldo bruto`*0.05  FROM `medico` WHERE Rut="{rut}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            valor  = int(datos[0])
        except Exception as ex:
            print(ex)
        return valor
    
    def descuentos_medicos(self,rut):
        descuentos=0
        descuentos+=self.descuento_AFP_medico(rut)
        descuentos+=self.descuento_Salud_medico(rut)
        return descuentos
    
    def beneficios_medicos(self,rut):
        beneficios=0
        beneficios+=self.bonificacion_20años_medico(rut)
        beneficios+=self.bonificacion_30años_medico(rut)
        beneficios+=self.bonificacion_medico(rut)
        return beneficios
    
    def sueldo_liquido_medicos(self,rut):
        sueldo=abs(self.beneficios_medicos(rut)-self.descuentos_medicos(rut))
        return sueldo
    
#----------------------------------------------------------------------------------PAGO TENS----------------------------------------------------------------------------------  

    def descuento_AFP_tens(self,rut):
        sql=f'SELECT `Sueldo bruto`*0.1  FROM `tens` WHERE Rut="{rut}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            valor = int(datos[0])
        except Exception as ex:
            print(ex)
        return valor 
    
    def descuento_Salud_tens(self,rut):
        sql=f'SELECT `Sueldo bruto`*0.07  FROM `tens` WHERE Rut="{rut}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            valor  = int(datos[0])
        except Exception as ex:
            print(ex)
        return valor 
    
    def bonificacion_20años_tens(self,rut):
        sql=f'SELECT DATEDIFF(CURRENT_DATE, `Fecha de ingreso`) / 365  FROM tens WHERE Rut="{rut}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            valor = int(datos[0])
            if(valor >=20):
                sql2=f'SELECT `Sueldo bruto`*0.05  FROM `tens` WHERE Rut="{rut}"'
                self.cursor.execute(sql2)
                datos2 = self.cursor.fetchone()
                valor2 = int(datos2[0])
            else:
                valor2=0

        except Exception as ex:
            print(ex)
        return valor2
    
    def bonificacion_30años_tens(self,rut):
        sql=f'SELECT DATEDIFF(CURRENT_DATE, `Fecha de ingreso`) / 365  FROM tens WHERE Rut="{rut}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            valor = int(datos[0])
            if(valor >=30):
                sql2=f'SELECT `Sueldo bruto`*0.07  FROM `tens` WHERE Rut="{rut}"'
                self.cursor.execute(sql2)
                datos2 = self.cursor.fetchone()
                valor2 = int(datos2[0])
            else:
                valor2=0

        except Exception as ex:
            print(ex)
        return valor2
    
    def bonificacion_tens(self,rut):
        sql=f'SELECT `Sueldo bruto`*0.05  FROM `tens` WHERE Rut="{rut}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            valor  = int(datos[0])
        except Exception as ex:
            print(ex)
        return valor
    
    def descuentos_tens(self,rut):
        descuentos=0
        descuentos+=self.descuento_AFP_tens(rut)
        descuentos+=self.descuento_Salud_tens(rut)
        return descuentos
    
    def beneficios_tens(self,rut):
        beneficios=0
        beneficios+=self.bonificacion_20años_tens(rut)
        beneficios+=self.bonificacion_30años_tens(rut)
        beneficios+=self.bonificacion_tens(rut)
        return beneficios
    
    def sueldo_liquido_tens(self,rut):
        sueldo=abs(self.beneficios_tens(rut)-self.descuentos_tens(rut))
        return sueldo
#----------------------------------------------------------------------------------PAGO ADMINISTRATIVO----------------------------------------------------------------------------------  
    def descuento_AFP_administrativo(self,rut):
        sql=f'SELECT `Sueldo bruto`*0.1  FROM `personal administrativo` WHERE Rut="{rut}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            valor = int(datos[0])
        except Exception as ex:
            print(ex)
        return valor 
    
    def descuento_Salud_administrativo(self,rut):
        sql=f'SELECT `Sueldo bruto`*0.07  FROM `personal administrativo` WHERE Rut="{rut}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            valor  = int(datos[0])
        except Exception as ex:
            print(ex)
        return valor 
    
    def bonificacion_20años_administrativo(self,rut):
        sql=f'SELECT DATEDIFF(CURRENT_DATE, `Fecha de ingreso`) / 365  FROM `personal administrativo` WHERE Rut="{rut}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            valor = int(datos[0])
            if(valor >=20):
                sql2=f'SELECT `Sueldo bruto`*0.05  FROM `personal administrativo` WHERE Rut="{rut}"'
                self.cursor.execute(sql2)
                datos2 = self.cursor.fetchone()
                valor2 = int(datos2[0])
            else:
                valor2=0

        except Exception as ex:
            print(ex)
        return valor2
    
    def bonificacion_30años_administrativo(self,rut):
        sql=f'SELECT DATEDIFF(CURRENT_DATE, `Fecha de ingreso`) / 365  FROM `personal administrativo` WHERE Rut="{rut}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            valor = int(datos[0])
            if(valor >=30):
                sql2=f'SELECT `Sueldo bruto`*0.07  FROM `personal administrativo` WHERE Rut="{rut}"'
                self.cursor.execute(sql2)
                datos2 = self.cursor.fetchone()
                valor2 = int(datos2[0])
            else:
                valor2=0

        except Exception as ex:
            print(ex)
        return valor2
    
    def bonificacion_administrativo(self,rut):
        sql=f'SELECT `Sueldo bruto`*0.03  FROM `personal administrativo` WHERE Rut="{rut}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            valor  = int(datos[0])
        except Exception as ex:
            print(ex)
        return valor
    
    def descuentos_administrativo(self,rut):
        descuentos=0
        descuentos+=self.descuento_AFP_administrativo(rut)
        descuentos+=self.descuento_Salud_administrativo(rut)
        return descuentos
    
    def beneficios_administrativo(self,rut):
        beneficios=0
        beneficios+=self.bonificacion_20años_administrativo(rut)
        beneficios+=self.bonificacion_30años_administrativo(rut)
        beneficios+=self.bonificacion_administrativo(rut)
        return beneficios
    
    def sueldo_liquido_administrativo(self,rut):
        sueldo=abs(self.beneficios_administrativo(rut)-self.descuentos_administrativo(rut))
        return sueldo
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    def insertar_pagopersonal(self,documento,nombre,sueldo,cargo,descuentos,beneficios,liquido):
        
        sql=f'INSERT INTO `pago personal` (`Rut`,`Nombre`, `Sueldo bruto`, `Cargo`,`Descuentos`,`Bonificaciones`,`Sueldo liquido`) VALUES ("{documento}","{nombre}", "{sueldo}", "{cargo}","{descuentos}", "{beneficios}", "{liquido}")'
        try:
            self.cursor.execute(sql)
            n = self.cursor.rowcount
            self.connection.commit()
            print("Datos Guardados Correctamente")
            return 1
        except Exception as ex:
            print(ex)
        return n
    
    def Rutspagopersonal(self):
        sql=f'SELECT Rut FROM `pago personal`'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
    
    def SueldoRut(self,rut):
        sql=f'SELECT `Sueldo liquido` FROM `pago personal` WHERE Rut="{rut}"' 
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
        except Exception as ex:
            print(ex)
        return datos[0]
    
    def SueldoNombre(self,rut):
        sql=f'SELECT `Nombre` FROM `pago personal` WHERE Rut="{rut}"' 
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
        except Exception as ex:
            print(ex)
        return datos[0]
#----------------------------------------------------------------------------------SQL COBRO PACIENTE----------------------------------------------------------------------------------  
class Cobro_paciente(DataBase):

    def consulta_cobro_paciente(self):
        sql = "SELECT * FROM `cobro paciente` ORDER BY id ASC"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
    
    def buscar_cobro_paciente(self, documento):
        sql=f'SELECT id,Nombre,`Prevision de salud`,Derivacion,Dias,Cobro,Descuento,`Cobro total` FROM `cobro paciente` WHERE Rut="{documento}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
        
    def insertar_cobro_paciente(self,rut,nombre,prevision,derivacion,dias,cobro,descuento,total):
        
        sql=f'INSERT INTO `cobro paciente` (`Rut`, `Nombre`, `Prevision de salud` , `Derivacion`, `Dias`,`Cobro`,`Descuento`,`Cobro total`) VALUES ("{rut}", "{nombre}", "{prevision}", "{derivacion}", "{dias}", "{cobro}","{descuento}","{total}")'
        try:
            self.cursor.execute(sql)
            n = self.cursor.rowcount
            self.connection.commit()
            print("Datos Guardados Correctamente")
            return 1
        except Exception as ex:
            print(ex)
        return n
      
    def eliminar_cobro_paciente(self,rut):
        sql=f'DELETE FROM `cobro paciente` WHERE `Rut`="{rut}"'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se elimino correctamente el personal")
            return 1
        except Exception as e:
            raise e  

    def modificar_cobro_paciente(self,rut,prevision,derivacion,dias,cobro,descuento,total):

        sql=f'UPDATE `cobro paciente` SET `Prevision de salud` = "{prevision}", `Derivacion` = "{derivacion}", `Dias` = "{dias}",`Cobro` = "{cobro}",Descuento = "{descuento}",`Cobro total` = "{total}" WHERE `Rut` = "{rut}"'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se modifico correctamente...")
            return 1
        except Exception as e:
            raise e
        
    def cobro_consulta(self,rut):
        sql=f'SELECT Derivacion FROM pacientes WHERE Rut="{rut}"' 
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            if(datos[0]=="Consulta medica"):
                pago=20000
                sql2=f'SELECT DATEDIFF(CURDATE(), `Fecha de ingreso`) FROM `pacientes` WHERE Rut="{rut}"'
                self.cursor.execute(sql2)
                datos2 = self.cursor.fetchone()
                if(datos2[0]<=0):
                    return pago
                else:
                    valor2 = int(datos2[0])*25000
                    pago+=valor2
                    return int(pago)
            else:
                pago=35000
                return int(pago)
        except Exception as ex:
            print(ex)

    def descuento_prevision(self,rut):
        sql=f'SELECT `Prevision de salud` FROM pacientes WHERE Rut="{rut}"' 
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            if(datos[0]=="Fonasa"):
                cobro=self.cobro_consulta(rut)
                descuento=cobro *0.25
                return int(descuento)
            elif(datos[0]=="Isapre"):
                cobro=self.cobro_consulta(rut)
                descuento=cobro *0.2
                return int(descuento)
            else:
                return 0
        except Exception as ex:
            print(ex)
            
    def cobro_total(self,rut):
        total=self.cobro_consulta(rut)-self.descuento_prevision(rut)
        return total
    
    def CobroRut(self,rut):
        sql=f'SELECT `Cobro total` FROM `cobro paciente` WHERE Rut="{rut}"' 
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
        except Exception as ex:
            print(ex)
        return datos[0]
    
    def dias(self,rut):
        sql=f'SELECT DATEDIFF(CURDATE(), `Fecha de ingreso`) FROM `pacientes` WHERE Rut="{rut}"' 
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            dias = int(datos[0])
            if(dias<=0):
                return 0
            else:
                return int(dias)
        except Exception as ex:
            print(ex)
            
    def cobroNombre(self,rut):
        sql=f'SELECT `Nombre` FROM `cobro paciente` WHERE Rut="{rut}"' 
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
        except Exception as ex:
            print(ex)
        return datos[0]
    
    def Rutscobropacientes(self):
        sql=f'SELECT Rut FROM `cobro paciente`'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
#----------------------------------------------------------------------------------SQL BUSQUEDAS----------------------------------------------------------------------------------  
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
      

