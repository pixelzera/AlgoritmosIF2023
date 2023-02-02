from ast import Num
from audioop import add
from dataclasses import dataclass
from optparse import Option
from tkinter import Menu
#Sistema de Cadastro de Motos

@dataclass
class moto:
    placa: str
    marca: str
    modelo: str
    cor: str
    ano: int


def main():
    pass
    menu = ''' 
    [1]Cadastro
    [2]Editar
    [3]Consultar
    [4]Sair
    '''
print (menu)
op = int(input("Selecione a OPÇÃO desejada : "))  

    while (op !=5):
                  
        if op == 1:
            add()
        if op == 2:
                update()
        if op == 3:
                list()
        if op == 4:
                delete()
        if op == 5:
                exit()
 
      
                     
                    
def add():
    pass

def update():
    pass

def list():
    pass

def delete():
    pass

main()
