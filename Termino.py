from Polinomio import Polinomio

class Termino(object):
    
    
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente

    def __repr__(self):
        if self.exponente == 0:
            return f"{self.coeficiente}"
        elif self.exponente == 1:
            return f"{self.coeficiente}x"
        else:
            return f"{self.coeficiente}x^{self.exponente}"