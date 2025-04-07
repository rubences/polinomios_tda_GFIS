from Termino import Termino
from Polinomio import Polinomio



p = Polinomio()
p.agregar_termino(3, 4)  # 3x^4
p.agregar_termino(-2, 3) # -2x^3
p.agregar_termino(1, 2)  # x^2
p.agregar_termino(-5, 1) # -5x
p.agregar_termino(1, 0)  # 1

q = Polinomio()
q.agregar_termino(1, 3)  # x^3
q.agregar_termino(2, 2)  # 2x^2
q.agregar_termino(-1, 1) # -x
q.agregar_termino(4, 0)  # 4

# Operaciones
suma = p + q
resta = p - q
producto = p * q
evaluacion_p_en_2 = p.evaluar(2)
derivada_p = p.derivar()
integral_p = p.integrar()

# Mostrar resultados
print(f"Polinomio p: {p}")
print(f"Polinomio q: {q}")
print(f"Suma (p + q): {suma}")
print(f"Resta (p - q): {resta}")
print(f"Producto (p * q): {producto}")
print(f"Evaluación de p en x = 2: {evaluacion_p_en_2}")
print(f"Derivada de p: {derivada_p}")
print(f"Integral de p: {integral_p}")