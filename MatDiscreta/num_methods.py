"""Integração Numérica"""
from math import sin, pi

#Midpoint rule :
#->Cada sub-intervalo é aproximado com um retangulo de base dx e altura f(x)
#->A área de cada sub-intervalo : A = dx*f(x)
#->A altura de cada retangulo f(x) é calculado no midpoint de cada subintervalo.

def mid_point(funcao, x_inicial, x_final, delta_x):
    soma = 0
    x= x_inicial+delta_x/2
    while x<=x_final:
        soma += delta_x*funcao(x)
        x+=delta_x
    return soma

# Testando com f=sin e dx=0.1 no intervalo [0, pi/2]
# O resultado esperado é 1
print(mid_point(sin, 0, pi/2, 0.1))



# Testando com f=sin(x)/x
# para dx=0.1 no intervalo [0, pi]
# O resultado esperado é ≈ 1.85194

# Não podemos fazer isto
# Integrate(sin(x)/x, 0, pi, 0.1)

# Podemos passar uma função, mas não uma expressão

# Neste caso criamos a função myFunc, equivalente à função matemática que pretendemos

def my_func(var_x):
    return sin(var_x)/var_x

print(mid_point(my_func, 0, pi, 0.1))
