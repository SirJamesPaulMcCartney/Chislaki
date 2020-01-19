import numpy

X = 2

def quadr(x,y):
    x = numpy.array(x)
    y = numpy.array(y)
    lenx = len(x)
    xn = yn = x2 = xy = 0

    for n in range(lenx):
        xn = xn + x[n]
        yn = yn + y[n]
        x2 = x2 + x[n]*x[n]
        xy = xy + x[n]*y[n]

    print('Ex = ', xn)
    print('Ey = ', yn)
    print('Ex^2 = ', x2)
    print('Exy = ', xy)

    v = x2*lenx - xn*xn
    va = xy*lenx - yn*xn
    vb = x2*yn - xn*xy
    a = va/v
    b = vb/v
    print('a =',a)
    print('b =',b)
    Y = a*X + b
    print('Y = ',Y)
    return x,y
