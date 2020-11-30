# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:04:09 2020

@author: chaparron02
"""

import math


def cesarCypher():
#ahora se implementa un input con el fin de recibir el mensaje a encriptar
 "info del usuario"
 
 mensaje = input("Mensaje: ")
 llave = int(input("¿Que llave desea usar? ")) #la llave es la que encripta el mensaje siendo el numero de veces que la letra se mueve en el abecedario
 modo = input("Desea encriptar o desencriptar:  ") #se usa para saber si el usuario desea desencriptar el mensaje o encriptarlo

 "Caracteres a intercambiar"
 
 codes= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890.,?¿ ¡!"
 traduccion = ""  #recibe el mensaje traducido

 "codigo cesar"

 for symbol in mensaje:
    if symbol in codes:
        symbolindex = codes.find(symbol)
        
        if modo == "encriptar" or modo == "encrypt":
         translatedindex = int(symbolindex + llave)
         
        elif modo == "desencriptar" or modo =="decrypt":
            translatedindex =  int(symbolindex - llave)
            
        else:
            print("formato no valido")

        
        if translatedindex >=len(codes):
            translatedindex = translatedindex - len(codes)
    
        elif translatedindex < 0:
          translatedindex = translatedindex + len(codes)
        
        
        traduccion = traduccion + codes[translatedindex]
        
   
    else:
        traduccion = traduccion + symbol
        
 if modo == "encriptar" or modo == "encrypt" :       
     print("el codigo encriptado es: {0} con llave {1}".format(traduccion,llave))
     
 elif modo == "desencriptar" or modo =="decrypt":
     
     print("El codigo traducido es: ",traduccion)
    
    



def reverse(): #codigo que se utiliza para darle la vuelta a un mensaje. Ej: hola se convierte en aloh
    
 mensaje = input("escriba su mensaje: ")
 traduccion = ''
 
 i = len(mensaje) - 1
 while i >= 0:
  traduccion = traduccion + mensaje[i]
  i = i - 1
 print(traduccion)
 


    

# Variacion cifrado cesar: cifrado y cifrado invertido     
def Cesar_rev ():
    
    mensaje = input("Mensaje: ")
    llave = int(input("¿Que llave desea usar? "))
    modo = input("Desea encriptar o desencriptar:  ")
    codes = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890.,?¿ ¡!"
    trad = ""
    
    for symbol in mensaje:
        if symbol in codes:
            symbolindex = codes.find(symbol)

            if modo == "encriptar" or modo == "encrypt":
                translatedindex = int(symbolindex + llave)
         
            elif modo == "desencriptar" or modo =="decrypt":
                translatedindex =  int(symbolindex - llave)
            
            else:
                print("formato no valido")

        
            if translatedindex >=len(codes):
                translatedindex = translatedindex - len(codes)
    
            elif translatedindex < 0:
                translatedindex = translatedindex + len(codes)
        
        
            trad = trad + codes[translatedindex]
        
   
        else:
            trad = trad + symbol
    
    # Combinando cesarCypher con reverse
    mensaje = trad
    traduccion = ''
 
    i = len(mensaje) - 1
    while i >= 0:
        traduccion = traduccion + mensaje[i]
        i = i - 1
    
    # Impresion final
    if modo == "encriptar" or modo == "encrypt" :       
        print("el codigo encriptado es: {0} con llave {1}".format(traduccion,llave))
     
    elif modo == "desencriptar" or modo =="decrypt":
     
       print("El codigo traducido es: ",traduccion)
       
# cifrado de transposicion

def cifrado_transposicion():
    message= input("escriba su mensaje: ")
    key= input ("digite su llave: ")
    key=int(key)
    modo = input("diga si encriptar o desencriptar: ")
    if modo == "encriptar":
       ciphertext = [""] * key
       for column in range(key):
        currentindex= column
        while currentindex < len(message):
         ciphertext[column] += message[currentindex]
         currentindex += key
       cifrado = ''.join(ciphertext)
       print(cifrado)
     
    if modo == "desencriptar":
       numofcolumns = int(math.ceil(len(message) / float(key)))
       numofrows = key
       boxes = (numofcolumns * numofrows) - len(message)
       plaintext = [''] * numofcolumns
       column = 0
       row= 0
       for symbol in message:
         plaintext[column] += symbol
         column += 1
         if (column == numofcolumns) or (column == numofcolumns - 1 and row >= numofrows - boxes):
          column = 0
          row += 1
       cifrado = ''.join(plaintext)
       print(cifrado)
     