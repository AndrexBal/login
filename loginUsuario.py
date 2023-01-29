from openpyxl import *
from openpyxl import Workbook

def loginUsuario():
    #Iniciamos el Excel
    book = load_workbook('bd_login.xlsx')
    
    #recuperar la cantidad de filas
    max_row = book.active.max_row
    
    #datos de usuario para comprobar que esten registrados en la bd
    
    username = input("Ingrese el nombre del usuario: ")
    password = input("Ingrese contraseña: ")
    
    #rastrear los usuarios de la bd
    sheet = book.active
    for i in range(max_row):
        #iniciamos en la fila 2
        variableApoyo = i+2
        
        userconfi = sheet[f"B{variableApoyo}"]
        passconfi = sheet[f"C{variableApoyo}"]
        
        if username == userconfi.value and password == passconfi.value:
            print("El usuario esta logueado ")
            return True 
        
    else: 
        print("Usuario o contraseña incorrecto")
        
loginUsuario()