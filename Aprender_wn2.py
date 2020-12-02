# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:34:55 2020

@author: David Medina
"""

import tkinter as tk

def saludo(box, wn):
    text = box.get()
    a = tk.Label(wn,text = "Bienvenido"+" "+ text + ", comenzemos a aprender") 
    a.config(bg = "PaleGreen1" , font = "Arial 12")
    a.place(x = 0, y = 5)
    
def etiqueta (wn,texto,bg,fg,font,x,y):
    e = tk.Label(wn,text =texto)
    e.config(bg = bg, fg= fg,font = font)
    e.place(x = x, y= y)
    
def refresh(box,wn):
    wn3= tk.Toplevel()
    wn3.geometry("510x355+400+250")
    wn3.config(bg = "PaleGreen1")
    wn3.title(" Cypher.Py: Aprendiendo cifrado ")
    wn3.resizable(False, False)
    saludo(box, wn3)
    wn.destroy()
    
    # Texto introducido en la nueva ventana
    i = 28
    
    etiqueta(wn3,"Cifrar consiste en  crear escritos  que  dificulten  su  lectura mediante el empleo de",
                "PaleGreen1",None,"Arial 9",0,i+10)
    
    etiqueta(wn3,"letras, simbolos o numeros dispuestos de tal forma que solo quien conozca la clave",
                "PaleGreen1",None,"Arial 9",0,i*2+8)
    
    etiqueta(wn3,"necesaria  pueda descifrarlo.  Los primeros ecriptadores  de  la historia datan de la",
                "PaleGreen1",None,"Arial 9",0,i*3+5)
    
    etiqueta(wn3,"espartana y sus escitalas. Hoy en día existen inumerables formas de cifrar mensajes",
                "PaleGreen1",None,"Arial 9",0,i*4+5)
    
    etiqueta(wn3,"sin embargo para comprender lo que es cifrar presentaremos unos breves y sencillos",
                "PaleGreen1",None,"Arial 9",0,i*5+3)
    
    etiqueta(wn3,"ejemplos de cifrado.",
                "PaleGreen1",None,"Arial 9",0,i*6)
    
    etiqueta(wn3,"El cifrado basico es el cifrado Cesar, el cual es un tipo de cifrado por desplazamiento el ",
                "PaleGreen1",None,"Arial 9",0,i*7)
    
    etiqueta(wn3,"cual consiste en remplazar la letra del texto original por una que se encuentra determinadas",
                "PaleGreen1",None,"Arial 9",0,i*8)
    
    etiqueta(wn3,"posiciones (llave) mas adelante en el alfabeto o de una cadena de caracteres establecida.",
                "PaleGreen1",None,"Arial 9",0,i*9)
    
    etiqueta(wn3,"EJEMPLO :  `Hola`, usando este cifrado con una llave 3 tendremos como resultado la",
                "PaleGreen1",None,"Arial 9",0,i*10+5)
    
    etiqueta(wn3,"palabra krñd. De esta forma se aplica para cualquie mensaje, permitiendonos ocultar ",
                "PaleGreen1",None,"Arial 9",0,i*11+3)
    
    etiqueta(wn3,"informacion importante de cualquier intruso.",
                "PaleGreen1",None,"Arial 9",0,i*12+1)
    