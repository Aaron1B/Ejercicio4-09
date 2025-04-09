from .torre import Torre

class Hanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.torres = {
            'A': Torre('A'),
            'B': Torre('B'),
            'C': Torre('C')
        }
        self._inicializar_torres()

    def _inicializar_torres(self):
        for i in range(self.num_discos, 0, -1):
            self.torres['A'].apilar(i)

    def mover(self, origen, destino):
        disco = self.torres[origen].desapilar()
        if disco is not None:
            self.torres[destino].apilar(disco)
        return self.estado()

    def resolver(self, num_discos=None, origen='A', destino='C', auxiliar='B'):
        if num_discos is None:
            num_discos = self.num_discos

        if num_discos == 1:
            self.mover(origen, destino)
        else:
            self.resolver(num_discos-1, origen, auxiliar, destino)
            self.mover(origen, destino)
            self.resolver(num_discos-1, auxiliar, destino, origen)

    def estado(self):
        return {nombre: str(torre) for nombre, torre in self.torres.items()}
