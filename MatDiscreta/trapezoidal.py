"""Integração Numérica"""
from math import sin, pi

#Cada subintervalo é aproximado com um trapézio `area = ½dx[f(a)+f(b)]`

def trapezoidal(f, x0, xf, dx):
    """
     f: função a integrar
    x0: inicio do intervalo de integração
    xf: fim do interval de integração
    dx: tamanho dos subintervalos de integração
    """

    # A soma das subáreas
    soma = 0
    
    # Precisamos de dois ponto no intervalo dx
    x1 = x0
    x2 = x0 + dx
    
    while x1<=xf:
              
        soma += 0.5*dx*( f(x1) + f(x2) )
        
        x1 += dx
        x2 += dx
    
    return soma