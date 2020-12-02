# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:04:09 2020

@author: chaparron02
"""

import math


def cesarCypher(mensaje,llave,modo):
#ahora se implementa un input con el fin de recibir el mensaje a encriptar
 "info del usuario"
 
 mensaje = str(mensaje)
 llave = int(llave) #la llave es la que encripta el mensaje siendo el numero de veces que la letra se mueve en el abecedario
 modo = str(modo) #se usa para saber si el usuario desea desencriptar el mensaje o encriptarlo

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
           traduccion = "formato no valido"
           return traduccion
        
        if translatedindex >=len(codes):
            translatedindex = translatedindex - len(codes)
    
        elif translatedindex < 0:
          translatedindex = translatedindex + len(codes)
        
        
        traduccion = traduccion + codes[translatedindex]
        
   
    else:
        traduccion = traduccion + symbol
        
 if modo == "encriptar" or modo == "encrypt" :       
      return traduccion
     
 elif modo == "desencriptar" or modo =="decrypt":
     
     traduccion
     return traduccion



def reverse(): #codigo que se utiliza para darle la vuelta a un mensaje. Ej: hola se convierte en aloh
    
 mensaje = input("escriba su mensaje: ")
 traduccion = ''
 
 i = len(mensaje) - 1
 while i >= 0:
  traduccion = traduccion + mensaje[i]
  i = i - 1
 return traduccion    


# Variacion cifrado cesar: cifrado y cifrado invertido     
def Cesar_rev (mensaje,llave,modo):
    
    mensaje = str(mensaje)
    llave = int(llave) 
    modo = str(modo)
    
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
        traduccion
        return traduccion
     
    elif modo == "desencriptar" or modo =="decrypt":
     
        traduccion
        return traduccion
       
# cifrado de transposicion

def cifrado_transposicion(mensaje,llave,modo):
    
    mensaje = str(mensaje)
    llave = int(llave) 
    modo = str(modo)
    
    
    if modo == "encriptar":
       ciphertext = [""] * llave
       for column in range(llave):
        currentindex= column
        while currentindex < len(mensaje):
         ciphertext[column] += mensaje[currentindex]
         currentindex += llave
       traduccion = ''.join(ciphertext)
       traduccion
       return traduccion
     
    if modo == "desencriptar":
       numofcolumns = int(math.ceil(len(mensaje) / float(llave)))
       numofrows = llave
       boxes = (numofcolumns * numofrows) - len(mensaje)
       plaintext = [''] * numofcolumns
       column = 0
       row= 0
       for symbol in mensaje:
         plaintext[column] += symbol
         column += 1
         if (column == numofcolumns) or (column == numofcolumns - 1 and row >= numofrows - boxes):
          column = 0
          row += 1
       traduccion = ''.join(plaintext)
       traduccion
       return traduccion
    
