# AGENDA de CELULARES

# importo las LIBRERIAS p/ INTERFACES GRAFICAS y CONEXION a bases de datos
from tkinter import *
from tkinter import messagebox
import sqlite3


# FUNCIONES --------------------------------------------------------------------

# funcion para CREAR/agregar REGISTROS en la base de datos
def crear():
    conexion = sqlite3.connect("celularesBBDD")
    miCursor = conexion.cursor()
    datos = nombre.get(), apellido.get(), celular.get(), mail.get(), notasText.get("1.0",END)
    miCursor.execute("INSERT INTO REGISTROS VALUES (NULL,?,?,?,?,?)",(datos))
    # un modo de reemplazar las 2 ultimas instrucciones
    ''' miCursor.execute("INSERT INTO REGISTROS VALUES (NULL, '" + nombre.get() +
                     "' , '" + apellido.get() +
                     "', '" + celular.get() +
                     "', '" + mail.get() +
                     "', '" + notasText.get("1.0", END) + "')") '''
    conexion.commit()
    messagebox.showinfo("CELULARES bbdd", "registro INSERTADO en la base de datos")
    limpiarCampos()

# funcion para ACTUALIZAR REGISTROS en la base de datos
def actualizar():
    conexion = sqlite3.connect("celularesBBDD")
    miCursor = conexion.cursor()
    datos = nombre.get(), apellido.get(), celular.get(), mail.get(), notasText.get("1.0",END)
    miCursor.execute("UPDATE REGISTROS SET nombre=?, apellido=?, NumCelular=?, eMail=?, notas=? WHERE ID=" + idregistro.get(), (datos))
    # un modo de reemplazar las 2 ultimas instrucciones
    ''' miCursor.execute("UPDATE REGISTROS SET Nombre='" + nombre.get() +
                     "', Apellido='" + apellido.get() +
                     "', NumCelular='" + celular.get() +
                     "', eMail='" + mail.get() +
                     "', notas='" + notasText.get("1.0", END) +
                     "' WHERE ID=" + idregistro.get()) '''
    conexion.commit()
    messagebox.showinfo("CELULARES bbdd", "registro ACTUALIZADO en la base de datos")
    limpiarCampos()

# funcion para BORRAR REGISTROS en la base de datos
def borrar():
    respuesta = messagebox.askquestion("CELULARES bbdd - BORRAR Registro", "esta seguro de BORRAR este registro ?...")
    if respuesta == "yes":
        conexion = sqlite3.connect("celularesBBDD")
        miCursor = conexion.cursor()
        miCursor.execute("DELETE FROM REGISTROS WHERE ID=" + idregistro.get())
        conexion.commit()
        messagebox.showinfo("CELULARES bbdd", "registro BORRADO de la base de datos")
        limpiarCampos()

# funciones para LEER REGISTROS en la base de datos
def buscar():
    notasText.delete(1.0, END)
    conexion = sqlite3.connect("celularesBBDD")
    miCursor = conexion.cursor()
    miCursor.execute("SELECT ID,Nombre,Apellido FROM REGISTROS WHERE Apellido='" + apellido.get() + "'")
    registro = miCursor.fetchall()
    for campo in registro:
        notasText.insert(1.0,campo[0],"- ",campo[1])
        notasText.insert(1.0,"\n")
    conexion.commit()

def buscarID():
    notasText.delete(1.0, END)
    conexion = sqlite3.connect("celularesBBDD")
    miCursor = conexion.cursor()
    miCursor.execute("SELECT * FROM REGISTROS WHERE ID=" + idregistro.get())
    registro = miCursor.fetchall()
    for campo in registro:
        idregistro.set(campo[0])
        nombre.set(campo[1])
        apellido.set(campo[2])
        celular.set(campo[3])
        mail.set(campo[4])
        notasText.insert(1.0,campo[5])
    conexion.commit()
    
# funcion p/ LIMPIAR los CAMPOS de los ENTRY y TEXT
def limpiarCampos():
    idregistro.set("")
    nombre.set("")
    apellido.set("")
    celular.set("")
    mail.set("")
    notasText.delete(1.0, END)

# funcion p/ realizar la CONEXION a la BASE DE DATOS 
# donde creo la TABLA "REGISTROS" de 6 campos
def crearBBDD():
    conexion = sqlite3.connect("celularesBBDD")
    miCursor = conexion.cursor()
    try:
        miCursor.execute('''
                         CREATE TABLE REGISTROS (
                         ID INTEGER PRIMARY KEY AUTOINCREMENT,
                         Nombre VARCHAR(50),
                         Apellido VARCHAR(50),
                         NumCelular VARCHAR(25) UNIQUE,
                         eMail VARCHAR(50),
                         notas VARCHAR(100))
                         ''')
        messagebox.showinfo("CELULARES bbdd", "BBDD creada")
    except:
        messagebox.showwarning("CELULARES bbdd", "La BBDD ya existe.")

def salir():
    respuesta = messagebox.askquestion("CELULARES bbdd - SALIR", "desea salir SIN guardar cambios ?...")
    if respuesta == "yes":
        ventana.destroy()


# creo una VENTANA -------------------------------------------------------------
ventana = Tk()
ventana.title("Agenda de CELULARES")
ventana.resizable(width=False,height=False)


# creo una VARIABLE para alojar un MENU ----------------------------------------
barraMenu = Menu(ventana)
ventana.config(menu=barraMenu, width=250, heigh=250)

# creo las OPCIONES de la BARRA del MENU
crudMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="C.R.U.D.", menu=crudMenu)
crudMenu.add_command(label="Create", command=crear)
crudMenu.add_command(label="Read - Search ID")
crudMenu.add_command(label="Update")
crudMenu.add_command(label="Delete")

deleteMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="clean", menu=deleteMenu)
deleteMenu.add_command(label="CLEAN Entry/Text", command=limpiarCampos)

bbddMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="bbdd", menu=bbddMenu)
bbddMenu.add_command(label="Crear", command=crearBBDD)
bbddMenu.add_command(label="Salir", command=quit)

helpMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="help", menu=helpMenu)
helpMenu.add_command(label="Documents")
helpMenu.add_command(label="About ...")

# creo un FRAME para CUADROS DE TEXTO (Entry/Text) dentro de la VENTANA --------
cuadrosFrame = Frame(ventana, width=250, heigh=250)
cuadrosFrame.pack()
#cuadrosFrame.config(bg="")


# creo los LABEL con sus respectivos ENTRY y VARIABLES ASOCIADAS ---------------
idLabel = Label(cuadrosFrame, text="ID (solo lectura):", fg="black")
idLabel.grid(row=1, column=1, sticky="e")
idregistro = StringVar()
idEntry = Entry(cuadrosFrame, textvariable=idregistro, fg="red", justify="center")
idEntry.grid(row=1, column=2)
#idEntry.configure(state="readonly")

nombreLabel = Label(cuadrosFrame, text="Nombre:", fg="black")
nombreLabel.grid(row=2, column=1, sticky="e")
nombre = StringVar()
nombreEntry = Entry(cuadrosFrame, textvariable=nombre)
nombreEntry.grid(row=2, column=2)

apellidoLabel = Label(cuadrosFrame, text="Apellido:", fg="black")
apellidoLabel.grid(row=3, column=1, sticky="e")
apellido = StringVar()
apellidoEntry = Entry(cuadrosFrame, textvariable=apellido)
apellidoEntry.grid(row=3, column=2)

celularLabel = Label(cuadrosFrame, text="N° celular:", fg="black")
celularLabel.grid(row=4, column=1, sticky="e")
celular = StringVar()
celularEntry = Entry(cuadrosFrame, textvariable=celular)
celularEntry.grid(row=4, column=2)

mailLabel = Label(cuadrosFrame, text="email:", fg="black")
mailLabel.grid(row=5, column=1, sticky="e")
mail = StringVar()
mailEntry = Entry(cuadrosFrame, textvariable=mail)
mailEntry.grid(row=5, column=2)

# creo un TEXT con su respectivo LABEL
notasLabel = Label(cuadrosFrame, text="notas:", fg="black")
notasLabel.grid(row=6, column=1, sticky="e")
notasText = Text(cuadrosFrame, width=16, heigh=7)
notasText.grid(row=6, column=2, pady=10)
scrollVert = Scrollbar(cuadrosFrame, command=notasText.yview)
scrollVert.grid(row=6, column=3, pady=10, sticky="nsew")
notasText.config(yscrollcommand=scrollVert.set)


# creo un FRAME para los BOTONES dentro de la VENTANA --------------------------
botonesFrame = Frame(ventana, width=250, heigh=70)
botonesFrame.pack()
botonesFrame.config(bg="yellow")

createButton = Button(botonesFrame, text="Create", command=crear)
createButton.grid(row=1, column=1, padx=10, pady=10)

updateButton = Button(botonesFrame, text="Update", command=actualizar)
updateButton.grid(row=1, column=2, padx=10, pady=10)

deleteButton = Button(botonesFrame, text="Delete", command=borrar)
deleteButton.grid(row=1, column=3, padx=10, pady=10)

readButton = Button(botonesFrame, text="Search", command=buscar)
readButton.grid(row=2, column=1, padx=10, pady=10)

readButton = Button(botonesFrame, text="Search ID", command=buscarID)
readButton.grid(row=2, column=2, padx=10, pady=10)

salirButton = Button(botonesFrame, text=" EXIT ", command=salir)
salirButton.grid(row=2, column=3, padx=10, pady=10)






# creo el BUCLE PRINCIPAL ------------------------------------------------------
ventana.mainloop()

