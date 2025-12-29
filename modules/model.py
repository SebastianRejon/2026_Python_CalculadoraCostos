class Costo:
    def __init__(self,fecha,combustible,kilometros,imp_bobina,luz,tiempo_prod, tiempo_viaje):
        self.fecha=fecha
        self.importe_combustible=combustible
        self.kilometros=kilometros
        self.importe_bobina=imp_bobina
        self.luz=luz
        self.tiempo_prod=tiempo_prod
        self.tiempo_viaje=tiempo_viaje
    def calculoCosto(self):
        