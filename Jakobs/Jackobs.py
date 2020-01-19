import numpy
from math import fabs

a = numpy.array([[-4, 0.5, -1.5, -1],
                   [0.55, 6, 2.4, 1.3],
                   [0.33, -0.52, 3, 0.21],
                   [-0.22, 0.98, -2.5, 5]])
B = numpy.array([[-1.67],
              [3.15],
              [-0.21],
              [5.54]])
X = numpy.array([[0.0],
              [0.0],
              [0.0],
              [0.0]])
deltaX = numpy.array([[0.0],
                   [0.0],
                   [0.0],
                   [0.0]])
i_n = len(a[:, 0])
j_n = len(a[0, :])
print(i_n)
for i in range(i_n):
    vectb = a[[0,1,i], :][:, [j_n-1]]
    print(vectb)

def chek(i):
    #    j = 0
    sum = 0
    for j in range(0, j_n, 1):
        if i != j:
            sum = sum + fabs(a[i, j])
    if fabs(a[i, i]) > sum:
        if i != 3:
            return chek(i + 1)
        if i == 3:
            print("Метод Якоби применим")
    else:
        print("Error 404")
        return


chek(0)
eps = 0.0001

for i in range(0, 4, 1):
    B[i, 0] = B[i, 0] / a[i, i]

i = 0
j = 0
for i in range(0, 4, 1):
    t = float(a[i, i])
    for j in range(0, 4, 1):
        a[i, j] = a[i, j] / t
        a[i, j] = a[i, j] * -1
    a[i][i] =  0
print(a)
print(B)
print("----------------------------------------")

counter = 0
max = 1.0000
while max > eps:
    counter += 1
    if counter > 1:
        B = X[:]
    print(B)
    for i in range(0, 4, 1):
        SUM = 0
#        s = 0
        for j in range(0, 4, 1):
            s = a[i, j] * B[j, 0]
            SUM = SUM + s
        SUM = SUM + B[i, 0]
        X[i, 0] = SUM
        deltaX[i, 0] = fabs((B[i, 0] - SUM))
    print(counter, "Iteraciya")
    print("X=", X)
    print("deltaX=", deltaX)
    max = deltaX[0, 0]
    for k in range(0, 4, 1):
        if deltaX[k, 0] > max:
            max = deltaX[k, 0]
print("--------------------------------------------------------------------------------------------------------------")


print(X)
print(deltaX)