from Termino import Termino

class Polinomio (object):
    def __init__(self):
        self.terminos = []

    def agregar_termino(self, coeficiente, exponente):
        if coeficiente != 0:
            for termino in self.terminos:
                if termino.exponente == exponente:
                    termino.coeficiente += coeficiente
                    return
            self.terminos.append(Termino(coeficiente, exponente))
        self.terminos.sort(key=lambda t: t.exponente, reverse=True)

    def __add__(self, otro):
        resultado = Polinomio()
        for termino in self.terminos:
            resultado.agregar_termino(termino.coeficiente, termino.exponente)
        for termino in otro.terminos:
            resultado.agregar_termino(termino.coeficiente, termino.exponente)
        return resultado

    def __sub__(self, otro):
        resultado = Polinomio()
        for termino in self.terminos:
            resultado.agregar_termino(termino.coeficiente, termino.exponente)
        for termino in otro.terminos:
            resultado.agregar_termino(-termino.coeficiente, termino.exponente)
        return resultado

    def __mul__(self, otro):
        resultado = Polinomio()
        for t1 in self.terminos:
            for t2 in otro.terminos:
                resultado.agregar_termino(t1.coeficiente * t2.coeficiente, t1.exponente + t2.exponente)
        return resultado

    def evaluar(self, valor):
        resultado = 0
        for termino in self.terminos:
            resultado += termino.coeficiente * (valor ** termino.exponente)
        return resultado

    def derivar(self):
        resultado = Polinomio()
        for termino in self.terminos:
            if termino.exponente > 0:
                resultado.agregar_termino(termino.coeficiente * termino.exponente, termino.exponente - 1)
        return resultado

    def integrar(self, constante_integracion=0):
        resultado = Polinomio()
        resultado.agregar_termino(constante_integracion, 0)
        for termino in self.terminos:
            resultado.agregar_termino(termino.coeficiente / (termino.exponente + 1), termino.exponente + 1)
        return resultado

    def __repr__(self):
        if not self.terminos:
            return "0"
        return " + ".join(map(str, self.terminos))