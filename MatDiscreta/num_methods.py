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

print(mid_point(sin, 0, pi/2, 0.1))
