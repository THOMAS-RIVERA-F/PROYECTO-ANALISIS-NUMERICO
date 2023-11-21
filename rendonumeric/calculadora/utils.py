import pandas as pd
import numpy as np
import math


# import wdb
# wdb.set_trace()

def newton(funcion):

    funcion = funcion.split(',')
    X0 = float(funcion[0])
    Tol = float(funcion[1])
    Niter = float(funcion[2])
    Fun = funcion[3]
    df = funcion[4]
    """"
    print("X0:")
    X0 = float(input())
    print("Tol:")
    Tol = float(input())
    print("Niter:")
    Niter = float(input())
    print("Function:")
    Fun = input()
    print("derivate Function df:")
    df = input()"""

    fn = []
    xn = []
    E = []
    N = []
    x = X0
    f = eval(Fun)
    derivada = eval(df)
    c = 0
    Error = 100
    fn.append(f)
    xn.append(x)
    E.append(Error)
    N.append(c)
    while Error > Tol and f != 0 and derivada != 0 and c < Niter:
        x = x - f / derivada
        derivada = eval(df)
        f = eval(Fun)
        fn.append(f)
        xn.append(x)
        c = c + 1
        Error = abs(xn[c] - xn[c - 1])
        N.append(c)
        E.append(Error)
    if f == 0:
        s = x
        print(s, "es raiz de f(x)")
    elif Error < Tol:
        s = x
        print(s, "es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
        print("N", N)
        print("xn", xn)
        print("fn", fn)
        print("Error", E)
    else:
        s = x
        print("Fracaso en ", Niter, " iteraciones ")


newton('1,0.0005,100,(x**3)-x-1,(3*x**2)-1')


def biseccion(funcion):
    funcion = funcion.split(',')
    Xi = float(funcion[0])
    Xs = float(funcion[1])
    Tol = float(funcion[2])
    Niter = float(funcion[3])
    Fun = funcion[4]
    '''
    print("Xi:")
    Xi = float(input())
    print("Xs:")
    Xs = float(input())
    print("Tol:")
    Tol = float(input())
    print("Niter:")
    Niter = float(input())
    print("Function:")
    Fun = input()
    '''

    fm = []
    E = []
    x = Xi
    fi = eval(Fun)
    x = Xs
    fs = eval(Fun)

    if fi == 0:
        s = Xi
        E = 0
        print(Xi, "es raiz de f(x)")
    elif fs == 0:
        s = Xs
        E = 0
        print(Xs, "es raiz de f(x)")
    elif fs * fi < 0:
        c = 0
        Xm = (Xi + Xs) / 2
        x = Xm
        fe = eval(Fun)
        fm.append(fe)
        E.append(100)
        while E[c] > Tol and fe != 0 and c < Niter:
            if fi * fe < 0:
                Xs = Xm
                x = Xs
                fs = eval(Fun)
            else:
                Xi = Xm
                x = Xi
                fs = eval(Fun)
            Xa = Xm
            Xm = (Xi + Xs) / 2
            x = Xm
            fe = eval(Fun)
            fm.append(fe)
            Error = abs(Xm - Xa)
            E.append(Error)
            c = c + 1
        if fe == 0:
            s = x
            print(s, "es raiz de f(x)")
        elif Error < Tol:
            s = x
            print(s, "es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
            print("Fm", fm)
            print("Error", fm)
        else:
            s = x
            print("Fracaso en ", Niter, " iteraciones ")
    else:
        print("El intervalo es inadecuado")

biseccion('0,1,0.000005,100,(x**4)+(3*x**3)-2')