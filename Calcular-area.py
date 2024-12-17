import math

# paso 1: Solcite al usuario ingresar el radio del circular.
radio= float(input("Ingresar radio del circulo para calcular su área: "))

# paso 2: Calculamos el área utilizando la formula area= pi *radio^2
area= math.pi * (radio**2)

# paso 3: Mostrar al usuario el calculo realizado
print("El área del círculo con Radio", radio,"es",area)