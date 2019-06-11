import datetime

class Saludo:

    def __init__(self):
        self.asunto=""
        self.fechaCreacion=datetime.datetime
        self.remitente=""
    
    def __init__(self, asunto, fechaCreacion, remitente):
        self.asunto=asunto
        self.fechaCreacion=fechaCreacion
        self.remitente=remitente

    def __str__(self):
        return '{} * {} * {}'.format(self.asunto, self.fechaCreacion.strftime("%d-%m-%Y %H:%M:%S"), self.remitente)
    #    return self.asunto+" "+self.fechaCreacion+" "+self.remitente
    #    return self.asunto," ",self.remitente
    