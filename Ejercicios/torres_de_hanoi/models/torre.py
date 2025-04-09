class Torre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.discos = []

    def apilar(self, disco):
        self.discos.append(disco)

    def desapilar(self):
        return self.discos.pop() if self.discos else None

    def __str__(self):
        return f"{self.nombre}: {self.discos}"
