import re
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sql import *
from tkcalendar import DateEntry
from datetime import datetime
from time import strftime

#----------------------------------------------------------------------------------VENTANA CONTROL----------------------------------------------------------------------------------  
class Ventana_Control(Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión departamento de Informatica")
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

        self.frame_actual = Ventana_Principal(self)

    def mostrar_ventana_pacientes(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()

        self.frame_actual = Ventana_Principal(self)

    def mostrar_ventana_personal(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()

        self.frame_actual = Ventana_personal(self)

    def mostrar_ventana_pago_personal(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()

        self.frame_actual = Ventana_Principal(self)
    
    def mostrar_ventana_cobro_paciente(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()
        self.frame_actual = Ventana_Principal(self)

    def mostrar_ventana_busquedas1(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()
        self.frame_actual = Ventana_Busquedas_1(self)
    
    def mostrar_ventana_busquedas2(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()
        self.frame_actual = Ventana_Principal(self)

    def mostrar_ventana_busquedas3(self):
        if self.frame_actual:
            self.frame_actual.pack_forget()
        self.frame_actual = Ventana_Principal(self)

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
def main():

    app = Ventana_Control()
    app.mainloop()
    
if __name__ == "__main__":
    main()