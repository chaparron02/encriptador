# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 08:51:01 2020

@author: David Medina
"""

import tkinter as tk
import Aprender_wn2 as ap2

" Configuracion boton Aprender de la ventana principal "



def etiqueta (wn,texto,bg,fg,font):
    e = tk.Label(wn,text =texto)
    e.config(bg = bg, fg= fg,font = font)
    e.pack()
    
    
def space(wn,col,n):
    for i in range(n):
        a = tk.Label(wn, text = " ")
        a.config(bg = col)
        a.pack()

    
" Funcion principal boton aprender "

def aprender():
    wn2 = tk.Toplevel()
    wn2.geometry("510x355+400+250")
    wn2.config(bg = "PaleGreen1")
    wn2.title(" Cypher.Py: Aprendiendo cifrado ")
    wn2.resizable(False, False)
    
    space(wn2, "PaleGreen1",1)
    
    etiqueta(wn2, "Aprendamos algo sobre cifrado", "PaleGreen1", None, "Garamon 18")
   
    space(wn2, "PaleGreen1",1)
    
    etiqueta(wn2, "Para iniciar, ingresa tu nombre", "PaleGreen1", None, "Garamond 15")
    
    space(wn2, "PaleGreen1",1)
    
    # Botones para la ventana aprender
    
    box1 = tk.Entry(wn2, font = "Arial 15", borderwidth = 5, justify = "center")
    box1.focus()
    box1.pack()
    
    
    boton21 =tk.Button(wn2, text = "Siguiente",command = lambda: ap2.refresh(box1,wn2)) 
    boton21.pack()
    
    
    