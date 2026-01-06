import os
from modulos.model import *

def listarHistorial(arch):
    print(arch.apertura())

def menup(arch):
    while True:
        os.system("cls")
        print("#"*50)
        print("#"+"MENU PRINCIPAL".center(48, " ")+"#")
        print("# 1.NUEVO CALCULO COSTO ".ljust(49, " ")+"#")
        print("# 2.HISTORIAL DE COSTOS ".ljust(49, " ")+"#")
        print("# 3.BORRAR TODO EL HISTORIAL ".ljust(49, " ")+"#")
        print("# 0.SALIR ".ljust(49, " ")+"#")
        print("#"*50)
        print("\n")
        opc=input("OPCION <0-2>: ")
        match opc:
            case '0':
                break
            case '1':
                pass
            case '2':
                listarHistorial(arch)
                os.system("Pause")
            case '3':
                pass 
            case _:
                print("Opción Incorrecta. Intente de nuevo.")  
                os.system("Pause")                     
        print("\n")
    os.system("Puase")

def main(rutaBase):
    arch=Datos(rutaBase)
    arch.apertura()
    peso=os.path.getsize(rutaBase)
    if peso==0:
        os.system("cls")
        print("#"*50)
        print("Alerta. No hay historial de calculos solo puede crear!")
        print("#"*50)
        os.system("Pause")
    menup(arch)
        

if __name__=='__main__':
    rutaBase='HistorialCostos.dat'
    main(rutaBase)