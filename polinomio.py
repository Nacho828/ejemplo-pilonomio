from nodo import Nodo
from DatoPolinomio import DatoPolinomio



class Polinomio:
    def __init__(self):
        self.grado = 0
        self.primero = None

    def cargar_termino(self, coef, exp):
        if coef == 0:
            return

        nuevo = Nodo(DatoPolinomio(coef, exp))

        if self.primero is None or exp > self.primero.termino.exponente:
            nuevo.siguiente = self.primero
            self.primero = nuevo
        else:
            actual = self.primero
            anterior = None
            while actual is not None and actual.termino.exponente > exp:
                anterior = actual
                actual = actual.siguiente

            if actual is not None and actual.termino.exponente == exp:
                actual.termino.coeficiente = coef
                return

            nuevo.siguiente = actual
            if anterior:
                anterior.siguiente = nuevo

        if exp > self.grado:
            self.grado = exp

    def obtener_valor(self, exp):
        actual = self.primero
        while actual:
            if actual.termino.exponente == exp:
                return actual.termino.coeficiente
            actual = actual.siguiente
        return 0

    def eliminar_termino(self, exp):
        actual = self.primero
        anterior = None

        while actual and actual.termino.exponente != exp:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            return  # Término no encontrado

        if anterior is None:
            self.primero = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente

        # Recalcular grado si se elimina el mayor
        if exp == self.grado:
            actual = self.primero
            nuevo_grado = 0
            while actual:
                if actual.termino.exponente > nuevo_grado:
                    nuevo_grado = actual.termino.exponente
                actual = actual.siguiente
            self.grado = nuevo_grado

    def existe_termino(self, exp):
        actual = self.primero
        while actual:
            if actual.termino.exponente == exp:
                return True
            actual = actual.siguiente
        return False

    def mostrar(self):
        actual = self.primero
        if not actual:
            return "0"

        partes = []
        while actual:
            coef = actual.termino.coeficiente
            exp = actual.termino.exponente
            if exp == 0:
                partes.append(f"{coef}")
            elif exp == 1:
                partes.append(f"{coef}x")
            else:
                partes.append(f"{coef}x^{exp}")
            actual = actual.siguiente

        return " + ".join(partes)
        def restar(self, otro):
            resultado = Polinomio()
            actual = self.primero

            while actual:
                coef = actual.termino.coeficiente
                exp = actual.termino.exponente
                resultado.cargar_termino(coef, exp)
                actual = actual.siguiente

            actual = otro.primero
            while actual:
                coef = -actual.termino.coeficiente
                exp = actual.termino.exponente
                resultado.cargar_termino(resultado.obtener_valor(exp) + coef, exp)
                actual = actual.siguiente

            return resultado

        def dividir(self, otro):
            if otro.primero is None:
                raise ValueError("No se puede dividir por un polinomio nulo")

            cociente = Polinomio()
            dividendo = Polinomio()
            actual = self.primero

            while actual:
                dividendo.cargar_termino(actual.termino.coeficiente, actual.termino.exponente)
                actual = actual.siguiente

            while dividendo.primero and dividendo.primero.termino.exponente >= otro.primero.termino.exponente:
                coef = dividendo.primero.termino.coeficiente / otro.primero.termino.coeficiente
                exp = dividendo.primero.termino.exponente - otro.primero.termino.exponente
                termino = Polinomio()
                termino.cargar_termino(coef, exp)
                cociente.cargar_termino(coef, exp)
                resto = otro.multiplicar(termino)
                dividendo = dividendo.restar(resto)

            return cociente