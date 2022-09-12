class Orden:
    def __init__(self, numero, nombreCliente, cantidadShucos, shucos, tiempoTotal, tiempoEnCola):
        self.numero = numero
        self.nombreCliente = nombreCliente
        self.cantidadShucos = cantidadShucos
        self.shucos = shucos
        self.tiempoTotal = tiempoTotal
        self.tiempoEnCola = tiempoEnCola

    def getNumero(self):
        return self.numero

    def getNombreCliente(self):
        return self.nombreCliente

    def getCantidadShucos(self):
        return self.cantidadShucos

    def getShucos(self):
        return self.shucos

    def getTiempoTotal(self):
        return self.tiempoTotal

    def getTiempoEnCola(self):
        return self.tiempoEnCola

    def setNumero(self, numero):
        self.numero = numero

    def setNombreCliente(self, nombreCliente):
        self.nombreCliente = nombreCliente

    def setCantidadShucos(self, cantidadShucos):
        self.cantidadShucos = cantidadShucos

    def setShucos(self, shucos):
        self.shucos = shucos

    def setTiempoTotal(self, tiempoTotal):
        self.tiempoTotal = tiempoTotal

    def setTiempoEnCola(self, tiempoEnCola):
        self.tiempoEnCola = tiempoEnCola