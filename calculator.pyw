# CALCULADORA con tkinter

# importo las LIBRERIAs
from tkinter import *
from tkinter import messagebox   # ventanas emergentes

# creo las VARIABLEs para
operacion = ""       # guardar el tipo de operacion a realizar
dato = ""            # variable de control (operacion nueva "" / en curso " " )
resultado = 0.0      # resultado de la ultima operacion realizada

# creo la VENTANA
ventana = Tk()
ventana.title("kalculator")
ventana.resizable(0,0)

# creo un FRAME
miFrame = Frame(ventana)
miFrame.config(bg="orange")
miFrame.pack()

# creo el display o PANTALLA con un Entry -------------------------------
# y le asocio una VARIABLE
numeroEntry = StringVar()
numero = ""
pantalla = Entry(miFrame, textvariable=numeroEntry)
pantalla.grid(row=0,column=1, columnspan=4, padx=3,pady=3)
pantalla.config(bg="black", fg="#03f943", justify="right", font=("bold",12))

# creo una FUNCION para el pulsado de los BOTONES numericos -------------
def botonPulsado(numero):
    global dato
    if (numeroEntry.get() == "") and (numero == "0"):
        pass
    elif dato != "":
        if numero == "0":
            numeroEntry.set("")
        else:
            numeroEntry.set(numero)
        dato = ""
    elif dato == "":
        # agrego el numero pulsado al ya existente
        numeroEntry.set(numeroEntry.get() + numero)
  
# creo una FUNCION para el pulsado de los BOTONES decimal y signo -------
def decimal():
    global dato
    global resultado
    global operacion
    if dato == "" and numeroEntry.get() == "":
        numeroEntry.set("0.")
    else:
        if float(numeroEntry.get()) == resultado:
            print(numeroEntry.get())
            numeroEntry.set("0.")
            dato = ""
        else:
            numeroEntry.set(numeroEntry.get() + ".")

def signo():
    global dato
    global resultado
    global operacion
    if dato == "" and numeroEntry.get() == "":
        numeroEntry.set("-")
    else:
        if float(numeroEntry.get()) == resultado:
            print(numeroEntry.get())
            numeroEntry.set("-")
            dato = ""
        
   
# creo una FUNCION para el pulsado de los BOTONES borrar ----------------
def borrarT():
    operacion = ""
    dato = ""
    resultado = 0
    numeroEntry.set("")

def borrarCE():
    lista = []
    lista.extend(numeroEntry.get())
    lista.pop()
    numeroEntry.set("")
    for numero in lista:
        numeroEntry.set(numeroEntry.get() + numero)
    

# creo una FUNCION para el pulsado de los BOTONES de operaciones --------
def suma(numero):
    global operacion
    global dato
    global resultado
    operacion = "suma"
    dato = " "
    resultado += numero
    numeroEntry.set(resultado)

def resta(numero):
    global operacion
    global dato
    global resultado
    if operacion == "":
        resultado = float(numero)
        operacion = "resta"
        dato = " "
    numeroEntry.set(resultado)

def multiplicacion(numero):
    global operacion
    global dato
    global resultado
    if operacion == "":
        resultado = float(numero)
        operacion = "multiplicacion"
        dato = " "
    numeroEntry.set(resultado)

def division (numero):
    global operacion
    global dato
    global resultado
    if operacion == "":
        resultado = float(numero)
        operacion = "division"
        dato = " "
    numeroEntry.set(resultado)
    
def igual():
    global resultado
    global operacion
    global dato
    if operacion == "resta":
        resultado = resultado - float(numeroEntry.get())
        numeroEntry.set(resultado)
    elif operacion == "multiplicacion":
        resultado = resultado * float(numeroEntry.get())
        numeroEntry.set(resultado)
    elif operacion == "division":
        if numeroEntry.get()=="" or float(numeroEntry.get())==0.0:
            messagebox.showwarning("kalculator", "NO es posible DIVIDIR por CERO")
        else:
            resultado = resultado / float(numeroEntry.get())
            numeroEntry.set(resultado)
    else:
        numeroEntry.set(resultado + float(numeroEntry.get()))
    operacion = ""
    dato = ""
    resultado = 0
    
        
    
# creo los BOTONES de la 1er. fila --------------------------------------
botonCE = Button(miFrame, text="CE", width=3, command=borrarCE)
botonCE.grid(row=1,column=1, padx=3,pady=3)

botonC = Button(miFrame, text="C", width=9, command=borrarT)
botonC.grid(row=1,column=2, columnspan=2, padx=3,pady=3)

botonIgual = Button(miFrame, text="=", width=3, command=lambda:igual())
botonIgual.grid(row=1,column=4, padx=3,pady=3)

# creo los BOTONES de la 2da. fila -------------------------------------
boton7 = Button(miFrame, text="7", width=3, command=lambda:botonPulsado("7"))
boton7.grid(row=2,column=1, padx=3,pady=3)

boton8 = Button(miFrame, text="8", width=3, command=lambda:botonPulsado("8"))
boton8.grid(row=2,column=2, padx=3,pady=3)

boton9 = Button(miFrame, text="9", width=3, command=lambda:botonPulsado("9"))
boton9.grid(row=2,column=3, padx=3,pady=3)

botonMult = Button(miFrame, text="x", width=3, command=lambda:multiplicacion(float(numeroEntry.get())))
botonMult.grid(row=2,column=4, padx=3,pady=3)

# creo los BOTONES de la 3er. fila -------------------------------------
boton4 = Button(miFrame, text="4", width=3, command=lambda:botonPulsado("4"))
boton4.grid(row=3,column=1, padx=3,pady=3)

boton5 = Button(miFrame, text="5", width=3, command=lambda:botonPulsado("5"))
boton5.grid(row=3,column=2, padx=3,pady=3)

boton6 = Button(miFrame, text="6", width=3, command=lambda:botonPulsado("6"))
boton6.grid(row=3,column=3, padx=3,pady=3)

botonDiv = Button(miFrame, text="/", width=3, command=lambda:division(float(numeroEntry.get())))
botonDiv.grid(row=3,column=4, padx=3,pady=3)

# creo los BOTONES de la 4ta. fila -------------------------------------
boton1 = Button(miFrame, text="1", width=3, command=lambda:botonPulsado("1"))
boton1.grid(row=4,column=1, padx=3,pady=3)

boton2 = Button(miFrame, text="2", width=3, command=lambda:botonPulsado("2"))
boton2.grid(row=4,column=2, padx=3,pady=3)

boton3 = Button(miFrame, text="3", width=3, command=lambda:botonPulsado("3"))
boton3.grid(row=4,column=3, padx=3,pady=3)

botonSum = Button(miFrame, text="+", width=3, command=lambda:suma(float(numeroEntry.get())))
botonSum.grid(row=4,column=4, padx=3,pady=3)


# creo los BOTONES de la 5ta. fila -------------------------------------
boton0 = Button(miFrame, text="0", width=3, command=lambda:botonPulsado("0"))
boton0.grid(row=5,column=1, padx=3,pady=3)

botonComa = Button(miFrame, text=",", width=3, command=decimal)
botonComa.grid(row=5,column=2, padx=3,pady=3)

botonSigno = Button(miFrame, text="+/-", width=3, command=signo)
botonSigno.grid(row=5,column=3, padx=3,pady=3)

botonResta = Button(miFrame, text="-", width=3, command=lambda:resta(float(numeroEntry.get())))
botonResta.grid(row=5,column=4, padx=3,pady=3)



# creo el BULCE principal  ---------------------------------------------
ventana.mainloop()
