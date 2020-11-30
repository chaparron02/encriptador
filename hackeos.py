# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:15:14 2020

@author: chaparron02
"""

"Hackeos"

import encriptadores, math

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

# Brute-force para cifrado reverse       
def hackreverse():
  encriptadores.reverse() 

# Brute-force para cifrado de transposicion     
def hack_transp():    
 message = str(input("Mensaje a descifrar: "))
 for key in range(1, len(message)): 
  print('Trying key #%s...' % (key)) 
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
    decryptedText = ''.join(plaintext)
   
  print('Possible encryption hack:')
  print('Key %s: %s' % (key, decryptedText[:100]))
  print('Enter D if done, anything else to continue hacking:')
  response = input('> ')
  if response.strip().upper().startswith('D'):
      return decryptedText
 return None
  

