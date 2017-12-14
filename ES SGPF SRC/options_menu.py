# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 18:55:26 2017

@author: Andreea Aniculaesei
"""

print("Welcome to SGPF application")
print("The options are: ")
print()
print("1 - Tecnico")
print("2 - CF")
print("3 - GF")
print("4 - EXIT")
print()

choice = input("Choose your option: ")
choice = int(choice)


if choice == 1:
    print("OPCOES DO TECNICO ")
    print("1 - submeter candidatura")
    print("2 - arquivar candidatura")    
    print("3 - alterar dados projeto")
    print("4 - suspender projecto")
    
    
    
elif choice == 2:
    print("OPCOES DO GF ")
    print("1 - alterar dados projeto")
    print("2 - suspender projecto")    
    print("3 - reactivar projeto")
    print("4 - emitir parecer")
    print("5 - efectuar pagamento")
    print("6 - pedir reforco")   
    
elif choice  == 3:
    print("OPCOES DA CF ")
    print("1 - suspender projecto")
    print("2 - reactivar projeto")    
    print("3 - emitir despacho")
    
elif choice == 4:
    break

    
    
    