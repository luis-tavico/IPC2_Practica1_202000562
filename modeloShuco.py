class Shuco:
    def __init__(self, ingrediente, tiempo):
        self.ingrediente = ingrediente
        self.tiempo = tiempo
    
    def getIngrediente(self):
        return self.ingrediente

    def getTiempo(self):
        return self.tiempo

    def setIngrediente(self, ingrediente):
        self.ingrediente = ingrediente

    def setTiempo(self, tiempo):
        self.tiempo = tiempo