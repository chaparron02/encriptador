# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 17:18:29 2020

@author: David Medina
"""

""" 
Formalizando uso de tkinter

"""

import tkinter as tk
import Aprender_wn as ap
import Cifrar_wn as cif

" Ventana principal "

# Creando un objeto tkinter
wn1 = tk.Tk()

# Tamñano de la ventama 
wn1.geometry("510x355+400+250")

# Titulo de la ventana 
wn1.title(" Cypher.Py ")

# Color de fondo de la ventana

wn1.config(bg = "DeepSkyBlue4")

wn1.resizable(False, False) # Bloquea la ventana a su tamaño definido
 
# wn1.iconbitmap(r"C:\Users\CiroFabian\Documents\Programacion Computadores\GIU_Proyecto\Seguridad.ICO")


# Definiendo funciones
    # Funciones alternas
def recolector(n, wn, col):
    text = n.get()
    a = tk.Label(wn,text = "Bienvenido"+" "+ text+ ", comenzemos a aprender") 
    a.config(bg = col)
    a.pack()

def etiqueta (wn,texto,bg,fg,font):
    e = tk.Label(wn,text =texto)
    e.config(bg = bg, fg= fg,font = font)
    e.pack()
    
def space(wn,col,n):
    for i in range(n):
        a = tk.Label(wn, text = " ")
        a.config(bg = col)
        a.pack()

def saludoA(nombre):
    print("Bienvenido" + nombre)
    
def hi3():
    return None


# Texto dentro de la ventana

tx1 = tk.Label(wn1, text = "Bienvenido a Cypher.Py",)
tx1.config(bg = "DeepSkyBlue4",fg = "grey1" , font = "Helvetica 14",pady= 12)
tx1.pack()

space(wn1, "DeepSkyBlue4",3)


# Definiendo botones ventana principal  

#------------------------------------------- Boton 1: Aprender

b1 = tk.Button(wn1, text = "Aprender cifrado", padx = 68, pady = 15, command =ap.aprender, 
               fg = "Darkorange3", bg = "old lace",activebackground="SeaGreen3")
b1.config(font = "Arial 12")
b1.pack(fill = tk.X)


#------------------------------------------- Boton 2: Cifrar/descifrar

b2 = tk.Button(wn1, text = "Cifrar/Descifrar mensaje", padx = 75, pady = 15, command = cif.cifrar ,
               fg = "Darkorange3", bg = "old lace",activebackground="navy")
b2.config(font = "Arial 12")
b2.pack(fill = tk.X)


#-------------------------------------------- Boton 4: Exit

b3 = tk.Button(wn1, text = "Salir", padx = 16, pady = 5,command = wn1.destroy,
               fg = "Darkorange3", bg = "old lace",activebackground="firebrick3")
b3.config(font = "Arial 8")
b3.pack(side = "bottom") 

# b4.place(x = 436,y = 318)


# Loop para que la ventana aguarde por instrucciones 
wn1.mainloop()
