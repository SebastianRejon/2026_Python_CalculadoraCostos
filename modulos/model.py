import os

class Costo:
    def __init__(self,fecha,imp_ltsCombustible,kilometros,imp_bobina,luz,tiempo_prod, tiempo_viaje,costo_kw):
        self.fecha=fecha
        self.importe_combustible=imp_ltsCombustible
        self.kilometros=kilometros
        self.importe_bobina=imp_bobina
        self.luz=luz
        self.tiempo_prod=tiempo_prod
        self.tiempo_viaje=tiempo_viaje
        self.costo_kw=costo_kw
        self.costo_final
    def calculoCosto(self):
        self.costo_final=10
    def calculoATexto(self):
        pass

class Datos:
    def __init__(self,rutaArchivo):
        self.ruta=rutaArchivo

    def apertura(self):    
        if not os.path.exists(self.ruta):
            archivo=open(self.ruta,"w")
            os.system("cls")
            print("#"*50)
            print("Archivo no existe en ruta especificada".center(50, " "))
            print("Archivo creado".center(50, " "))
            print("#"*50)
        else:
            archivo=open(self.ruta,"r")
            os.system("cls")
            print("#"*50)
            print("Archivo existente abierto".center(50, " "))
            print("#"*50)
            self.lecturaDeDatos(archivo)

    def lecturaDeDatos(self, ruta):
        with open(ruta, "r") as archivo:
            tb=archivo.read()
        print(tb)
        return tb
        


