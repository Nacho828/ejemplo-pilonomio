from polinomio import Polinomio

def ejecutar():
    # Function implementation
    print("Ejecutar function is running")

p = Polinomio()
p.cargar_termino(3, 4)
p.cargar_termino(2, 2)
p.cargar_termino(5, 0)

print("Polinomio:", p.mostrar())
print("Valor de x^2:", p.obtener_valor(2))
print("¿Existe x^2?:", p.existe_termino(2))

p.eliminar_termino(2)
print("Después de eliminar x^2:")
print("Polinomio:", p.mostrar())
print("¿Existe x^2?:", p.existe_termino(2))
