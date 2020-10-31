# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:04:09 2020

@author: chaparron02
"""




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
 

# Brute-force para cifrado cesar clasico
def HackCesar ():
    message = str(input(" Mensaje a descifrar: "))
    
    symbols = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890.,?¿ ¡!" 
    
    # La cadena symbols debe coincidir con la cadena usada en el cifrado cesar
    
    # For para recorrer con cada una de las posibles llaves
    
    for key in range (len(symbols)):
        # Cadena vacia para escribir cada uno de los posibles mensajes 
        HackPhrase = ""
        
        # Ciclo for para recorrer el mensaje a descifrar
        for sym in message:
            if sym in symbols:
                index = symbols.find(sym)
                tranInx = index - key
                
                if index < 0 :
                    tranInx = tranInx + len(symbols)
                    
                HackPhrase = HackPhrase + symbols[tranInx]
                    
            else:
                HackPhrase = HackPhrase + sym
                
        # Se imprime los posibles mensajes con cada una de las posibles llaves
        print("Key #{0} : {1}" .format(key, HackPhrase))
        print("")
    

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
       

# Brute-Force para descifrar el cifrado cesar con inversibilidad

def Hack_CRev ():
    message = str(input("Mensaje a descifrar: "))
    symbols = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890.,?¿ ¡!" 
    
    # Primro se invierte el mensaje inicial
    traduccion = ""
 
    j = len(message) - 1
    while j >= 0:
        traduccion = traduccion + message[j]
        j = j - 1
    # La cadena symbols debe coincidir con la cadena usada en el cifrado cesar
    
    # For para recorrer con cada una de las posibles llaves
    
    for key in range (len(symbols)):
        # Cadena vacia para escribir cada uno de los posibles mensajes 
        HackPhrase = ""
        
        # Ciclo for para recorrer el mensaje a descifrar
        for sym in traduccion:
            if sym in symbols:
                index = symbols.find(sym)
                tranInx = index - key
                
                if index < 0 :
                    tranInx = tranInx + len(symbols)
                    
                HackPhrase = HackPhrase + symbols[tranInx]
                    
            else:
                HackPhrase = HackPhrase + sym
                
        # Se imprime los posibles mensajes con cada una de las posibles llaves
        print("Key #{0} : {1}" .format(key, HackPhrase))
        print("")
