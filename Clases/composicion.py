class Llanta:
    def __init__(self):
        pass

class Motor:
    def __init__(self):
        pass

class Carro:
    def __init__(self):
        self.motor = Motor()
        self.llantas = []
        self.instalarLlantas()

    def instalarLlantas(self, cantidad):
        for i in range(cantidad):
            self.llantas.append(Llanta())