from sympy import symbols, diff, tan, cos, sin


a = 0
b = 9
x0 = b
e = 0.001

def Fx(x):
    X = symbols('x')
    Y = symbols('y')
    Y = tan(X) - 5*X**2 + 1
    dY = diff(Y)
    return dY

print('1 призводн =', Fx(0))
print('2 призводн =', diff(Fx(0)))
print('-----------------------------')


n = 0

def f(x):
    a = tan(x)- 5*x**2 + 2
    return a

def df(x):
    return -10*x + tan(x)**2 + 1

# тупо чтоб def была от 2 переменных
def dx(f, x):
    return abs(0-f(x))

def kasat(f, df, x0, e):

    print(n,'итерация')
    delta = 0
    while delta > e:
        x0 = x0 - f(x0) / df(x0)
        delta = dx(f, x0)
    print('x =', x0)
    print('f(x) =', f(x0))

x0s = [a, (b-a)/2, b]
for x0 in x0s:
    n = n + 1
    kasat(f, df, x0, e)

