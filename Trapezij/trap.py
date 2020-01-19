import math
from numpy import arange

def trap(a,b,h):
    fs = 0

    def f(X):
        f = 1 / ((2*X+7)*(3*X+4))
        return f
    for xi in arange(a, b+h, h):
        print('x = ',xi)
        f1 = f(xi)
        print('f(x)  =',f1)
    for xi2 in arange(a+h, b, h):
        fs = fs + f(xi2)
    F = h*((f(a)+f(b))/2+fs)
    return F
