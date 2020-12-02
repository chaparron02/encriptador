# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 10:24:57 2020

@author: David Medina
"""

import tkinter as tk
import encriptadores as cy

" Modulo para controlar la funcion de cifrar de la ventana inicial "

# Funcion para agregar espacios
def space(wn,col,n):
    for i in range(n):
        a = tk.Label(wn, text = " ")
        a.config(bg = col)
        a.pack()
        
# Funcion para definir una etiqueta        
def etiquetaimportante (wn,texto,X,Y):
    e = tk.Label(wn,text =texto)
    e.config(font ="Arial 12" ,fg = "red",bg ="LightBlue2")
    e.place(x=X,y=Y )

# Funcion para el boton encriptar
def Encriptar(n0,n1,n2):
    wn = tk.Toplevel()
    wn.title("Cypher: Codigo")
    textmes = n0.get()
    textmet= n1.get()
    textkey= n2.get()
    
    mensaje = str(textmes)
    llave = int(textkey)
    modo = "encrypt"
    metodo =str(textmet).lower() 
    
    if metodo == "cesar":
        
        x = cy.cesarCypher(mensaje,llave,modo)
        et0 = tk.Label(wn,text = "Codigo encriptado:") 
        et0.config(font = "Arial 10", fg= "red")
        
        bet = tk.Entry(wn,fg = "red")
        bet.insert(0,x) 
        bet.config(font = "Helvetica 12", fg= "red") 
        
        et0.pack(side = "top")
        bet.pack(side = "left")
        
         
    elif metodo == "cesar rev" or modo == "cesar_rev" :
        x = cy.Cesar_rev(mensaje,llave,modo)
        et0 = tk.Label(wn,text = "Codigo encriptado:") 
        et0.config(font = "Arial 10", fg= "red")
        
        bet = tk.Entry(wn,fg = "red")
        bet.insert(0,x) 
        bet.config(font = "Helvetica 12", fg= "red") 
        
        et0.pack(side = "top")
        bet.pack(side = "left")
        
    elif metodo == "trasp" or modo == "trasposicion":
        x = cy.cifrado_transposicion(mensaje,llave,modo)
        et0 = tk.Label(wn,text = "Codigo encriptado:") 
        et0.config(font = "Arial 10", fg= "red")
        
        bet = tk.Entry(wn,fg = "red")
        bet.insert(0,x) 
        bet.config(font = "Helvetica 12", fg= "red") 
        
        et0.pack(side = "top")
        bet.pack(side = "left")
    else:
        et0 = tk.Label(wn,text = "Metodo"+ " " + metodo + " " +"desconocido")
        et0.grid(row=5,column=1)


# Funcion para el boton desencriptar

def Desencriptar(n0,n1,n2):
    wn = tk.Toplevel()
    wn.title("Cypher: Codigo")
    
    textmes = n0.get()
    textmet= n1.get()
    textkey= n2.get()
    
    mensaje = str(textmes)
    llave = int(textkey)
    modo = "decrypt"
    metodo =str(textmet).lower() 
    
    if metodo == "cesar":
        
        x = cy.cesarCypher(mensaje,llave,modo)
        et0 = tk.Label(wn,text = "Codigo encriptado:") 
        et0.config(font = "Arial 10", fg= "red")
        
        bet = tk.Entry(wn,fg = "red")
        bet.insert(0,x) 
        bet.config(font = "Helvetica 12", fg= "red") 
        
        et0.pack(side = "top")
        bet.pack(side = "left")
        
         
    elif metodo == "cesar rev" or modo == "cesar_rev" :
        x = cy.Cesar_rev(mensaje,llave,modo)
        et0 = tk.Label(wn,text = "Codigo encriptado:") 
        et0.config(font = "Arial 10", fg= "red")
        
        bet = tk.Entry(wn,fg = "red")
        bet.insert(0,x) 
        bet.config(font = "Helvetica 12", fg= "red") 
        
        et0.pack(side = "top")
        bet.pack(side = "left")
        
    elif metodo == "trasp" or modo == "trasposicion":
        x = cy.cifrado_transposicion(mensaje,llave,modo)
        et0 = tk.Label(wn,text = "Codigo encriptado:") 
        et0.config(font = "Arial 10", fg= "red")
        
        bet = tk.Entry(wn,fg = "red")
        bet.insert(0,x) 
        bet.config(font = "Helvetica 12", fg= "red") 
        
        et0.pack(side = "top")
        bet.pack(side = "left")
    
    else:
        et0 = tk.Label(wn,text = "Metodo"+ " " + metodo + " " +"desconocido")
        et0.grid(row=5,column=1)




# Funcion principal para control de ventana cifrar
    
def cifrar():
    wn2 = tk.Toplevel()
    wn2.geometry("510x355+400+250")
    wn2.title(" Cypher.Py : Cifrar mensaje")
    wn2.config(bg = "LightBlue2")
    wn2.resizable(False, False)
    
    # Texto en la ventana
    
    sub_mensaje = tk.Label(wn2, text = " Ingrese el mensaje a cifrar: " )
    sub_mensaje.config(bg = "LightBlue2")
    sub_mensaje.grid(row = 0, column =0)
    sub2_mensaje = tk.Label(wn2, text = "Ej: Hola ")
    sub2_mensaje.config(bg = "LightBlue2")
    sub2_mensaje.grid(row = 0, column =3)
    
    
    sub_cifrado = tk.Label(wn2, text = " Metodo de cifrado a utilizar: " )
    sub_cifrado.config(bg = "LightBlue2")
    sub_cifrado.grid(row = 1, column =0)
    sub2_cifrado = tk.Label(wn2, text = "Como: Cesar, Cesar rev, Trasp" )
    sub2_cifrado.config(bg = "LightBlue2")
    sub2_cifrado.grid(row = 1, column =3)
    
    
    sub_key = tk.Label(wn2, text = "Llave a utilizar en el cifrado:" )
    sub_key.config(bg = "LightBlue2")
    sub_key.grid(row = 2, column =0)
    sub2_key = tk.Label(wn2, text = "Ej: 1,2,3,..., MAX 99 " )
    sub2_key.config(bg = "LightBlue2")
    sub2_key.grid(row = 2, column =3)
    
    
    
    
    # Cajas de texto de la venta 
    box_mensaje = tk.Entry(wn2, font = "Garamond 12", borderwidth = 5, justify = "center")
    box_mensaje.focus()
    box_mensaje.grid(row = 0, column =1)
    
    box_metodo = tk.Entry(wn2, font = "Garamond 12", borderwidth = 5, justify = "center")
    box_metodo.grid(row = 1, column =1)
    
    box_key = tk.Entry(wn2, font = "Garamond 12", borderwidth = 5, justify = "center")
    box_key.grid(row = 2, column =1)
    
    
    
    # Botones de la ventana
    
    boton_encriptar =tk.Button(wn2, text = " Encriptar  ",command = lambda:(Encriptar(box_mensaje,box_metodo,box_key),etiquetaimportante(wn2,"Guarda la llave, la necesitaras para desencriptar el mensaje",50,130))) 
    boton_encriptar.config(padx = 25, pady = 5,fg = "Darkorange3", bg = "snow",activebackground="firebrick3")
    boton_encriptar.place(x =140 , y = 96)
    
    
    boton_desencriptar =tk.Button(wn2, text = "Desencriptar",command = lambda:Desencriptar(box_mensaje,box_metodo,box_key)) 
    boton_desencriptar.config(padx = 16, pady = 5,fg = "Darkorange3", bg = "snow",activebackground="firebrick3")
    boton_desencriptar.place(x =260 , y = 95)
    
    
    boton_atras =tk.Button(wn2, text = "Atras",command = wn2.destroy)
    boton_atras.config(padx = 16, pady = 5,fg = "Darkorange3", bg = "snow",activebackground="firebrick3",
                       font = "Arial 12")
    boton_atras.place(x =215 , y = 315)
    
