import re
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ConsultasSQL import *
from tkcalendar import DateEntry
from datetime import datetime
from time import strftime
import pandas as pd
#----------------------------------------------------------------------------------VENTANA CONTROL----------------------------------------------------------------------------------  
class Ventana_Control(Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión Hospital Copiapó")
        self.geometry("1920x1080")
        self.frame_actual = None
        self.mostrar_interfaz()
        self.Menus()

    def Menus(self):

        menubar = Menu(self)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Médicos y tens", command=self.mostrar_ventana_medicos_tens)
        file_menu.add_command(label="Personal administrativo", command=self.mostrar_ventana_personal)
        file_menu.add_command(label="Pago de personal", command=self.mostrar_ventana_pago_personal)
        file_menu.add_command(label="Pacientes", command=self.mostrar_ventana_pacientes)
        file_menu.add_command(label="Cobro paciente", command=self.mostrar_ventana_cobro_paciente)
        file_menu.add_command(label="Búsquedas de sueldos y fechas ", command=self.mostrar_ventana_busquedas1)
        file_menu.add_command(label="Búsquedas de medicos,Tens y personal", command=self.mostrar_ventana_busquedas2)
        file_menu.add_command(label="Búsquedas de pacientes", command=self.mostrar_ventana_busquedas3)
        file_menu.add_command(label="Volver al menu", command=self.mostrar_interfaz)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.salir)
        menubar.add_cascade(label="Opciones del menu", menu=file_menu)
        self.config(menu=menubar)

    def mostrar_interfaz(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()

        self.frame_actual = Ventana_Principal(self)

    def mostrar_ventana_medicos_tens(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()

        self.frame_actual = Ventana_medicos_tens(self)

    def mostrar_ventana_pacientes(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()

        self.frame_actual = Ventana_pacientes(self)

    def mostrar_ventana_personal(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()

        self.frame_actual = Ventana_personal(self)

    def mostrar_ventana_pago_personal(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()

        self.frame_actual = Ventana_pago_personal(self)
    
    def mostrar_ventana_cobro_paciente(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()
        self.frame_actual = Ventana_cobro_paciente(self)

    def mostrar_ventana_busquedas1(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()
        self.frame_actual = Ventana_Busquedas_1(self)
    
    def mostrar_ventana_busquedas2(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()
        self.frame_actual = Ventana_Busquedas_2(self)

    def mostrar_ventana_busquedas3(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()
        self.frame_actual = Ventana_Busquedas_3(self)

    def salir(self):
        if messagebox.askokcancel("Salir", "¿Estás seguro de que deseas salir?"):
            self.destroy()
#----------------------------------------------------------------------------------VENTANA BOTONES----------------------------------------------------------------------------------  
class Ventana_Principal(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1920, height=1080)
        self.master = master
        self.pack()
        self.Crear_Botones()

    def Crear_Botones(self):
        frame1 = Frame(self, bg="#40E0D0")
        frame1.place(x=0, y=0, width=1920, height=1080)

        titulo=Label(frame1,text="Gestión Administrativa",bg="#40E0D0",fg="#000000",font=("Garamond",35,"bold"))
        titulo.place(x=0,y=0,width=1980, height=100)

        titulo2=Label(frame1,text="Hospital San José del Carmen",bg="#40E0D0",fg="#000000",font=("Garamond",35,"bold"))
        titulo2.place(x=0,y=70,width=1980, height=80)

        self.btnMedicoTens = Button(frame1, text="Gestionar médicos y tens",command=self.master.mostrar_ventana_medicos_tens, bg="#000000", fg="white")
        self.btnMedicoTens.place(x=850, y=200, width=200, height=30)

        self.btnPersonal = Button(frame1, text="Gestionar personal",command=self.master.mostrar_ventana_personal, bg="#000000", fg="white")
        self.btnPersonal.place(x=850, y=300, width=200, height=30)

        self.btnPacientes = Button(frame1, text="Gestionar pacientes",command=self.master.mostrar_ventana_pacientes, bg="#000000", fg="white")
        self.btnPacientes.place(x=850, y=400, width=200, height=30)

        self.btnPagopersonal = Button(frame1, text="Gestionar pago de personal",command=self.master.mostrar_ventana_pago_personal, bg="#000000", fg="white")
        self.btnPagopersonal.place(x=850, y=500, width=200, height=30)

        self.btnPagopacientes = Button(frame1, text="Gestionar cobro pacientes",command=self.master.mostrar_ventana_cobro_paciente, bg="#000000", fg="white")
        self.btnPagopacientes.place(x=850, y=600, width=200, height=30)

        self.btnconsultas = Button(frame1, text="Búsquedas de sistema 1",command=self.master.mostrar_ventana_busquedas1, bg="#000000", fg="white")
        self.btnconsultas.place(x=850, y=700, width=200, height=30)

        self.btnconsultas2 = Button(frame1, text="Búsquedas de sistema 2",command=self.master.mostrar_ventana_busquedas2, bg="#000000", fg="white")
        self.btnconsultas2.place(x=850, y=800, width=200, height=30)

        self.btnconsultas3 = Button(frame1, text="Búsquedas de sistema 3",command=self.master.mostrar_ventana_busquedas3, bg="#000000", fg="white")
        self.btnconsultas3.place(x=850, y=900, width=200, height=30)           
#--------------------------------------------------------------------------VENTANA MEDICOS Y TENS----------------------------------------------------------------------------------  
class Ventana_medicos_tens(Frame):
    
    medicos=Medicos()
    tens=Tens()
    pago_personal=PagoPersonal()

    def __init__(self, master=None):
        super().__init__(master,width=1920, height=1080)
        self.master = master
        self.pack()
        self.CrearFrames()
        self.llenaDatos()
        self.habilitarCajas("disabled")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")
        self.llenaDatostens()
        self.habilitarCajastens("disabled")  
        self.habilitarBtnOpertens("normal")
        self.habilitarBtnGuardartens("disabled")   
        self.id=-1

    def validar_sueldo(self,sueldo):
        if(int(sueldo)<=0):
            return False
        return True
    
    def validar_nombre(self,nombre):
        patron = r'^[a-zA-Z\s]+$'
        if re.match(patron, nombre):
            return True
        else:
            return False
    
    def validarFecha(self,fecha):
        fecha_seleccionada = datetime.strptime(fecha, "%Y-%m-%d")
        fecha_actual = datetime.now()

        if fecha_seleccionada > fecha_actual:
            return False
        else:
            return True
#--------------------------------------------------------------------------ACCIONES FRAME 1----------------------------------------------------------------------------------  
    def habilitarCajas(self,estado):
        self.etRut.configure(state=estado)
        self.etNombre.configure(state=estado)
        self.etFecha.configure(state=estado)
        self.etPrevision.configure(state=estado)
        self.etSueldo.configure(state=estado)
        self.etEspecialidad.configure(state=estado)

    def habilitarBtnOper(self,estado):
        self.btnNuevo.configure(state=estado)                
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)

    def habilitarBtnGuardar(self,estado):
        self.btnGuardar.configure(state=estado)                
        self.btnCancelar.configure(state=estado) 

    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

    def limpiarCajas(self):
        self.etRut.delete(0,END)
        self.etNombre.delete(0,END)
        self.etFecha.delete(0,END)
        self.etPrevision.delete(0,END)
        self.etSueldo.delete(0,END)
        self.etEspecialidad.delete(0,END)
    
    def llenaDatos(self):
        datos = self.medicos.consulta_medicos()        
        for row in datos:            
            self.grid.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6]))

    def Nuevo(self):
        self.limpiarCajas()         
        self.habilitarCajas("normal")  
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.etPrevision.configure(state="readonly")
        self.etFecha.configure(state="readonly")
        self.etEspecialidad.configure(state="readonly") 
        self.limpiarCajas()

    def validar_valores_medicos(self):
        if not self.etNombre.get() or not self.etRut.get() or not self.etFecha.get() or not self.etPrevision.get() or not self.etSueldo.get() or not self.etEspecialidad.get():
            return False
        return True
        
    def Guardar(self):
        if(self.validar_valores_medicos()): 
            if self.id ==-1:
                if(self.validarFecha(self.etFecha.get())):
                    if(self.validar_nombre(self.etNombre.get())):
                        if(self.validar_sueldo(self.etSueldo.get())):
                            if(self.medicos.insertar_medico(self.etRut.get(),self.etNombre.get(),self.etFecha.get(),self.etPrevision.get(),self.etSueldo.get(),self.etEspecialidad.get())==1):
                                datos=self.medicos.Ruts()
                                self.etBuscar.configure(values=datos)
                                self.pago_personal.insertar_pagopersonal(self.etRut.get(),self.etNombre.get(),self.etSueldo.get(),"Medico",self.pago_personal.descuentos_medicos(self.etRut.get()),self.pago_personal.beneficios_medicos(self.etRut.get()),int(self.etSueldo.get())-int(self.pago_personal.sueldo_liquido_medicos(self.etRut.get())))            
                                messagebox.showinfo("Guardar", 'Elemento guardado correctamente.')
                                self.etRut.configure(state="normal")
                                self.etNombre.configure(state="normal")
                                self.etPrevision.configure(state="normal")
                                self.etFecha.configure(state="normal")
                                self.etEspecialidad.configure(state="normal") 
                                self.limpiaGrid()
                                self.llenaDatos() 
                                self.limpiarCajas() 
                                self.habilitarBtnGuardar("disabled")      
                                self.habilitarBtnOper("normal")
                                self.habilitarCajas("disabled")
                            else:
                                messagebox.showinfo("Guardar", "No fue posible guardar el elemento.")
                        else:
                            messagebox.showinfo("ERROR", "Ingrese un sueldo mayor a 0.")
                    else:
                        messagebox.showinfo("ERROR", "Ingrese un nombre alfabético.")
                else:
                    messagebox.showinfo("ERROR", "Fecha seleccionada no puede ser futura.")
            else:
                if(self.validarFecha(self.etFecha.get())):
                    if(self.validar_nombre(self.etNombre.get())):
                        if(self.validar_sueldo(self.etSueldo.get())):

                            if(self.medicos.modificar_medicos(self.etRut.get(),self.etFecha.get(),self.etPrevision.get(),self.etSueldo.get(),self.etEspecialidad.get())==1):
                                self.id = -1
                                self.pago_personal.modificar_pagopersonal(self.etRut.get(),self.etSueldo.get(),self.pago_personal.descuentos_medicos(self.etRut.get()),self.pago_personal.beneficios_medicos(self.etRut.get()),int(self.etSueldo.get())-int(self.pago_personal.sueldo_liquido_medicos(self.etRut.get())))
                                messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
                                self.etRut.configure(state="normal")
                                self.etNombre.configure(state="normal")
                                self.etPrevision.configure(state="normal")
                                self.etFecha.configure(state="normal")
                                self.etEspecialidad.configure(state="normal") 
                                self.limpiaGrid()
                                self.llenaDatos() 
                                self.limpiarCajas() 
                                self.habilitarBtnGuardar("disabled")      
                                self.habilitarBtnOper("normal")
                                self.habilitarCajas("disabled")
                            else:
                                messagebox.showinfo("Modificar", "No fue posible modificar el elemento")
                        else:
                            messagebox.showinfo("ERROR", "Ingrese un sueldo mayor a 0")
                    else:
                        messagebox.showinfo("ERROR", "Ingrese un nombre alfabético")
                else:
                    messagebox.showinfo("ERROR", "Fecha seleccionada no puede ser futura.")
        else:
            messagebox.showwarning("Guardar", "Debes completar todos los campos")
         
    def Modificar(self):        
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id= clave  
            self.habilitarCajas("normal")                         
            valores = self.grid.item(selected,'values')
            self.limpiarCajas()
            self.etRut.insert(0,valores[0])
            self.etNombre.insert(0,valores[1])
            self.etFecha.insert(0,valores[2])
            self.etRut.configure(state="disabled")
            self.etNombre.configure(state="disabled")         
            self.etPrevision.insert(0,valores[3])
            self.etSueldo.insert(0,valores[4]) 
            self.etEspecialidad.insert(0,valores[5])
            self.etPrevision.configure(state="readonly")
            self.etFecha.configure(state="readonly")
            self.etEspecialidad.configure(state="readonly")   
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")

    def Eliminar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid.item(selected,'values')
            print(valores[0])
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            respuesta = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if respuesta == messagebox.YES:
                n = self.medicos.eliminar_medico(valores[0])
                self.pago_personal.eliminar_pago_personal(valores[0])
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatos()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')

    def Cancelar(self):
        r = messagebox.askquestion("Cancelar", "Esta seguro que desea cancelar la operación actual.")
        if r == messagebox.YES:
            self.etRut.configure(state="normal")
            self.etNombre.configure(state="normal")
            self.etPrevision.configure(state="normal")
            self.etFecha.configure(state="normal")
            self.etEspecialidad.configure(state="normal")
            self.limpiarCajas() 
            self.habilitarBtnGuardar("disabled")      
            self.habilitarBtnOper("normal")
            self.habilitarCajas("disabled")
            self.limpiarCajas()
            
    def Exel_Medico(self):
        datos=self.medicos.consulta_medicos()
        i=-1
        id,rut,nombre,fecha,prevision,sueldo,especialidad= [],[],[],[],[],[],[]
        for dato in datos:
            i=i+1
            id.append(datos[i][0])
            rut.append(datos[i][1])
            nombre.append(datos[i][2])
            fecha.append(datos[i][3])
            prevision.append(datos[i][4])
            sueldo.append(datos[i][5])
            especialidad.append(datos[i][6])

        fecha_archivo=str(strftime('%d-%m-%y_%H-%M-%S'))
        datos2={'Id': id,'Rut': rut,'Nombre': nombre,'Fecha de ingreso': fecha,'Prevision de salud': prevision,'Sueldo bruto': sueldo,'Especialidad': especialidad}
        df=pd.DataFrame(datos2)
        df.to_excel(rf'C:\Users\vicen\Desktop\Hospital-Regional-Copiapo\Excel\Datos_Medicos_{fecha_archivo}.xlsx')
        messagebox.showinfo('Informacion','Excel creado correctamente')

#--------------------------------------------------------------------------ACCIONES FRAME 2----------------------------------------------------------------------------------  
                         
    def habilitarCajastens(self,estado):
        self.etRut2.configure(state=estado)
        self.etNombre2.configure(state=estado)
        self.etFecha2.configure(state=estado)
        self.etPrevision2.configure(state=estado)
        self.etSueldo2.configure(state=estado)
        self.etArea.configure(state=estado)

    def habilitarBtnOpertens(self,estado):
        self.btnNuevo2.configure(state=estado)                
        self.btnModificar2.configure(state=estado)
        self.btnEliminar2.configure(state=estado)

    def habilitarBtnGuardartens(self,estado):
        self.btnGuardar2.configure(state=estado)                
        self.btnCancelar2.configure(state=estado) 

    def limpiaGridtens(self):
        for item in self.Tree2.get_children():
            self.Tree2.delete(item)

    def limpiarCajastens(self):
        self.etRut2.delete(0,END)
        self.etNombre2.delete(0,END)
        self.etFecha2.delete(0,END)
        self.etPrevision2.delete(0,END)
        self.etSueldo2.delete(0,END)
        self.etArea.delete(0,END)

    def llenaDatostens(self):
        datos = self.tens.consulta_tens()        
        for row in datos:            
            self.Tree2.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6]))
        
    def Nuevotens(self):
        self.limpiarCajastens()         
        self.habilitarCajastens("normal")  
        self.habilitarBtnOpertens("disabled")
        self.habilitarBtnGuardartens("normal")
        self.etPrevision2.configure(state="readonly")
        self.etFecha2.configure(state="readonly")
        self.etArea.configure(state="readonly")
        self.limpiarCajastens()

    def validar_valores_tens(self):
        if not self.etNombre2.get() or not self.etRut2.get() or not self.etFecha2.get() or not self.etPrevision2.get() or not self.etSueldo2.get() or not self.etArea.get():
            return False
        return True
    
    def Guardartens(self):
        if(self.validar_valores_tens()): 
            if self.id ==-1:
                if(self.validarFecha(self.etFecha2.get())):
                    if(self.validar_nombre(self.etNombre2.get())):
                        if(self.validar_sueldo(self.etSueldo2.get())):
                            if(self.tens.insertar_tens(self.etRut2.get(),self.etNombre2.get(),self.etFecha2.get(),self.etPrevision2.get(),self.etSueldo2.get(),self.etArea.get())==1):
                                datos=self.tens.Rutstens()
                                self.etBuscar2.configure(values=datos)
                                self.pago_personal.insertar_pagopersonal(self.etRut2.get(),self.etNombre2.get(),self.etSueldo2.get(),"Tens",self.pago_personal.descuentos_tens(self.etRut2.get()),self.pago_personal.beneficios_tens(self.etRut2.get()),int(self.etSueldo2.get())-int(self.pago_personal.sueldo_liquido_tens(self.etRut2.get())))            
                                messagebox.showinfo("Guardar", 'Elemento guardado correctamente.')
                                self.etRut2.configure(state="normal")
                                self.etNombre2.configure(state="normal")
                                self.etPrevision2.configure(state="normal")
                                self.etFecha2.configure(state="normal")
                                self.etArea.configure(state="normal") 
                                self.limpiaGridtens()
                                self.llenaDatostens() 
                                self.limpiarCajastens() 
                                self.habilitarBtnGuardartens("disabled")      
                                self.habilitarBtnOpertens("normal")
                                self.habilitarCajastens("disabled")
                            else:
                                messagebox.showinfo("Guardar", "No fue posible guardar el elemento.")
                        else:
                            messagebox.showinfo("ERROR", "Ingrese un sueldo mayor a 0.")
                    else:
                        messagebox.showinfo("ERROR", "Ingrese un nombre alfabético.")
                else:
                    messagebox.showinfo("ERROR", "Fecha seleccionada no puede ser futura.")
                    
            else:
                if(self.validarFecha(self.etFecha2.get())):
                    if(self.validar_nombre(self.etNombre2.get())):
                        if(self.validar_sueldo(self.etSueldo2.get())):
                            if(self.tens.modificar_tens(self.etRut2.get(),self.etFecha2.get(),self.etPrevision2.get(),self.etSueldo2.get(),self.etArea.get())==1):
                                self.id = -1
                                self.pago_personal.modificar_pagopersonal(self.etRut2.get(),self.etSueldo2.get(),self.pago_personal.descuentos_tens(self.etRut2.get()),self.pago_personal.beneficios_tens(self.etRut2.get()),int(self.etSueldo2.get())-int(self.pago_personal.sueldo_liquido_tens(self.etRut2.get())))
                                messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
                                self.etRut2.configure(state="normal")
                                self.etNombre2.configure(state="normal")
                                self.etPrevision2.configure(state="normal")
                                self.etFecha2.configure(state="normal")
                                self.etArea.configure(state="normal") 
                                self.limpiaGridtens()
                                self.llenaDatostens() 
                                self.limpiarCajastens() 
                                self.habilitarBtnGuardartens("disabled")      
                                self.habilitarBtnOpertens("normal")
                                self.habilitarCajastens("disabled")
                            else:
                                messagebox.showinfo("Modificar", "No fue posible modificar el elemento.")
                        else:
                            messagebox.showinfo("ERROR", "Ingrese un sueldo mayor a 0.")
                    else:
                        messagebox.showinfo("ERROR", "Ingrese un nombre alfabético.")
                else:
                    messagebox.showinfo("ERROR", "Fecha seleccionada no puede ser futura.")
        else:
            messagebox.showwarning("Guardar", "Debes completar todos los campos.")
                    
    def Modificartens(self):        
        selected = self.Tree2.focus()                               
        clave = self.Tree2.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id= clave  
            self.habilitarCajastens("normal")                         
            valores = self.Tree2.item(selected,'values')
            self.limpiarCajastens()
            self.etRut2.insert(0,valores[0])
            self.etNombre2.insert(0,valores[1])
            self.etFecha2.insert(0,valores[2])
            self.etRut2.configure(state="disabled")
            self.etNombre2.configure(state="disabled")         
            self.etPrevision2.insert(0,valores[3])
            self.etSueldo2.insert(0,valores[4]) 
            self.etArea.insert(0,valores[5])
            self.etPrevision2.configure(state="readonly")
            self.etFecha2.configure(state="readonly")
            self.etArea.configure(state="readonly")
            self.habilitarBtnOpertens("disabled")
            self.habilitarBtnGuardartens("normal")
            self.etPrevision2.focus()

    def Eliminartens(self):
        selected = self.Tree2.focus()                               
        clave = self.Tree2.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.Tree2.item(selected,'values')
            print(valores[0])
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            respuesta = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if respuesta == messagebox.YES:
                n = self.tens.eliminar_tens(valores[0])
                self.pago_personal.eliminar_pago_personal(valores[0])
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGridtens()
                    self.llenaDatostens()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')
                            
    def Cancelartens(self):
        respuesta = messagebox.askquestion("Cancelar", "Esta seguro que desea cancelar la operación actual.")
        if respuesta == messagebox.YES:
            self.etRut2.configure(state="normal")
            self.etNombre2.configure(state="normal")
            self.etPrevision2.configure(state="normal")
            self.etFecha2.configure(state="normal")
            self.etArea.configure(state="normal")
            self.limpiarCajastens() 
            self.habilitarBtnGuardartens("disabled")      
            self.habilitarBtnOpertens("normal")
            self.habilitarCajastens("disabled")

    def Exel_Tens(self):
        datos2=self.tens.consulta_tens()
        i=-1
        id,rut,nombre,fecha,prevision,sueldo,area= [],[],[],[],[],[],[]
        for dato in datos2:
            i=i+1
            id.append(datos2[i][0])
            rut.append(datos2[i][1])
            nombre.append(datos2[i][2])
            fecha.append(datos2[i][3])
            prevision.append(datos2[i][4])
            sueldo.append(datos2[i][5])
            area.append(datos2[i][6])

        fecha_archivo=str(strftime('%d-%m-%y_%H-%M-%S'))
        datosTens={'Id': id,'Rut': rut,'Nombre': nombre,'Fecha de ingreso': fecha,'Prevision de salud': prevision,'Sueldo bruto': sueldo,'Area': area}
        df2=pd.DataFrame(datosTens)
        df2.to_excel(rf'C:\Users\vicen\Desktop\n\Excel\Datos_Tens_{fecha_archivo}.xlsx')
        messagebox.showinfo('Informacion','Excel creado correctamente')

    def vaciararbolbuscarmedicos(self):
        for item in self.treebuscar.get_children():
            self.treebuscar.delete(item)

    def llenardatosBuscar(self):
        self.vaciararbolbuscarmedicos()
        datos = self.medicos.buscar_medico(self.etBuscar.get())        
        for row in datos:            
            self.treebuscar.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],))

    def vaciararbolbuscartens(self):
        for item in self.treebuscar2.get_children():
            self.treebuscar2.delete(item)

    def llenardatosBuscartens(self):
        self.vaciararbolbuscartens()
        datos = self.tens.buscar_tens(self.etBuscar2.get())        
        for row in datos:            
            self.treebuscar2.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],))

#------------------------------------------------------------------------METODO PARA CREAR FRAMES----------------------------------------------------------------------------------
    def CrearFrames(self):
#--------------------------------------------------------------------------FRAME 1 MEDICOS----------------------------------------------------------------------------------
        frame1=Frame(self,bg="#00BFFF")
        frame1.place(x=0,y=0,width=960, height=1080)

#--------------------------------------------------------------------------TITULO FRAME 1----------------------------------------------------------------------------------
        titulo=Label(frame1,text="Médicos",bg="#1E90FF",fg="#000000",font=("Garamond",30,"bold"))
        titulo.place(x=330,y=0,width=300, height=100)
#--------------------------------------------------------------------------BOTNES FRAME 1----------------------------------------------------------------------------------
        self.btnNuevo=Button(frame1,text="Nuevo", command=self.Nuevo, bg="#0000CD", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnNuevo.place(x=250,y=500,width=80, height=30 )  

        self.btnModificar=Button(frame1,text="Modificar", command=self.Modificar, bg="#0000CD", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnModificar.place(x=350,y=500,width=80, height=30)   

        self.btnEliminar=Button(frame1,text="Eliminar", command=self.Eliminar, bg="#0000CD", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnEliminar.place(x=450,y=500,width=80, height=30)    

        self.btnGuardar=Button(frame1,text="Guardar", command=self.Guardar, bg="#00FF7F", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnGuardar.place(x=550,y=500,width=80, height=30)

        self.btnCancelar=Button(frame1,text="Cancelar", command=self.Cancelar, bg="#FF0000", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnCancelar.place(x=650,y=500,width=80, height=30)

        self.btnExelMedico=Button(frame1,text="Crear Exel", command=self.Exel_Medico, bg="#0000CD", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnExelMedico.place(x=750,y=500,width=100, height=30)

#--------------------------------------------------------------------------FRAME1:FRAME BUSCAR----------------------------------------------------------------------------------
        framebuscar=Frame(frame1,bg="#0000FF")
        framebuscar.place(x=450,y=187,width=480, height=200)
        
        self.btnbuscar=Button(framebuscar,text="Buscar", command=self.llenardatosBuscar, bg="#4B0082", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnbuscar.place(relx=0.1,rely=0.1)

        datos=self.medicos.Ruts()
        self.etBuscar=ttk.Combobox(framebuscar,values=datos)
        self.etBuscar.place(relx=0.3,rely=0.1,relheight=0.1,relwidth=0.5)

        self.treebuscar=ttk.Treeview(framebuscar,columns=("col2","col3","col4","col5","col6"),height=3)
        self.treebuscar.column("#0",width=38,anchor=CENTER)
        self.treebuscar.column("col2",width=100, anchor=CENTER)
        self.treebuscar.column("col3",width=80, anchor=CENTER)
        self.treebuscar.column("col4",width=80, anchor=CENTER)
        self.treebuscar.column("col5",width=80, anchor=CENTER)
        self.treebuscar.column("col6",width=100, anchor=CENTER)  

        self.treebuscar.heading("#0", text="Id", anchor=CENTER)
        self.treebuscar.heading("col2", text="Nombre", anchor=CENTER)
        self.treebuscar.heading("col3", text="Fecha", anchor=CENTER)
        self.treebuscar.heading("col4", text="Previsión", anchor=CENTER)
        self.treebuscar.heading("col5", text="Sueldo", anchor=CENTER)
        self.treebuscar.heading("col6", text="Especialidad", anchor=CENTER)
        self.treebuscar.place(relx=0,rely=0.3)

#--------------------------------------------------------------------------VALORES DEL FRAME 1----------------------------------------------------------------------------------
        labelRut=Label(frame1,text="Rut",font=("Blue Fonte",12,"bold"))
        labelRut.place(x=70,y=150,width=150, height=20)
        self.etRut=Entry(frame1)
        self.etRut.place(x=250,y=150,width=180, height=20)

        labelNombre=Label(frame1,text="Nombre",font=("Blue Fonte",12,"bold"))
        labelNombre.place(x=70,y=200,width=150, height=20)
        self.etNombre=Entry(frame1)
        self.etNombre.place(x=250,y=200,width=180, height=20)

        labelFecha=Label(frame1,text="Fecha de ingreso",font=("Blue Fonte",12,"bold"))
        labelFecha.place(x=70,y=250,width=150, height=20)
        self.etFecha=DateEntry(frame1,width=12, background='darkblue', foreground='white', selectbackground='orange', date_pattern='y-mm-dd')
        self.etFecha.place(x=250,y=250,width=180, height=20)

        labelPrevision=Label(frame1,text="Previsión de salud",font=("Blue Fonte",12,"bold"))
        labelPrevision.place(x=70,y=300,width=150, height=20)
        self.etPrevision=ttk.Combobox(frame1,state="readonly",values=["Fonasa","Isapre","Particular"])
        self.etPrevision.place(x=250,y=300,width=180, height=20)

        labelSueldo=Label(frame1,text="Sueldo Bruto",font=("Blue Fonte",12,"bold"))
        labelSueldo.place(x=70,y=350,width=150, height=20)
        self.etSueldo=Entry(frame1)
        self.etSueldo.place(x=250,y=350,width=180, height=20)

        labelEspecialidad=Label(frame1,text="Especialidad",font=("Blue Fonte",12,"bold"))
        labelEspecialidad.place(x=70,y=400,width=150, height=20)
        self.etEspecialidad=ttk.Combobox(frame1,values=["Pediatria","Anestesiologia","Cardiologia","Gastroenterologia","Medicina General","Ginecologia","Obstetricia"])
        self.etEspecialidad.place(x=250,y=400,width=180, height=20)

#--------------------------------------------------------------------------ARBOL FRAME 1----------------------------------------------------------------------------------
        
        self.grid=ttk.Treeview(frame1, columns=("col1","col2","col3","col4","col5","col6"),height=20)
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=125, anchor=CENTER)
        self.grid.column("col2",width=125, anchor=CENTER)
        self.grid.column("col3",width=125, anchor=CENTER)
        self.grid.column("col4",width=125, anchor=CENTER)
        self.grid.column("col5",width=125, anchor=CENTER)
        self.grid.column("col6",width=125, anchor=CENTER)  

        self.grid.heading("#0", text="id", anchor=CENTER)
        self.grid.heading("col1", text="Rut", anchor=CENTER)
        self.grid.heading("col2", text="Nombre", anchor=CENTER)
        self.grid.heading("col3", text="Fecha de ingreso", anchor=CENTER)
        self.grid.heading("col4", text="Previsión de salud", anchor=CENTER)
        self.grid.heading("col5", text="Sueldo bruto", anchor=CENTER)
        self.grid.heading("col6", text="Especialidad", anchor=CENTER)                    
        self.grid.place(x=70,y=550)  

#--------------------------------------------------------------------------FRAME 2 TENS---------------------------------------------------------------------------------

        frame2=Frame(self,bg="#FFB6C1")
        frame2.place(x=960,y=0,width=960, height=1080)
#--------------------------------------------------------------------------TITULO FRAME 2----------------------------------------------------------------------------------
        titulo2=Label(frame2,text="Tens",bg="#D87093",fg="#000000",font=("Garamond",30,"bold"))
        titulo2.place(x=330,y=0,width=300, height=100)
        
#--------------------------------------------------------------------------BOTNES FRAME 2----------------------------------------------------------------------------------
        self.btnNuevo2=Button(frame2,text="Nuevo", command=self.Nuevotens, bg="#C71585", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnNuevo2.place(x=250,y=500,width=80, height=30 )  

        self.btnModificar2=Button(frame2,text="Modificar", command=self.Modificartens, bg="#C71585", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnModificar2.place(x=350,y=500,width=80, height=30)   

        self.btnEliminar2=Button(frame2,text="Eliminar", command=self.Eliminartens, bg="#C71585", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnEliminar2.place(x=450,y=500,width=80, height=30)    

        self.btnGuardar2=Button(frame2,text="Guardar", command=self.Guardartens, bg="#00FF7F", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnGuardar2.place(x=550,y=500,width=80, height=30)

        self.btnCancelar2=Button(frame2,text="Cancelar", command=self.Cancelartens, bg="#FF0000", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnCancelar2.place(x=650,y=500,width=80, height=30)
    
        self.btnExelTens=Button(frame2,text="Crear Exel", command=self.Exel_Tens, bg="#C71585", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnExelTens.place(x=750,y=500,width=100, height=30)

#--------------------------------------------------------------------------FRAME2:FRAME BUSCAR----------------------------------------------------------------------------------
        framebuscar2=Frame(frame2,bg="#DA70D6")
        framebuscar2.place(x=450,y=187,width=480, height=200)

        self.btnbuscar2=Button(framebuscar2,text="Buscar", command=self.llenardatosBuscartens, bg="#DC143C", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnbuscar2.place(relx=0.1,rely=0.1)
        datos=self.tens.Rutstens()
        self.etBuscar2=ttk.Combobox(framebuscar2,values=datos)
        self.etBuscar2.place(relx=0.3,rely=0.1,relheight=0.1,relwidth=0.5)

        self.treebuscar2=ttk.Treeview(framebuscar2,columns=("col2","col3","col4","col5","col6"),height=3)
        self.treebuscar2.column("#0",width=38,anchor=CENTER)
        self.treebuscar2.column("col2",width=100, anchor=CENTER)
        self.treebuscar2.column("col3",width=80, anchor=CENTER)
        self.treebuscar2.column("col4",width=80, anchor=CENTER)
        self.treebuscar2.column("col5",width=80, anchor=CENTER)
        self.treebuscar2.column("col6",width=100, anchor=CENTER) 

        self.treebuscar2.heading("#0", text="id", anchor=CENTER)
        self.treebuscar2.heading("col2", text="Nombre", anchor=CENTER)
        self.treebuscar2.heading("col3", text="Fecha", anchor=CENTER)
        self.treebuscar2.heading("col4", text="Previsión", anchor=CENTER)
        self.treebuscar2.heading("col5", text="Sueldo", anchor=CENTER)
        self.treebuscar2.heading("col6", text="Área", anchor=CENTER)
        self.treebuscar2.place(relx=0,rely=0.3)

#--------------------------------------------------------------------------VALORES FRAME 2----------------------------------------------------------------------------------
        labelRut2=Label(frame2,text="Rut",font=("Blue Fonte",12,"bold"))
        labelRut2.place(x=70,y=150,width=150, height=20)
        self.etRut2=Entry(frame2)
        self.etRut2.place(x=250,y=150,width=180, height=20)

        labelNombre2=Label(frame2,text="Nombre",font=("Blue Fonte",12,"bold"))
        labelNombre2.place(x=70,y=200,width=150, height=20)
        self.etNombre2=Entry(frame2)
        self.etNombre2.place(x=250,y=200,width=180, height=20)

        labelFecha2=Label(frame2,text="Fecha de ingreso",font=("Blue Fonte",12,"bold"))
        labelFecha2.place(x=70,y=250,width=150, height=20)
        self.etFecha2=DateEntry(frame2,width=12, background='darkblue', foreground='white', selectbackground='orange', date_pattern='y-mm-dd')
        self.etFecha2.place(x=250,y=250,width=180, height=20)

        labelPrevision2=Label(frame2,text="Previsión de salud",font=("Blue Fonte",12,"bold"))
        labelPrevision2.place(x=70,y=300,width=150, height=20)
        self.etPrevision2=ttk.Combobox(frame2,values=["Fonasa","Isapre","Particular"])
        self.etPrevision2.place(x=250,y=300,width=180, height=20)
        
        labelSueldo2=Label(frame2,text="Sueldo Bruto",font=("Blue Fonte",12,"bold"))
        labelSueldo2.place(x=70,y=350,width=150, height=20)
        self.etSueldo2=Entry(frame2)
        self.etSueldo2.place(x=250,y=350,width=180, height=20)

        labelArea=Label(frame2,text="Área que pertenece",font=("Blue Fonte",12,"bold"))
        labelArea.place(x=70,y=400,width=150, height=20)
        self.etArea=ttk.Combobox(frame2,values=["Consulta externa","Emergencia","Pediatria","Quirofano","Hospitalizacion","Recuperacion UCI"])
        self.etArea.place(x=250,y=400,width=180, height=20)

#-------------------------------------------------------------------------ARBOL FRAME 2----------------------------------------------------------------------------------
        self.Tree2=ttk.Treeview(frame2, columns=("col1","col2","col3","col4","col5","col6"),height=20)
        self.Tree2.column("#0",width=50)
        self.Tree2.column("col1",width=125, anchor=CENTER)
        self.Tree2.column("col2",width=125, anchor=CENTER)
        self.Tree2.column("col3",width=125, anchor=CENTER)
        self.Tree2.column("col4",width=125, anchor=CENTER)
        self.Tree2.column("col5",width=125, anchor=CENTER)  
        self.Tree2.column("col6",width=125, anchor=CENTER)

        self.Tree2.heading("#0", text="Id", anchor=CENTER)
        self.Tree2.heading("col1", text="Rut", anchor=CENTER)
        self.Tree2.heading("col2", text="Nombre", anchor=CENTER)
        self.Tree2.heading("col3", text="Fecha de ingreso", anchor=CENTER)
        self.Tree2.heading("col4", text="Previsión de salud", anchor=CENTER)
        self.Tree2.heading("col5", text="Sueldo bruto", anchor=CENTER)
        self.Tree2.heading("col6", text="Área que pertenece", anchor=CENTER)
        self.Tree2.place(x=70,y=550)

#--------------------------------------------------------------------------VENTANA PACIENTES----------------------------------------------------------------------------------
class Ventana_pacientes(Frame):

    medicos=Medicos()
    pacientes=Pacientes()
    cobro=Cobro_paciente()

    def __init__(self, master=None):
        super().__init__(master,width=1920, height=1080)
        self.master = master
        self.pack()
        self.CrearFrames()
        self.llenaDatos()
        self.habilitarCajas("disabled")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")  
        self.id=-1

    def habilitarCajas(self,estado):
        self.etRut.configure(state=estado)
        self.etNombre.configure(state=estado)
        self.etFecha.configure(state=estado)
        self.etPrevision.configure(state=estado)
        self.etMotivo.configure(state=estado)
        self.etDerivacion.configure(state=estado)
        self.etMedico.configure(state=estado)
       

    def habilitarBtnOper(self,estado):
        self.btnNuevo.configure(state=estado)                
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)

    def habilitarBtnGuardar(self,estado):
        self.btnGuardar.configure(state=estado)                
        self.btnCancelar.configure(state=estado) 

    def limpiaGrid(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def limpiarCajas(self):
        self.etRut.delete(0,END)
        self.etNombre.delete(0,END)
        self.etFecha.delete(0,END)
        self.etPrevision.delete(0,END)
        self.etMotivo.delete(0,END)
        self.etDerivacion.delete(0,END)
        self.etMedico.delete(0,END)
        
    def llenaDatos(self):
        datos = self.pacientes.consulta_paciente()        
        for row in datos:            
            self.tree.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6],row[7],row[8]))     

    def Nuevo(self):
        self.limpiarCajas()
        self.habilitarCajas("normal")
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.etPrevision.configure(state="readonly")
        self.etFecha.configure(state="readonly")
        self.etMotivo.configure(state="readonly")
        self.etDerivacion.configure(state="readonly")
        self.etMedico.configure(state="readonly")
        self.limpiarCajas()

    def validar_valores_pacientes(self):
        if not self.etNombre.get() or not self.etRut.get() or not self.etFecha.get() or not self.etPrevision.get() or not self.etMotivo.get() or not self.etDerivacion.get() or not self.etMedico.get():
            return False
        return True
    
    def validar_nombre(self,nombre):
        patron = r'^[a-zA-Z\s]+$'
        if re.match(patron, nombre):
            return True
        else:
            return False
        
    def validarFecha(self,fecha):
        fecha_seleccionada = datetime.strptime(fecha, "%Y-%m-%d")
        fecha_actual = datetime.now()

        if fecha_seleccionada > fecha_actual:
            return False
        else:
            return True
            
    def Guardar(self): 
        if(self.validar_valores_pacientes()): 
            if self.id ==-1:
                if(self.validarFecha(self.etFecha.get())):
                    if(self.validar_nombre(self.etNombre.get())):
                        if(self.etDerivacion.get()=="Consulta medica"):
                            if(self.pacientes.insertar_paciente(self.etRut.get(),self.etNombre.get(),self.etFecha.get(),self.etPrevision.get(),self.etMotivo.get(),self.etDerivacion.get(),self.etMedico.get(),0)==1):
                                self.cobro.insertar_cobro_paciente(self.etRut.get(),self.etNombre.get(),self.etPrevision.get(),self.etDerivacion.get(),self.cobro.dias(self.etRut.get()),self.cobro.cobro_consulta(self.etRut.get()),self.cobro.descuento_prevision(self.etRut.get()),self.cobro.cobro_total(self.etRut.get()))
                                datos=self.pacientes.Rutspacientes()
                                self.Box2.configure(text="Box ocupados:"+str(self.pacientes.suma_de_box()))
                                self.etBuscar.configure(values=datos)            
                                messagebox.showinfo("Guardar", 'Elemento guardado correctamente.')

                                self.etRut.configure(state="normal")
                                self.etNombre.configure(state="normal")
                                self.etPrevision.configure(state="normal")
                                self.etFecha.configure(state="normal")
                                self.etMotivo.configure(state="normal")
                                self.etDerivacion.configure(state="normal")
                                self.etMedico.configure(state="normal") 
                                self.limpiaGrid()
                                self.llenaDatos() 
                                self.limpiarCajas() 
                                self.habilitarBtnGuardar("disabled")      
                                self.habilitarBtnOper("normal")
                                self.habilitarCajas("disabled")
                            else:
                                messagebox.showinfo("Guardar", "No fue posible guardar el elemento.")
                        else:
                            if(int(self.pacientes.suma_de_box())<5):
                                if(self.pacientes.insertar_paciente(self.etRut.get(),self.etNombre.get(),self.etFecha.get(),self.etPrevision.get(),self.etMotivo.get(),self.etDerivacion.get(),"N/A",1)==1):
                                    self.cobro.insertar_cobro_paciente(self.etRut.get(),self.etNombre.get(),self.etPrevision.get(),self.etDerivacion.get(),self.cobro.dias(self.etRut.get()),self.cobro.cobro_consulta(self.etRut.get()),self.cobro.descuento_prevision(self.etRut.get()),self.cobro.cobro_total(self.etRut.get()))
                                    datos=self.pacientes.Rutspacientes()
                                    self.Box2.configure(text="Box ocupados:"+str(self.pacientes.suma_de_box()))
                                    self.etBuscar.configure(values=datos)            
                                    messagebox.showinfo("Guardar", 'Elemento guardado correctamente.')

                                    self.etRut.configure(state="normal")
                                    self.etNombre.configure(state="normal")
                                    self.etPrevision.configure(state="normal")
                                    self.etFecha.configure(state="normal")
                                    self.etMotivo.configure(state="normal")
                                    self.etDerivacion.configure(state="normal")
                                    self.etMedico.configure(state="normal") 
                                    self.limpiaGrid()
                                    self.llenaDatos() 
                                    self.limpiarCajas() 
                                    self.habilitarBtnGuardar("disabled")      
                                    self.habilitarBtnOper("normal")
                                    self.habilitarCajas("disabled")
                                else:
                                    messagebox.showinfo("Guardar", "No fue posible guardar el elemento.")
                            else:
                                respuesta= messagebox.askquestion("PROBLEMA", "Los box del hospital estan ocupados ¿Desea continuar?")
                                if(respuesta==messagebox.YES):
                                    if(self.pacientes.insertar_paciente(self.etRut.get(),self.etNombre.get(),self.etFecha.get(),self.etPrevision.get(),self.etMotivo.get(),self.etDerivacion.get(),"N/A",0)==1):
                                        self.cobro.insertar_cobro_paciente(self.etRut.get(),self.etNombre.get(),self.etPrevision.get(),self.etDerivacion.get(),self.cobro.dias(self.etRut.get()),self.cobro.cobro_consulta(self.etRut.get()),self.cobro.descuento_prevision(self.etRut.get()),self.cobro.cobro_total(self.etRut.get()))
                                        datos=self.pacientes.Rutspacientes()
                                        self.etBuscar.configure(values=datos)
                                        self.Box2.configure(text="Box ocupados:"+str(self.pacientes.suma_de_box()))            
                                        messagebox.showinfo("Guardar", 'Elemento guardado correctamente tendra que esperar box.')
                                        self.etRut.configure(state="normal")
                                        self.etNombre.configure(state="normal")
                                        self.etPrevision.configure(state="normal")
                                        self.etFecha.configure(state="normal")
                                        self.etMotivo.configure(state="normal")
                                        self.etDerivacion.configure(state="normal")
                                        self.etMedico.configure(state="normal") 
                                        self.limpiaGrid()
                                        self.llenaDatos() 
                                        self.limpiarCajas() 
                                        self.habilitarBtnGuardar("disabled")      
                                        self.habilitarBtnOper("normal")
                                        self.habilitarCajas("disabled")
                                    else:
                                        messagebox.showinfo("Guardar", "No fue posible guardar el elemento.")
                                else:
                                    messagebox.showinfo("Lo sentimos", "Elemento no guardado tendrá que esperar un box.")
                    else:
                        messagebox.showinfo("ERROR", "Ingrese un nombre alfabético.")
                else:
                    messagebox.showinfo("ERROR", "Fecha seleccionada no puede ser futura.")

            else:
                if(self.validarFecha(self.etFecha.get())):
                    if(self.validar_nombre(self.etNombre.get())):
                        if(self.etDerivacion.get()=="Consulta medica"):
                            if(self.pacientes.modificar_paciente(self.etRut.get(),self.etFecha.get(),self.etPrevision.get(),self.etMotivo.get(),self.etDerivacion.get(),self.etMedico.get(),0)==1):
                                self.cobro.modificar_cobro_paciente(self.etRut.get(),self.etPrevision.get(),self.etDerivacion.get(),self.cobro.dias(self.etRut.get()),self.cobro.cobro_consulta(self.etRut.get()),self.cobro.descuento_prevision(self.etRut.get()),self.cobro.cobro_total(self.etRut.get()))
                                self.id = -1
                                messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')

                                self.Box2.configure(text="Box ocupados:"+str(self.pacientes.suma_de_box()))
                                self.etRut.configure(state="normal")
                                self.etNombre.configure(state="normal")
                                self.etPrevision.configure(state="normal")
                                self.etFecha.configure(state="normal")
                                self.etMotivo.configure(state="normal")
                                self.etDerivacion.configure(state="normal")
                                self.etMedico.configure(state="normal") 
                                self.limpiaGrid()
                                self.llenaDatos() 
                                self.limpiarCajas() 
                                self.habilitarBtnGuardar("disabled")      
                                self.habilitarBtnOper("normal")
                                self.habilitarCajas("disabled")
                            else:
                                messagebox.showinfo("Modificar", "No fue posible modificar el elemento.")
                        else:
                            if(int(self.pacientes.suma_de_box())<5):
                                if(self.pacientes.modificar_paciente(self.etRut.get(),self.etFecha.get(),self.etPrevision.get(),self.etMotivo.get(),self.etDerivacion.get(),"N/A",1)==1):
                                    self.cobro.modificar_cobro_paciente(self.etRut.get(),self.etPrevision.get(),self.etDerivacion.get(),self.cobro.dias(self.etRut.get()),self.cobro.cobro_consulta(self.etRut.get()),self.cobro.descuento_prevision(self.etRut.get()),self.cobro.cobro_total(self.etRut.get()))
                                    messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
                                    self.Box2.configure(text="Box ocupados:"+str(self.pacientes.suma_de_box()))
                                    self.etRut.configure(state="normal")
                                    self.etNombre.configure(state="normal")
                                    self.etPrevision.configure(state="normal")
                                    self.etFecha.configure(state="normal")
                                    self.etMotivo.configure(state="normal")
                                    self.etDerivacion.configure(state="normal")
                                    self.etMedico.configure(state="normal") 
                                    self.limpiaGrid()
                                    self.llenaDatos() 
                                    self.limpiarCajas() 
                                    self.habilitarBtnGuardar("disabled")      
                                    self.habilitarBtnOper("normal")
                                    self.habilitarCajas("disabled")
                                else:
                                    messagebox.showinfo("Guardar", "No fue posible guardar el elemento.")
                            else:
                                respuesta= messagebox.askquestion("PROBLEMA", "Los box del hospital estan ocupados ¿Desea continuar?")
                                if(respuesta==messagebox.YES):
                                    if(self.pacientes.modificar_paciente(self.etRut.get(),self.etFecha.get(),self.etPrevision.get(),self.etMotivo.get(),self.etDerivacion.get(),"N/A",0)==1):
                                        self.cobro.modificar_cobro_paciente(self.etRut.get(),self.etPrevision.get(),self.etDerivacion.get(),self.cobro.dias(self.etRut.get()),self.cobro.cobro_consulta(self.etRut.get()),self.cobro.descuento_prevision(self.etRut.get()),self.cobro.cobro_total(self.etRut.get()))
                                        messagebox.showinfo("Guardar", 'Elemento guardado correctamente tendra que esperar box.')
                                        self.Box2.configure(text="Box ocupados:"+str(self.pacientes.suma_de_box()))
                                        self.etRut.configure(state="normal")
                                        self.etNombre.configure(state="normal")
                                        self.etPrevision.configure(state="normal")
                                        self.etFecha.configure(state="normal")
                                        self.etMotivo.configure(state="normal")
                                        self.etDerivacion.configure(state="normal")
                                        self.etMedico.configure(state="normal") 
                                        self.limpiaGrid()
                                        self.llenaDatos() 
                                        self.limpiarCajas() 
                                        self.habilitarBtnGuardar("disabled")      
                                        self.habilitarBtnOper("normal")
                                        self.habilitarCajas("disabled")
                                    else:
                                        messagebox.showinfo("Guardar", "No fue posible guardar el elemento.")
                                else:
                                    messagebox.showinfo("Lo sentimos", "Elemento no guardado,tendrá que esperar un box.")
                    else:
                        messagebox.showinfo("ERROR", "Ingrese un nombre alfabético.")
                else:
                    messagebox.showinfo("ERROR", "Fecha seleccionada no puede ser futura.")
        else:
            messagebox.showwarning("Guardar", "Debes completar todos los campos.")
                    
    def Modificar(self):        
        selected = self.tree.focus()                               
        clave = self.tree.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id= clave  
            self.habilitarCajas("normal")                         
            valores = self.tree.item(selected,'values')
            self.limpiarCajas()
            self.etRut.insert(0,valores[0])
            self.etNombre.insert(0,valores[1])
            self.etRut.configure(state="disabled")
            self.etNombre.configure(state="disabled") 
            self.etFecha.insert(0,valores[2])
            self.etPrevision.insert(0,valores[3])
            self.etMotivo.insert(0,valores[4]) 
            self.etDerivacion.insert(0,valores[5])
            self.etMedico.insert(0,valores[6])
            self.etPrevision.configure(state="readonly")
            self.etFecha.configure(state="readonly")
            self.etMotivo.configure(state="readonly")
            self.etDerivacion.configure(state="readonly")
            self.etMedico.configure(state="readonly")  
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")

    def Eliminar(self):
        selected = self.tree.focus()                               
        clave = self.tree.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.tree.item(selected,'values')
            print(valores[0])
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            respuesta = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if respuesta == messagebox.YES:
                n = self.pacientes.eliminar_paciente(valores[0])
                if n == 1:
                    self.cobro.eliminar_cobro_paciente(valores[0])
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.Box2.configure(text="Box ocupados:"+str(self.pacientes.suma_de_box()))
                    self.limpiaGrid()
                    self.llenaDatos()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')

    def Cancelar(self):
        r = messagebox.askquestion("Cancelar", "Esta seguro que desea cancelar la operación actual.")
        if r == messagebox.YES:
            self.etRut.configure(state="normal")
            self.etNombre.configure(state="normal")
            self.etPrevision.configure(state="normal")
            self.etFecha.configure(state="normal")
            self.etMotivo.configure(state="normal")
            self.etDerivacion.configure(state="normal")
            self.etMedico.configure(state="normal")
            self.limpiarCajas() 
            self.habilitarBtnGuardar("disabled")      
            self.habilitarBtnOper("normal")
            self.habilitarCajas("disabled")

    def vaciararbolbuscarpaciente(self):
        for item in self.treebuscar.get_children():
            self.treebuscar.delete(item)

    def llenardatosBuscarpaciente(self):
        self.vaciararbolbuscarpaciente()
        datos = self.pacientes.buscar_paciente(self.etBuscar.get())        
        for row in datos:            
            self.treebuscar.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6],row[7]))
    
    def Exel_Paciente(self):
        datos=self.pacientes.consulta_paciente()
        i=-1
        id,rut,nombre,fecha,prevision,motivo,derivacion,medico,box= [],[],[],[],[],[],[],[],[]
        for dato in datos:
            i=i+1
            id.append(datos[i][0])
            rut.append(datos[i][1])
            nombre.append(datos[i][2])
            fecha.append(datos[i][3])
            prevision.append(datos[i][4])
            motivo.append(datos[i][5])
            derivacion.append(datos[i][6])
            medico.append(datos[i][7])
            box.append(datos[i][8])

        fecha_archivo=str(strftime('%d-%m-%y_%H-%M-%S'))
        datos2={'Id': id,'Rut': rut,'Nombre': nombre,'Fecha de ingreso': fecha,'Prevision de salud': prevision,'Motivo de ingreso': motivo,'Derivacion': derivacion,'Medico que lo atendio': medico,'Box de atencion': box}
        df=pd.DataFrame(datos2)
        df.to_excel(rf'C:\Users\vicen\Desktop\n\Excel\Datos_Pacientes_{fecha_archivo}.xlsx')
        messagebox.showinfo('Informacion','Excel creado correctamente')
    

    def CrearFrames(self):

        frame1=Frame(self,bg="#90EE90")
        frame1.place(x=0,y=0,width=1920, height=1080)
#--------------------------------------------------------------------------TITULO----------------------------------------------------------------------------------
        titulo2=Label(frame1,text="Pacientes",bg="#32CD32",fg="#000000",font=("Garamond",30,"bold"))
        titulo2.place(x=860,y=0,width=250, height=60)
        
#--------------------------------------------------------------------------BOTONES----------------------------------------------------------------------------------
        self.btnNuevo=Button(frame1,text="Nuevo", command=self.Nuevo, bg="#CD853F", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnNuevo.place(x=660,y=520,width=80, height=30 )  

        self.btnModificar=Button(frame1,text="Modificar", command=self.Modificar, bg="#CD853F", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnModificar.place(x=760,y=520,width=80, height=30)   

        self.btnEliminar=Button(frame1,text="Eliminar", command=self.Eliminar, bg="#CD853F", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnEliminar.place(x=860,y=520,width=80, height=30)    

        self.btnGuardar=Button(frame1,text="Guardar", command=self.Guardar, bg="#228B22", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnGuardar.place(x=960,y=520,width=80, height=30)

        self.btnCancelar=Button(frame1,text="Cancelar", command=self.Cancelar, bg="#FF0000", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnCancelar.place(x=1060,y=520,width=80, height=30)

        self.btnExcel=Button(frame1,text="Crear Excel", command=self.Exel_Paciente,bg="#CD853F", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnExcel.place(x=1160,y=520,width=100, height=30)

#--------------------------------------------------------------------------VALORES----------------------------------------------------------------------------------
        labelRut=Label(frame1,text="Rut",font=("Blue Fonte",12,"bold"))
        labelRut.place(x=70,y=125,width=230, height=20)
        self.etRut=Entry(frame1)
        self.etRut.place(x=330,y=125,width=230, height=20)

        labelNombre=Label(frame1,text="Nombre",font=("Blue Fonte",12,"bold"))
        labelNombre.place(x=70,y=175,width=230, height=20)
        self.etNombre=Entry(frame1)
        self.etNombre.place(x=330,y=175,width=230, height=20)

        labelFecha=Label(frame1,text="Fecha de ingreso",font=("Blue Fonte",12,"bold"))
        labelFecha.place(x=70,y=225,width=230, height=20)
        self.etFecha=DateEntry(frame1,width=12, background='darkblue', foreground='white', selectbackground='orange', date_pattern='y-mm-dd')
        self.etFecha.place(x=330,y=225,width=230, height=20)

        labelPrevision=Label(frame1,text="Previsión de salud",font=("Blue Fonte",12,"bold"))
        labelPrevision.place(x=70,y=275,width=230, height=20)
        self.etPrevision=ttk.Combobox(frame1,values=["Fonasa","Isapre","Particular"])
        self.etPrevision.place(x=330,y=275,width=230, height=20)

        labelMotivo=Label(frame1,text="Motivo de ingreso",font=("Blue Fonte",12,"bold"))
        labelMotivo.place(x=70,y=325,width=230, height=20)
        self.etMotivo=ttk.Combobox(frame1,values=["Accidente","Fiebre","Herida","Fractura","Quemadura","Infección","Hemorragia","Desmayo","Alergia","Vómito","Infarto","Apéndice","Neumonía","Parto"])
        self.etMotivo.place(x=330,y=325,width=230, height=20)

        labelDerivacion=Label(frame1,text="Derivación",font=("Blue Fonte",12,"bold"))
        labelDerivacion.place(x=70,y=375,width=230, height=20)
        self.etDerivacion=ttk.Combobox(frame1,values=["Consulta medica","Urgencia"])
        self.etDerivacion.place(x=330,y=375,width=230, height=20)

        labelMedico=Label(frame1,text="Médico que lo atendió ",font=("Blue Fonte",12,"bold"))
        labelMedico.place(x=70,y=425,width=230, height=20)
        medicos=self.medicos.medico_paciente()
        self.etMedico=ttk.Combobox(frame1,values=medicos)
        self.etMedico.place(x=330,y=425,width=230, height=20)

#--------------------------------------------------------------------------ARBOL----------------------------------------------------------------------------------
        self.tree=ttk.Treeview(frame1, columns=("col1","col2","col3","col4","col5","col6","col7","col8"),height=20)
        self.tree.column("#0",width=50)
        self.tree.column("col1",width=125, anchor=CENTER)
        self.tree.column("col2",width=125, anchor=CENTER)
        self.tree.column("col3",width=125, anchor=CENTER)
        self.tree.column("col4",width=125, anchor=CENTER)
        self.tree.column("col5",width=125, anchor=CENTER)
        self.tree.column("col6",width=125, anchor=CENTER)
        self.tree.column("col7",width=250, anchor=CENTER)
        self.tree.column("col8",width=125, anchor=CENTER)   

        self.tree.heading("#0", text="id", anchor=CENTER)
        self.tree.heading("col1", text="Rut", anchor=CENTER)
        self.tree.heading("col2", text="Nombre", anchor=CENTER)
        self.tree.heading("col3", text="Fecha de ingreso", anchor=CENTER)
        self.tree.heading("col4", text="Prevision de salud", anchor=CENTER)
        self.tree.heading("col5", text="Motivo de ingreso", anchor=CENTER)
        self.tree.heading("col6", text="Derivacion", anchor=CENTER)
        self.tree.heading("col7", text="Medico atencion", anchor=CENTER)
        self.tree.heading("col8", text="Box de atencion", anchor=CENTER)                        
        self.tree.place(x=450,y=570) 
#--------------------------------------------------------------------------FRAME BUSCAR----------------------------------------------------------------------------------
        framebuscar=Frame(frame1,bg="#228B22")
        framebuscar.place(x=650,y=125,width=1000, height=350)
        
        self.btnbuscar=Button(framebuscar,text="Buscar", command=self.llenardatosBuscarpaciente, bg="#4B0082", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnbuscar.place(x=400,y=40,width=100,height=30)
        datos=self.pacientes.Rutspacientes()
        self.etBuscar=ttk.Combobox(framebuscar,values=datos)
        self.etBuscar.place(x=525,y=40,width=150,height=30)

        self.treebuscar=ttk.Treeview(framebuscar,columns=("col2","col3","col4","col5","col6","col7","col8"),height=1)
        self.treebuscar.column("#0",width=38,anchor=CENTER)
        self.treebuscar.column("col2",width=100, anchor=CENTER)
        self.treebuscar.column("col3",width=100, anchor=CENTER)
        self.treebuscar.column("col4",width=100, anchor=CENTER)
        self.treebuscar.column("col5",width=125, anchor=CENTER)
        self.treebuscar.column("col6",width=100, anchor=CENTER)
        self.treebuscar.column("col7",width=200, anchor=CENTER) 
        self.treebuscar.column("col8",width=100, anchor=CENTER)   

        self.treebuscar.heading("#0", text="Id", anchor=CENTER)
        self.treebuscar.heading("col2", text="Nombre", anchor=CENTER)
        self.treebuscar.heading("col3", text="Fecha", anchor=CENTER)
        self.treebuscar.heading("col4", text="Previsión", anchor=CENTER)
        self.treebuscar.heading("col5", text="Motivo de ingreso", anchor=CENTER)
        self.treebuscar.heading("col6", text="Derivación", anchor=CENTER)
        self.treebuscar.heading("col7", text="Médico atención", anchor=CENTER)
        self.treebuscar.heading("col8", text="Box de atención", anchor=CENTER)
        self.treebuscar.place(x=100,y=100)
        
        self.Box=Label(framebuscar,text="Box totales 5",font=("Blue Fonte",12,"bold"))
        self.Box.place(x=400,y=200,width=200,height=30)
        self.Box2=Label(framebuscar,text="Box ocupados:"+str(self.pacientes.suma_de_box()),font=("Blue Fonte",12,"bold"))
        self.Box2.place(x=400,y=220,width=200,height=30)

#----------------------------------------------------------------------VENTANA PERSONAL ADMINISTRATIVOS----------------------------------------------------------------------------------
class Ventana_personal(Frame):

    personal=Personal()
    pago_personal=PagoPersonal()

    def __init__(self, master=None):
        super().__init__(master,width=1920, height=1080)
        self.master = master
        self.pack()
        self.CrearFrames()
        self.llenaDatos()
        self.habilitarCajas("disabled")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")  
        self.id=-1

    def habilitarCajas(self,estado):
        self.etRut.configure(state=estado)
        self.etNombre.configure(state=estado)
        self.etFecha.configure(state=estado)
        self.etPrevision.configure(state=estado)
        self.etSueldo.configure(state=estado)
        self.etUnidad.configure(state=estado)
        self.etCargo.configure(state=estado)

    def habilitarBtnOper(self,estado):
        self.btnNuevo.configure(state=estado)                
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)

    def habilitarBtnGuardar(self,estado):
        self.btnGuardar.configure(state=estado)                
        self.btnCancelar.configure(state=estado) 

    def limpiaGrid(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def limpiarCajas(self):
        self.etRut.delete(0,END)
        self.etNombre.delete(0,END)
        self.etFecha.delete(0,END)
        self.etPrevision.delete(0,END)
        self.etSueldo.delete(0,END)
        self.etUnidad.delete(0,END)
        self.etCargo.delete(0,END)

    def llenaDatos(self):
        datos = self.personal.consulta_personal()        
        for row in datos:            
            self.tree.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6],row[7]))     

    def Nuevo(self):
        self.limpiarCajas()
        self.habilitarCajas("normal")
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.etPrevision.configure(state="readonly")
        self.etFecha.configure(state="readonly")
        self.etUnidad.configure(state="readonly")
        self.etCargo.configure(state="readonly")
        self.limpiarCajas() 

    def validar_valores_personal(self):
        if not self.etNombre.get() or not self.etRut.get() or not self.etFecha.get() or not self.etPrevision.get() or not self.etSueldo.get() or not self.etUnidad.get() or not self.etCargo.get():
            return False
        return True
    
    def validar_sueldo(self,sueldo):
        if(int(sueldo)<=0):
            return False
        return True
    
    def validar_nombre(self,nombre):
        patron = r'^[a-zA-Z\s]+$'
        if re.match(patron, nombre):
            return True
        else:
            return False
        
    def validarFecha(self,fecha):
        fecha_seleccionada = datetime.strptime(fecha, "%Y-%m-%d")
        fecha_actual = datetime.now()

        if fecha_seleccionada > fecha_actual:
            return False
        else:
            return True
        
    def Guardar(self):
        if(self.validar_valores_personal()): 
            if self.id ==-1:
                if(self.validarFecha(self.etFecha.get())):
                    if(self.validar_nombre(self.etNombre.get())):
                        if(self.validar_sueldo(self.etSueldo.get())):
                            if(self.personal.insertar_personal(self.etRut.get(),self.etNombre.get(),self.etFecha.get(),self.etPrevision.get(),self.etSueldo.get(),self.etUnidad.get(),self.etCargo.get())==1):
                                datos=self.personal.Rutspersonal()
                                self.etBuscar.configure(values=datos)
                                self.pago_personal.insertar_pagopersonal(self.etRut.get(),self.etNombre.get(),self.etSueldo.get(),"Administrativo",self.pago_personal.descuentos_administrativo(self.etRut.get()),self.pago_personal.beneficios_administrativo(self.etRut.get()),int(self.etSueldo.get())-int(self.pago_personal.sueldo_liquido_administrativo(self.etRut.get())))            
                                messagebox.showinfo("Guardar", 'Elemento guardado correctamente.')
                                self.etRut.configure(state="normal")
                                self.etNombre.configure(state="normal")
                                self.etPrevision.configure(state="normal")
                                self.etFecha.configure(state="normal")
                                self.etUnidad.configure(state="normal")
                                self.etCargo.configure(state="normal") 
                                self.limpiaGrid()
                                self.llenaDatos() 
                                self.limpiarCajas() 
                                self.habilitarBtnGuardar("disabled")      
                                self.habilitarBtnOper("normal")
                                self.habilitarCajas("disabled")
                            else:
                                messagebox.showinfo("Guardar", "No fue posible guardar el elemento.")
                        else:
                            messagebox.showinfo("ERROR", "Ingrese un sueldo mayor a 0.")
                    else:
                        messagebox.showinfo("ERROR", "Ingrese un nombre alfabético.")
                else:
                    messagebox.showinfo("ERROR", "Fecha seleccionada no puede ser futura.")
            else:
                if(self.validarFecha(self.etFecha.get())):
                    if(self.validar_nombre(self.etNombre.get())):
                        if(self.validar_sueldo(self.etSueldo.get())):
                            if(self.personal.modificar_personal(self.etRut.get(),self.etFecha.get(),self.etPrevision.get(),self.etSueldo.get(),self.etUnidad.get(),self.etCargo.get())==1):
                                self.id = -1
                                self.pago_personal.modificar_pagopersonal(self.etRut.get(),self.etSueldo.get(),self.pago_personal.descuentos_administrativo(self.etRut.get()),self.pago_personal.beneficios_administrativo(self.etRut.get()),int(self.etSueldo.get())-int(self.pago_personal.sueldo_liquido_administrativo(self.etRut.get())))
                                messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
                                self.etRut.configure(state="normal")
                                self.etNombre.configure(state="normal")
                                self.etPrevision.configure(state="normal")
                                self.etFecha.configure(state="normal")
                                self.etUnidad.configure(state="normal")
                                self.etCargo.configure(state="normal") 
                                self.limpiaGrid()
                                self.llenaDatos() 
                                self.limpiarCajas() 
                                self.habilitarBtnGuardar("disabled")      
                                self.habilitarBtnOper("normal")
                                self.habilitarCajas("disabled")
                            else:
                                messagebox.showinfo("Modificar", "No fue posible modificar el elemento.")
                        else:
                            messagebox.showinfo("ERROR", "Ingrese un sueldo mayor a 0.")
                    else:
                        messagebox.showinfo("ERROR", "Ingrese un nombre alfabético.")
                else:
                    messagebox.showinfo("ERROR", "Fecha seleccionada no puede ser futura.")
        else:
            messagebox.showwarning("Guardar", "Debes completar todos los campos.")
                    
    def Modificar(self):        
        selected = self.tree.focus()                               
        clave = self.tree.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:           
            self.id= clave  
            self.habilitarCajas("normal")                         
            valores = self.tree.item(selected,'values')
            print(valores) 
            self.limpiarCajas()
            self.etRut.insert(0,valores[0])
            self.etNombre.insert(0,valores[1])
            self.etRut.configure(state="disabled")
            self.etNombre.configure(state="disabled") 
            self.etFecha.insert(0,valores[2])
            self.etPrevision.insert(0,valores[3])
            self.etSueldo.insert(0,valores[4]) 
            self.etUnidad.insert(0,valores[5])
            self.etCargo.insert(0,valores[6])
            self.etPrevision.configure(state="readonly")
            self.etFecha.configure(state="readonly")
            self.etUnidad.configure(state="readonly")
            self.etCargo.configure(state="readonly")  
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")

    def Eliminar(self):
        selected = self.tree.focus()                               
        clave = self.tree.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.tree.item(selected,'values')
            print(valores[0])
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            respuesta = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if respuesta == messagebox.YES:
                n = self.personal.eliminar_personal(valores[0])
                self.pago_personal.eliminar_pago_personal(valores[0])
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatos()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')

    def Cancelar(self):
        r = messagebox.askquestion("Cancelar", "Esta seguro que desea cancelar la operación actual.")
        if r == messagebox.YES:

            self.etRut.configure(state="normal")
            self.etNombre.configure(state="normal")
            self.etPrevision.configure(state="normal")
            self.etFecha.configure(state="normal")
            self.etUnidad.configure(state="normal")
            self.etCargo.configure(state="normal")
            self.limpiarCajas() 
            self.habilitarBtnGuardar("disabled")      
            self.habilitarBtnOper("normal")
            self.habilitarCajas("disabled")
    
    def Exel_Personal(self):
        datos=self.personal.consulta_personal()
        i=-1
        id,rut,nombre,fecha,prevision,sueldo,unidad,cargo= [],[],[],[],[],[],[],[]
        for dato in datos:
            i=i+1
            id.append(datos[i][0])
            rut.append(datos[i][1])
            nombre.append(datos[i][2])
            fecha.append(datos[i][3])
            prevision.append(datos[i][4])
            sueldo.append(datos[i][5])
            unidad.append(datos[i][6])
            cargo.append(datos[i][7])

        fecha_archivo=str(strftime('%d-%m-%y_%H-%M-%S'))
        datos2={'Id': id,'Rut': rut,'Nombre': nombre,'Fecha de ingreso': fecha,'Prevision de salud': prevision,'Sueldo bruto': sueldo,'Unidad administrativa': unidad,'Cargo': cargo}
        df=pd.DataFrame(datos2)
        df.to_excel(rf'C:\Users\vicen\Desktop\n\Excel\Datos_Personal_{fecha_archivo}.xlsx')
        messagebox.showinfo('Informacion','Excel creado correctamente')

    def vaciararbolbuscarpaciente(self):
        for item in self.treebuscar.get_children():
            self.treebuscar.delete(item)

    def llenardatosBuscarpaciente(self):
        self.vaciararbolbuscarpaciente()
        datos = self.personal.buscar_personal(self.etBuscar.get())        
        for row in datos:            
            self.treebuscar.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6]))
    
    def CrearFrames(self):
        frame1=Frame(self,bg="#E9967A")
        frame1.place(x=0,y=0,width=1920, height=1080)
#--------------------------------------------------------------------------TITULO----------------------------------------------------------------------------------
        titulo2=Label(frame1,text="Personal Administrativo",bg="#D2691E",fg="#000000",font=("Garamond",30,"bold"))
        titulo2.place(x=700,y=0,width=500, height=60)
        
#--------------------------------------------------------------------------BOTONES----------------------------------------------------------------------------------
        self.btnNuevo=Button(frame1,text="Nuevo", command=self.Nuevo, bg="#B22222", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnNuevo.place(x=660,y=520,width=80, height=30 )  

        self.btnModificar=Button(frame1,text="Modificar", command=self.Modificar, bg="#B22222", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnModificar.place(x=760,y=520,width=80, height=30)   

        self.btnEliminar=Button(frame1,text="Eliminar", command=self.Eliminar, bg="#B22222", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnEliminar.place(x=860,y=520,width=80, height=30)    

        self.btnGuardar=Button(frame1,text="Guardar", command=self.Guardar, bg="#228B22", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnGuardar.place(x=960,y=520,width=80, height=30)

        self.btnCancelar=Button(frame1,text="Cancelar", command=self.Cancelar, bg="#FF0000", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnCancelar.place(x=1060,y=520,width=80, height=30)

        self.btnExcel=Button(frame1,text="Crear Excel", command=self.Exel_Personal,bg="#B22222", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnExcel.place(x=1160,y=520,width=100, height=30)

#--------------------------------------------------------------------------VALORES----------------------------------------------------------------------------------
        labelRut=Label(frame1,text="Rut",font=("Blue Fonte",12,"bold"))
        labelRut.place(x=100,y=125,width=200, height=20)
        self.etRut=Entry(frame1)
        self.etRut.place(x=330,y=125,width=200, height=20)

        labelNombre=Label(frame1,text="Nombre",font=("Blue Fonte",12,"bold"))
        labelNombre.place(x=100,y=175,width=200, height=20)
        self.etNombre=Entry(frame1)
        self.etNombre.place(x=330,y=175,width=200, height=20)

        labelFecha=Label(frame1,text="Fecha de ingreso",font=("Blue Fonte",12,"bold"))
        labelFecha.place(x=100,y=225,width=200, height=20)
        self.etFecha=DateEntry(frame1,width=12, background='darkblue', foreground='white', selectbackground='orange', date_pattern='y-mm-dd')
        self.etFecha.place(x=330,y=225,width=200, height=20)

        labelPrevision=Label(frame1,text="Previsión de salud",font=("Blue Fonte",12,"bold"))
        labelPrevision.place(x=100,y=275,width=200, height=20)
        self.etPrevision=ttk.Combobox(frame1,values=["Fonasa","Isapre","Particular"])
        self.etPrevision.place(x=330,y=275,width=200, height=20)

        labelSueldo=Label(frame1,text="Sueldo bruto",font=("Blue Fonte",12,"bold"))
        labelSueldo.place(x=100,y=325,width=200, height=20)
        self.etSueldo=Entry(frame1)
        self.etSueldo.place(x=330,y=325,width=200, height=20)

        labelUnidad=Label(frame1,text="Unidad administrativa",font=("Blue Fonte",12,"bold"))
        labelUnidad.place(x=100,y=375,width=200, height=20)
        self.etUnidad=ttk.Combobox(frame1,values=["Unidad de servicios generales","Unidad de personal","Unidad de jefatura"])
        self.etUnidad.place(x=330,y=375,width=200, height=20)

        labelCargo=Label(frame1,text="Cargo",font=("Blue Fonte",12,"bold"))
        labelCargo.place(x=100,y=425,width=200, height=20)
        self.etCargo=ttk.Combobox(frame1,values=["Jefe","Secretario","Tesorero","Asistente","Sin cargo"])
        self.etCargo.place(x=330,y=425,width=200, height=20)

#--------------------------------------------------------------------------ARBOL---------------------------------------------------------------------------------- 
        self.tree=ttk.Treeview(frame1, columns=("col1","col2","col3","col4","col5","col6","col7"),height=20)
        self.tree.column("#0",width=50)
        self.tree.column("col1",width=125, anchor=CENTER)
        self.tree.column("col2",width=125, anchor=CENTER)
        self.tree.column("col3",width=125, anchor=CENTER)
        self.tree.column("col4",width=125, anchor=CENTER)
        self.tree.column("col5",width=125, anchor=CENTER)
        self.tree.column("col6",width=170, anchor=CENTER)
        self.tree.column("col7",width=150, anchor=CENTER)
    
        self.tree.heading("#0", text="id", anchor=CENTER)
        self.tree.heading("col1", text="Rut", anchor=CENTER)
        self.tree.heading("col2", text="Nombre", anchor=CENTER)
        self.tree.heading("col3", text="Fecha de ingreso", anchor=CENTER)
        self.tree.heading("col4", text="Previsión de salud", anchor=CENTER)
        self.tree.heading("col5", text="Sueldo bruto", anchor=CENTER)
        self.tree.heading("col6", text="Unidad administrativa", anchor=CENTER)
        self.tree.heading("col7", text="Cargo", anchor=CENTER)
                        
        self.tree.place(x=400,y=570) 

#--------------------------------------------------------------------------FRAME BUSCAR----------------------------------------------------------------------------------
        framebuscar=Frame(frame1,bg="#CD853F")
        framebuscar.place(x=650,y=125,width=1000, height=350)
        
        self.btnbuscar=Button(framebuscar,text="Buscar", command=self.llenardatosBuscarpaciente, bg="#FF6347", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnbuscar.place(x=400,y=40,width=100,height=30)
        datos=self.personal.Rutspersonal()
        self.etBuscar=ttk.Combobox(framebuscar,values=datos)
        self.etBuscar.place(x=525,y=40,width=150,height=30)

        self.treebuscar=ttk.Treeview(framebuscar,columns=("col2","col3","col4","col5","col6","col7"),height=1)
        self.treebuscar.column("#0",width=38,anchor=CENTER)
        self.treebuscar.column("col2",width=100, anchor=CENTER)
        self.treebuscar.column("col3",width=100, anchor=CENTER)
        self.treebuscar.column("col4",width=100, anchor=CENTER)
        self.treebuscar.column("col5",width=125, anchor=CENTER)
        self.treebuscar.column("col6",width=170, anchor=CENTER)
        self.treebuscar.column("col7",width=150, anchor=CENTER) 
  

        self.treebuscar.heading("#0", text="Id", anchor=CENTER)
        self.treebuscar.heading("col2", text="Nombre", anchor=CENTER)
        self.treebuscar.heading("col3", text="Fecha", anchor=CENTER)
        self.treebuscar.heading("col4", text="Previsión", anchor=CENTER)
        self.treebuscar.heading("col5", text="Sueldo bruto", anchor=CENTER)
        self.treebuscar.heading("col6", text="Unidad administrativa", anchor=CENTER)
        self.treebuscar.heading("col7", text="Cargo", anchor=CENTER)
        self.treebuscar.place(x=80,y=100)

#--------------------------------------------------------------------------VENTANA PAGO PERSONAL----------------------------------------------------------------------------------
class Ventana_pago_personal(Frame):

    pago_personal=PagoPersonal()

    def __init__(self, master=None):
        super().__init__(master,width=1920, height=1080)
        self.master = master
        self.pack()
        self.CrearFrames()
        self.llenaDatos() 
        self.id=-1

    def limpiartree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def llenaDatos(self):
        self.limpiartree()
        datos = self.pago_personal.consulta_pagos_personal()        
        for row in datos:            
            self.tree.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6],row[7]))     

    def vaciararbolbuscarpago(self):
        for item in self.treebuscar.get_children():
            self.treebuscar.delete(item)

    def llenardatosBuscarpago(self):
        self.vaciararbolbuscarpago()
        datos = self.pago_personal.buscar_pago_personal(self.etBuscar.get())        
        for row in datos:            
            self.treebuscar.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6],row[7]))
        self.SueldoLiquido2.configure(text="$"+str(self.pago_personal.SueldoRut(self.etBuscar.get())))
        self.SueldoNombre.configure(text=str(self.pago_personal.SueldoNombre(self.etBuscar.get())))
    
    def Exel_Pago_personal(self):
        datos=self.pago_personal.consulta_pagos_personal()
        i=-1
        id,rut,nombre,sueldo,cargo,descuentos,bonificaciones,liquido= [],[],[],[],[],[],[],[]
        for dato in datos:
            i=i+1
            id.append(datos[i][0])
            rut.append(datos[i][1])
            nombre.append(datos[i][2])
            sueldo.append(datos[i][3])
            cargo.append(datos[i][4])
            descuentos.append(datos[i][5])
            bonificaciones.append(datos[i][6])
            liquido.append(datos[i][7])

        fecha_archivo=str(strftime('%d-%m-%y_%H-%M-%S'))
        datos2={'Id': id,'Rut': rut,'Nombre': nombre,'Sueldo bruto': sueldo,'Cargo': cargo,'Descuentos(AFP y salud)': descuentos,'Bonificaciones': bonificaciones,'Sueldo liquido': cargo}
        df=pd.DataFrame(datos2)
        df.to_excel(rf'C:\Users\vicen\Desktop\n\Excel\Datos_Pago_Personal_{fecha_archivo}.xlsx')
        messagebox.showinfo('Informacion','Excel creado correctamente')
        
    def CrearFrames(self):
        frame1=Frame(self,bg="#FF8C00")
        frame1.place(x=0,y=0,width=1920, height=1080)
#---------------------------------------------------------------------------TITULOS--------------------------------------------------------------------------------
        titulo2=Label(frame1,text="Pago del personal",bg="#800000",fg="#F0F8FF",font=("Garamond",30,"bold"))
        titulo2.place(x=750,y=0,width=500, height=60)

#--------------------------------------------------------------------------ARBOL----------------------------------------------------------------------------------
        self.tree=ttk.Treeview(frame1,columns=("col1","col2","col3","col4","col5","col6","col7"),height=20)
        self.tree.column("#0",width=50,anchor=CENTER)
        self.tree.column("col1",width=150, anchor=CENTER)
        self.tree.column("col2",width=150, anchor=CENTER)
        self.tree.column("col3",width=150, anchor=CENTER)
        self.tree.column("col4",width=150, anchor=CENTER)
        self.tree.column("col5",width=150, anchor=CENTER)
        self.tree.column("col6",width=150, anchor=CENTER)
        self.tree.column("col7",width=150, anchor=CENTER) 
  
        self.tree.heading("#0", text="Id", anchor=CENTER)
        self.tree.heading("col1", text="Rut", anchor=CENTER)
        self.tree.heading("col2", text="Nombre", anchor=CENTER)
        self.tree.heading("col3", text="Sueldo bruto", anchor=CENTER)
        self.tree.heading("col4", text="Cargo", anchor=CENTER)
        self.tree.heading("col5", text="Descuentos", anchor=CENTER)
        self.tree.heading("col6", text="Bonificaciones", anchor=CENTER)
        self.tree.heading("col7", text="Sueldo líquido", anchor=CENTER)
        self.tree.place(x=400,y=500)
                        

#--------------------------------------------------------------------------FRAME BUSCAR----------------------------------------------------------------------------------
        framebuscar=Frame(frame1,bg="#FF6347")
        framebuscar.place(x=475,y=125,width=1000, height=350)
        
        self.btnbuscar=Button(framebuscar,text="Buscar", command=self.llenardatosBuscarpago, bg="#FF6347", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnbuscar.place(x=400,y=40,width=100,height=30)

        self.btnCrearExcel=Button(framebuscar,text="Crear Excel", command=self.Exel_Pago_personal, bg="#B22222", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnCrearExcel.place(x=250,y=40,width=100,height=30)

        datos=self.pago_personal.Rutspagopersonal()
        self.etBuscar=ttk.Combobox(framebuscar,values=datos)
        self.etBuscar.place(x=525,y=40,width=150,height=30)

        self.SueldoLiquido=Label(framebuscar,text="Sueldo líquido a pagar a:",font=("Blue Fonte",18,"bold"))
        self.SueldoLiquido.place(x=100,y=170,width=350,height=80)
        
        self.SueldoNombre=Label(framebuscar,text="",font=("Blue Fonte",18,"bold"))
        self.SueldoNombre.place(x=100,y=250,width=350,height=80)

        self.SueldoLiquido2=Label(framebuscar,text="",font=("Blue Fonte",18,"bold"))
        self.SueldoLiquido2.place(x=500,y=200,width=350,height=80)

        self.treebuscar=ttk.Treeview(framebuscar,columns=("col1","col2","col3","col4","col5","col6","col7"),height=1)
        self.treebuscar.column("#0",width=40)
        self.treebuscar.column("col1",width=100, anchor=CENTER)
        self.treebuscar.column("col2",width=150, anchor=CENTER)
        self.treebuscar.column("col3",width=100, anchor=CENTER)
        self.treebuscar.column("col4",width=100, anchor=CENTER)
        self.treebuscar.column("col5",width=100, anchor=CENTER)
        self.treebuscar.column("col6",width=100, anchor=CENTER)
        self.treebuscar.column("col7",width=125, anchor=CENTER)
         
        self.treebuscar.heading("#0", text="Id")
        self.treebuscar.heading("col1", text="Rut", anchor=CENTER)
        self.treebuscar.heading("col2", text="Nombre", anchor=CENTER)
        self.treebuscar.heading("col3", text="Sueldo bruto", anchor=CENTER)
        self.treebuscar.heading("col4", text="Cargo", anchor=CENTER)
        self.treebuscar.heading("col5", text="Descuentos", anchor=CENTER)
        self.treebuscar.heading("col6", text="Bonificaciones", anchor=CENTER)
        self.treebuscar.heading("col7", text="Sueldo líquido", anchor=CENTER)
        self.treebuscar.place(x=70,y=100)

#--------------------------------------------------------------------------VENTA COBRO PACIENTES----------------------------------------------------------------------------------
class Ventana_cobro_paciente(Frame):

    cobro=Cobro_paciente()

    def __init__(self, master=None):
        super().__init__(master,width=1920, height=1080)
        self.master = master
        self.pack()
        self.CrearFrames()
        self.llenaDatos() 
        self.id=-1

    def limpiartree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def llenaDatos(self):
        self.limpiartree()
        datos = self.cobro.consulta_cobro_paciente()        
        for row in datos:            
            self.tree.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6],row[7],row[8]))     

    def vaciararbolbuscarpago(self):
        for item in self.treebuscar.get_children():
            self.treebuscar.delete(item)

    def llenardatosBuscarpago(self):
        self.vaciararbolbuscarpago()
        datos = self.cobro.buscar_cobro_paciente(self.etBuscar.get())        
        for row in datos:            
            self.treebuscar.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6],row[7]))

        self.CobroTotal.configure(text="$"+str(self.cobro.CobroRut(self.etBuscar.get())))
        self.CobroNombre.configure(text=str(self.cobro.cobroNombre(self.etBuscar.get())))

    def Exel_Cobro_paciente(self):
        datos=self.cobro.consulta_cobro_paciente()
        i=-1
        id,rut,nombre,prevision,derivacion,dias,cobro,descuento,total= [],[],[],[],[],[],[],[],[]
        for dato in datos:
            i=i+1
            id.append(datos[i][0])
            rut.append(datos[i][1])
            nombre.append(datos[i][2])
            prevision.append(datos[i][3])
            derivacion.append(datos[i][4])
            dias.append(datos[i][5])
            cobro.append(datos[i][6])
            descuento.append(datos[i][7])
            total.append(datos[i][8])

        fecha_archivo=str(strftime('%d-%m-%y_%H-%M-%S'))
        datos2={'Id': id,'Rut': rut,'Nombre': nombre,'Prevision de salud': prevision,'Derivacion': derivacion,'Dias': dias,'Cobro': cobro,'Descuento': descuento,'Cobro total': total}
        df=pd.DataFrame(datos2)
        df.to_excel(rf'C:\Users\vicen\Desktop\n\Excel\Datos_Cobro_Consulta_{fecha_archivo}.xlsx')
        messagebox.showinfo('Informacion','Excel creado correctamente')

    def CrearFrames(self):
        frame1=Frame(self,bg="#228B22")
        frame1.place(x=0,y=0,width=1920, height=1080)
#--------------------------------------------------------------------------TITULO----------------------------------------------------------------------------------
        titulo2=Label(frame1,text="Cobro consulta",bg="#3CB371",fg="#000000",font=("Garamond",30,"bold"))
        titulo2.place(x=750,y=0,width=500, height=60)

#--------------------------------------------------------------------------ARBOL----------------------------------------------------------------------------------
        self.tree=ttk.Treeview(frame1,columns=("col1","col2","col3","col4","col5","col6","col7","col8"),height=20)
        self.tree.column("#0",width=50,anchor=CENTER)
        self.tree.column("col1",width=150, anchor=CENTER)
        self.tree.column("col2",width=150, anchor=CENTER)
        self.tree.column("col3",width=150, anchor=CENTER)
        self.tree.column("col4",width=150, anchor=CENTER)
        self.tree.column("col5",width=150, anchor=CENTER)
        self.tree.column("col6",width=150, anchor=CENTER)
        self.tree.column("col7",width=150, anchor=CENTER)
        self.tree.column("col8",width=150, anchor=CENTER) 
  
        self.tree.heading("#0", text="Id", anchor=CENTER)
        self.tree.heading("col1", text="Rut", anchor=CENTER)
        self.tree.heading("col2", text="Nombre", anchor=CENTER)
        self.tree.heading("col3", text="Previsión de salud", anchor=CENTER)
        self.tree.heading("col4", text="Derivación", anchor=CENTER)
        self.tree.heading("col5", text="Días", anchor=CENTER)
        self.tree.heading("col6", text="Cobro sin descuento", anchor=CENTER)
        self.tree.heading("col7", text="Descuento", anchor=CENTER)
        self.tree.heading("col8", text="Cobro total", anchor=CENTER)
        self.tree.place(x=300,y=500)
                        
#--------------------------------------------------------------------------FRAME BUSCAR----------------------------------------------------------------------------------
        framebuscar=Frame(frame1,bg="#8FBC8F")
        framebuscar.place(x=475,y=125,width=1000, height=350)
        
        self.btnbuscar=Button(framebuscar,text="Buscar", command=self.llenardatosBuscarpago, bg="#2E8B57", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnbuscar.place(x=400,y=40,width=100,height=30)
        datos=self.cobro.Rutscobropacientes()
        self.etBuscar=ttk.Combobox(framebuscar,values=datos)
        self.etBuscar.place(x=525,y=40,width=150,height=30)

        self.btnCrearExcel=Button(framebuscar,text="Crear Excel", command=self.Exel_Cobro_paciente, bg="#2E8B57", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnCrearExcel.place(x=250,y=40,width=100,height=30)

        self.consulta=Label(framebuscar,text="Precio a pagar por:",font=("Blue Fonte",20,"bold"))
        self.consulta.place(x=100,y=170,width=400,height=80)
        
        self.CobroNombre=Label(framebuscar,text="",font=("Blue Fonte",20,"bold"))
        self.CobroNombre.place(x=100,y=250,width=400,height=80)

        self.CobroTotal=Label(framebuscar,text="",font=("Blue Fonte",20,"bold"))
        self.CobroTotal.place(x=550,y=200,width=350,height=80)

        self.treebuscar=ttk.Treeview(framebuscar,columns=("col1","col2","col3","col4","col5","col6","col7"),height=1)
        self.treebuscar.column("#0",width=40)
        self.treebuscar.column("col1",width=100, anchor=CENTER)
        self.treebuscar.column("col2",width=150, anchor=CENTER)
        self.treebuscar.column("col3",width=100, anchor=CENTER)
        self.treebuscar.column("col4",width=100, anchor=CENTER)
        self.treebuscar.column("col5",width=125, anchor=CENTER)
        self.treebuscar.column("col6",width=100, anchor=CENTER)
        self.treebuscar.column("col7",width=125, anchor=CENTER)
         
        self.treebuscar.heading("#0", text="Id")
        self.treebuscar.heading("col1", text="Nombre", anchor=CENTER)
        self.treebuscar.heading("col2", text="Previsión", anchor=CENTER)
        self.treebuscar.heading("col3", text="Derivación", anchor=CENTER)
        self.treebuscar.heading("col4", text="Días", anchor=CENTER)
        self.treebuscar.heading("col5", text="Cobro sin descuentos", anchor=CENTER)
        self.treebuscar.heading("col6", text="Descuentos", anchor=CENTER)
        self.treebuscar.heading("col7", text="Cobro total", anchor=CENTER)
        self.treebuscar.place(x=70,y=100)
#--------------------------------------------------------------------------VENTANA BUSQUEDAS 1----------------------------------------------------------------------------------
class Ventana_Busquedas_1(Frame):

    busquedas=Busquedas()

    def __init__(self, master=None):
        super().__init__(master,width=1920, height=1080)
        self.master = master
        self.pack()
        self.CrearFrames()
        self.id=-1

    def vaciararbolmedico(self):
        for item in self.treebuscarmedico.get_children():
            self.treebuscarmedico.delete(item)

    def llenardatosmedicos(self):
        self.vaciararbolmedico()
        datos = self.busquedas.Medicos_x_Especialista(self.etBuscarmedico.get())        
        for row in datos:            
            self.treebuscarmedico.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6]))
    
    def vaciararboltens(self):
        for item in self.treebuscartens.get_children():
            self.treebuscartens.delete(item)

    def llenardatostens(self):
        self.vaciararboltens()
        datos = self.busquedas.Tens_x_Areas(self.etBuscartens.get())        
        for row in datos:            
            self.treebuscartens.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6]))

    def vaciararbolpersonal(self):
        for item in self.treebuscarPersonal.get_children():
            self.treebuscarPersonal.delete(item)

    def llenardatospersonal(self):
        self.vaciararbolpersonal()
        datos = self.busquedas.Administrativos_x_cargo_unidad(self.etBuscarUnidad.get(),self.etBuscarCargo.get())        
        for row in datos:            
            self.treebuscarPersonal.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6],row[7]))

    def CrearFrames(self):
        frame1=Frame(self,bg="#8FBC8F")
        frame1.place(x=0,y=0,width=1920, height=1080)

        frameMedico=Frame(frame1,bg="#8FBC8F")
        frameMedico.place(x=0,y=50,width=1920, height=340)
#--------------------------------------------------------------------------TITULO----------------------------------------------------------------------------------
        tituloMedico=Label(frameMedico,text="Médicos por Especialidad",bg="#3CB371",fg="#000000",font=("Garamond",30,"bold"))
        tituloMedico.place(x=790,y=0,width=500, height=60)
        
        self.btnbuscarmedico=Button(frameMedico,text="Buscar", command=self.llenardatosmedicos, bg="#2E8B57", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnbuscarmedico.place(x=400,y=40,width=100,height=30)
#--------------------------------------------------------------------------ARBOL---------------------------------------------------------------------------------
        self.etBuscarmedico=ttk.Combobox(frameMedico,values=["Pediatria","Anestesiologia","Cardiologia","Gastroenterologia","Medicina General","Ginecologia","Obstetricia"])
        self.etBuscarmedico.place(x=525,y=40,width=150,height=30)

        self.treebuscarmedico=ttk.Treeview(frameMedico,columns=("col1","col2","col3","col4","col5","col6"),height=4)
        self.treebuscarmedico.column("#0",width=40)
        self.treebuscarmedico.column("col1",width=150, anchor=CENTER)
        self.treebuscarmedico.column("col2",width=150, anchor=CENTER)
        self.treebuscarmedico.column("col3",width=150, anchor=CENTER)
        self.treebuscarmedico.column("col4",width=150, anchor=CENTER)
        self.treebuscarmedico.column("col5",width=150, anchor=CENTER)
        self.treebuscarmedico.column("col6",width=150, anchor=CENTER)
         
        self.treebuscarmedico.heading("#0", text="Id")
        self.treebuscarmedico.heading("col1", text="Rut", anchor=CENTER)
        self.treebuscarmedico.heading("col2", text="Nombre", anchor=CENTER)
        self.treebuscarmedico.heading("col3", text="Fecha de ingreso", anchor=CENTER)
        self.treebuscarmedico.heading("col4", text="Previsión de salud", anchor=CENTER)
        self.treebuscarmedico.heading("col5", text="Sueldo bruto", anchor=CENTER)
        self.treebuscarmedico.heading("col6", text="Especialidad", anchor=CENTER)
        self.treebuscarmedico.place(x=450,y=100)
#____________________________________________________________________________________________________________________________________________________________________
        frameTens=Frame(frame1,bg="#8FBC8F")
        frameTens.place(x=0,y=300,width=1920, height=340)

#--------------------------------------------------------------------------TITULO----------------------------------------------------------------------------------

        titulotens=Label(frameTens,text="Tens según área",bg="#3CB371",fg="#000000",font=("Garamond",30,"bold"))
        titulotens.place(x=790,y=0,width=500, height=60)
        
        self.btnbuscartens=Button(frameTens,text="Buscar", command=self.llenardatostens, bg="#2E8B57", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnbuscartens.place(x=400,y=40,width=100,height=30)

        self.etBuscartens=ttk.Combobox(frameTens,values=["Consulta externa","Emergencia","Pediatria","Quirofano","Hospitalizacion","Recuperacion UCI"])
        self.etBuscartens.place(x=525,y=40,width=150,height=30)

#--------------------------------------------------------------------------ARBOL----------------------------------------------------------------------------------
        self.treebuscartens=ttk.Treeview(frameTens,columns=("col1","col2","col3","col4","col5","col6"),height=4)
        self.treebuscartens.column("#0",width=40)
        self.treebuscartens.column("col1",width=150, anchor=CENTER)
        self.treebuscartens.column("col2",width=150, anchor=CENTER)
        self.treebuscartens.column("col3",width=150, anchor=CENTER)
        self.treebuscartens.column("col4",width=150, anchor=CENTER)
        self.treebuscartens.column("col5",width=150, anchor=CENTER)
        self.treebuscartens.column("col6",width=150, anchor=CENTER)
         
        self.treebuscartens.heading("#0", text="Id")
        self.treebuscartens.heading("col1", text="Rut", anchor=CENTER)
        self.treebuscartens.heading("col2", text="Nombre", anchor=CENTER)
        self.treebuscartens.heading("col3", text="Fecha de ingreso", anchor=CENTER)
        self.treebuscartens.heading("col4", text="Previsión de salud", anchor=CENTER)
        self.treebuscartens.heading("col5", text="Sueldo bruto", anchor=CENTER)
        self.treebuscartens.heading("col6", text="Especialidad", anchor=CENTER)
        self.treebuscartens.place(x=450,y=100)

#____________________________________________________________________________________________________________________________________________________________________
        framePersonal=Frame(frame1,bg="#8FBC8F")
        framePersonal.place(x=0,y=550,width=1920, height=340)
#--------------------------------------------------------------------------TITULO----------------------------------------------------------------------------------
        tituloPersonal=Label(framePersonal,text="Administrativos según cargo y unidad",bg="#3CB371",fg="#000000",font=("Garamond",30,"bold"))
        tituloPersonal.place(x=790,y=0,width=800, height=60)
        
        self.btnbuscarPersonal=Button(framePersonal,text="Buscar", command=self.llenardatospersonal, bg="#2E8B57", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnbuscarPersonal.place(x=280,y=40,width=100,height=30)

        self.etBuscarUnidad=ttk.Combobox(framePersonal,values=["Unidad de servicios generales","Unidad de personal","Unidad de jefatura"])
        self.etBuscarUnidad.place(x=400,y=40,width=180,height=30)

        self.etBuscarCargo=ttk.Combobox(framePersonal,values=["Jefe","Secretario","Tesorero","Asistente","Sin cargo"])
        self.etBuscarCargo.place(x=600,y=40,width=150,height=30)

#--------------------------------------------------------------------------ARBOL----------------------------------------------------------------------------------
        self.treebuscarPersonal=ttk.Treeview(framePersonal,columns=("col1","col2","col3","col4","col5","col6","col7"),height=4)
        self.treebuscarPersonal.column("#0",width=40)
        self.treebuscarPersonal.column("col1",width=150, anchor=CENTER)
        self.treebuscarPersonal.column("col2",width=150, anchor=CENTER)
        self.treebuscarPersonal.column("col3",width=150, anchor=CENTER)
        self.treebuscarPersonal.column("col4",width=150, anchor=CENTER)
        self.treebuscarPersonal.column("col5",width=150, anchor=CENTER)
        self.treebuscarPersonal.column("col6",width=150, anchor=CENTER)
        self.treebuscarPersonal.column("col7",width=150, anchor=CENTER)
         
        self.treebuscarPersonal.heading("#0", text="Id")
        self.treebuscarPersonal.heading("col1", text="Rut", anchor=CENTER)
        self.treebuscarPersonal.heading("col2", text="Nombre", anchor=CENTER)
        self.treebuscarPersonal.heading("col3", text="Fecha de ingreso", anchor=CENTER)
        self.treebuscarPersonal.heading("col4", text="Previsión de salud", anchor=CENTER)
        self.treebuscarPersonal.heading("col5", text="Sueldo bruto", anchor=CENTER)
        self.treebuscarPersonal.heading("col6", text="Unidad administrativa", anchor=CENTER)
        self.treebuscarPersonal.heading("col7", text="Cargo", anchor=CENTER)
        self.treebuscarPersonal.place(x=350,y=100)
#--------------------------------------------------------------------------VENTANA BUSQUEDAS 2 ----------------------------------------------------------------------------------
class Ventana_Busquedas_2(Frame):

    busquedas=Busquedas()

    def __init__(self, master=None):
        super().__init__(master,width=1920, height=1080)
        self.master = master
        self.pack()
        self.CrearFrames()
        self.llenardatosSueldos()
        self.id=-1

    def vaciararbolSueldo(self):
        for item in self.treeSueldo.get_children():
            self.treeSueldo.delete(item)

    def llenardatosSueldos(self):
        self.vaciararbolSueldo()
        datos = self.busquedas.Sueldos_ordenados()      
        for row in datos:            
            self.treeSueldo.insert("",END,text=row[0], values=(row[1],row[2], row[3]))
    
    def vaciararbolFechas(self):
        for item in self.treeFechas.get_children():
            self.treeFechas.delete(item)

    def llenardatosFechas(self):
        self.vaciararbolFechas()
        datos = self.busquedas.fechas_tramos(self.tramo1.get(),int(self.tramo1.get())+10)        
        for row in datos:            
            self.treeFechas.insert("",END,text=row[0], values=(row[1],row[2], row[3]))
    
    def Exel_Sueldos_ordenados(self):
        datos=self.busquedas.Sueldos_ordenados()
        i=-1
        id,rut,nombre,sueldo,= [],[],[],[]
        for dato in datos:
            i=i+1
            id.append(datos[i][0])
            rut.append(datos[i][1])
            nombre.append(datos[i][2])
            sueldo.append(datos[i][3])
        fecha_archivo=str(strftime('%d-%m-%y_%H-%M-%S'))
        datos2={'Id': id,'Rut': rut,'Nombre': nombre,'Sueldo liquido': sueldo}
        df=pd.DataFrame(datos2)
        df.to_excel(rf'C:\Users\vicen\Desktop\n\Excel\Datos_Sueldos_Ordenados_{fecha_archivo}.xlsx')
        messagebox.showinfo('Informacion','Excel creado correctamente')

    def Exel_Fechas_ordenadas(self):
        datos=self.busquedas.Fecha_ingreso_personal()
        i=-1
        id,rut,nombre,fecha,= [],[],[],[]
        for dato in datos:
            i=i+1
            id.append(datos[i][0])
            rut.append(datos[i][1])
            nombre.append(datos[i][2])
            fecha.append(datos[i][3])
        fecha_archivo=str(strftime('%d-%m-%y_%H-%M-%S'))
        datos2={'Id': id,'Rut': rut,'Nombre': nombre,'Fecha de ingreso': fecha}
        df=pd.DataFrame(datos2)
        df.to_excel(rf'C:\Users\vicen\Desktop\n\Excel\Datos_Fechas_Ordenados_{fecha_archivo}.xlsx')
        messagebox.showinfo('Informacion','Excel creado con todas las fechas')

    def CrearFrames(self):
        frame1=Frame(self,bg="#708090")
        frame1.place(x=0,y=0,width=1920, height=1080)

        frameSueldo=Frame(frame1,bg="#708090")
        frameSueldo.place(x=0,y=0,width=1920, height=540)
#--------------------------------------------------------------------------TITULO----------------------------------------------------------------------------------
        tituloSueldo=Label(frameSueldo,text="Sueldos ordenados",bg="#6495ED",fg="#000000",font=("Garamond",30,"bold"))
        tituloSueldo.place(x=790,y=0,width=500, height=60)

        self.btnCrearExcelSueldo=Button(frameSueldo,text="Crear Excel", command=self.Exel_Sueldos_ordenados, bg="#6495ED", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnCrearExcelSueldo.place(x=650,y=30,width=100,height=30)

#--------------------------------------------------------------------------ARBOL----------------------------------------------------------------------------------
        self.treeSueldo=ttk.Treeview(frameSueldo,columns=("col1","col2","col3"),height=15)
        self.treeSueldo.column("#0",width=40)
        self.treeSueldo.column("col1",width=250, anchor=CENTER)
        self.treeSueldo.column("col2",width=250, anchor=CENTER)
        self.treeSueldo.column("col3",width=250, anchor=CENTER)

        self.treeSueldo.heading("#0", text="Id")
        self.treeSueldo.heading("col1", text="Rut", anchor=CENTER)
        self.treeSueldo.heading("col2", text="Nombre", anchor=CENTER)
        self.treeSueldo.heading("col3", text="Sueldo líquido", anchor=CENTER)
        self.treeSueldo.place(x=600,y=100)
#____________________________________________________________________________________________________________________________________________________________________
        frameFechas=Frame(frame1,bg="#708090")
        frameFechas.place(x=0,y=500,width=1920, height=540)
#--------------------------------------------------------------------------TITULO----------------------------------------------------------------------------------
        tituloFechas=Label(frameFechas,text="Fechas por tramos",bg="#6495ED",fg="#000000",font=("Garamond",30,"bold"))
        tituloFechas.place(x=790,y=0,width=500, height=60)

        self.btnbuscarPersonal=Button(frameFechas,text="Buscar", command=self.llenardatosFechas, bg="#2E8B57", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnbuscarPersonal.place(x=540,y=40,width=100,height=30)

        self.tramo1=ttk.Combobox(frameFechas,values=["1980","1990","2000","2010","2020"])
        self.tramo1.place(x=660,y=40,width=120,height=30)

        self.btnCrearExcelFechas=Button(frameFechas,text="Crear Excel", command=self.Exel_Fechas_ordenadas, bg="#6495ED", fg="white",font=("Blue Fonte",12,"bold"))
        self.btnCrearExcelFechas.place(x=1300,y=30,width=100,height=30)

#--------------------------------------------------------------------------ARBOL----------------------------------------------------------------------------------
        self.treeFechas=ttk.Treeview(frameFechas,columns=("col1","col2","col3"),height=15)
        self.treeFechas.column("#0",width=40)
        self.treeFechas.column("col1",width=250, anchor=CENTER)
        self.treeFechas.column("col2",width=250, anchor=CENTER)
        self.treeFechas.column("col3",width=250, anchor=CENTER)

        self.treeFechas.heading("#0", text="Id")
        self.treeFechas.heading("col1", text="Rut", anchor=CENTER)
        self.treeFechas.heading("col2", text="Nombre", anchor=CENTER)
        self.treeFechas.heading("col3", text="Fecha de ingreso", anchor=CENTER)
        self.treeFechas.place(x=600,y=100)

#--------------------------------------------------------------------------VENTANA BUSQUEDAS 3----------------------------------------------------------------------------------
class Ventana_Busquedas_3(Frame):

    busquedas=Busquedas()

    def __init__(self, master=None):
        super().__init__(master,width=1920, height=1080)
        self.master = master
        self.pack()
        self.CrearFrames()
        self.id=-1
        self.llenardatoscobros()
        self.llenardatosderivacion()
        self.llenardatosprevision()

    def vaciararbolcobros(self):
        for item in self.treeCobros.get_children():
            self.treeCobros.delete(item)

    def llenardatoscobros(self):
        self.vaciararbolcobros()
        datos = self.busquedas.Cobros_Ordenados()        
        for row in datos:            
            self.treeCobros.insert("",END,text=row[0], values=(row[1],row[2], row[3]))
    
    def vaciararbolderivacion(self):
        for item in self.treeCantidad.get_children():
            self.treeCantidad.delete(item)

    def llenardatosderivacion(self):
        self.vaciararbolderivacion()
        datos = self.busquedas.Cantidad_derivacion()        
        for row in datos:            
            self.treeCantidad.insert("",END,text=row[0], values=(row[1]))

    def vaciararbolprevision(self):
        for item in self.treeprevision.get_children():
            self.treeprevision.delete(item)

    def llenardatosprevision(self):
        self.vaciararbolprevision()
        datos = self.busquedas.Prevision_cantidad()      
        for row in datos:            
            self.treeprevision.insert("",END,text=row[0], values=(row[1]))

    def CrearFrames(self):
        frame1=Frame(self,bg="#B0E0E6")
        frame1.place(x=0,y=0,width=1920, height=1080)

        frameCobros=Frame(frame1,bg="#B0E0E6")
        frameCobros.place(x=0,y=0,width=1920, height=340)
#--------------------------------------------------------------------------TITULO----------------------------------------------------------------------------------
        tituloMedico=Label(frameCobros,text="Precios ordenados",bg="#4682B4",fg="#000000",font=("Garamond",30,"bold"))
        tituloMedico.place(x=0,y=0,width=1980, height=60)

#--------------------------------------------------------------------------ARBOL----------------------------------------------------------------------------------
        self.treeCobros=ttk.Treeview(frameCobros,columns=("col1","col2","col3"),height=5)
        self.treeCobros.column("#0",width=40)
        self.treeCobros.column("col1",width=150, anchor=CENTER)
        self.treeCobros.column("col2",width=150, anchor=CENTER)
        self.treeCobros.column("col3",width=150, anchor=CENTER)
         
        self.treeCobros.heading("#0", text="Id")
        self.treeCobros.heading("col1", text="Rut", anchor=CENTER)
        self.treeCobros.heading("col2", text="Nombre", anchor=CENTER)
        self.treeCobros.heading("col3", text="Cobro total", anchor=CENTER)
        self.treeCobros.place(x=750,y=100)
#____________________________________________________________________________________________________________________________________________________________________

        frameCantidad=Frame(frame1,bg="#B0E0E6")
        frameCantidad.place(x=0,y=330,width=1920, height=340)
#--------------------------------------------------------------------------TITULO----------------------------------------------------------------------------------
        titulotens=Label(frameCantidad,text="Cantidad de consulta o urgencia",bg="#4682B4",fg="#000000",font=("Garamond",30,"bold"))
        titulotens.place(x=0,y=0,width=1980, height=60)

#--------------------------------------------------------------------------ARBOL----------------------------------------------------------------------------------
        self.treeCantidad=ttk.Treeview(frameCantidad,columns=("col1"),height=4)
        self.treeCantidad.column("#0",width=150)
        self.treeCantidad.column("col1",width=150, anchor=CENTER)

        self.treeCantidad.heading("#0", text="Derivación")
        self.treeCantidad.heading("col1", text="Cantidad", anchor=CENTER)
        self.treeCantidad.place(x=850,y=100)
#____________________________________________________________________________________________________________________________________________________________________

        frameprevision=Frame(frame1,bg="#B0E0E6")
        frameprevision.place(x=0,y=650,width=1920, height=340)
#--------------------------------------------------------------------------TITULO----------------------------------------------------------------------------------
        tituloPersonal=Label(frameprevision,text="Cantidad de previsiones",bg="#4682B4",fg="#000000",font=("Garamond",30,"bold"))
        tituloPersonal.place(x=0,y=0,width=1980, height=60)

#--------------------------------------------------------------------------ARBOL----------------------------------------------------------------------------------
        self.treeprevision=ttk.Treeview(frameprevision,columns=("col1"),height=4)
        self.treeprevision.column("#0",width=150)
        self.treeprevision.column("col1",width=150, anchor=CENTER)
     
        self.treeprevision.heading("#0", text="Previsión de salud")
        self.treeprevision.heading("col1", text="Cantidad", anchor=CENTER)
        self.treeprevision.place(x=850,y=100)
#--------------------------------------------------------------------------FUNCION PRINCIPAL----------------------------------------------------------------------------------

def main():

    app = Ventana_Control()
    app.mainloop()
    
if __name__ == "__main__":
    main()

