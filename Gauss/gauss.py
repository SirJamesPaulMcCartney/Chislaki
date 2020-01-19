import numpy
import copy
from gausss import DetermExeption


def gaussFunc(a):
    eps = 1e-3

    a = numpy.array(a)

    i_n = len(a[:, 0])
    j_n = len(a[0, :])

    for i in range(i_n):

        max = abs(a[i][i])
        ix1 = i
        ix2 = i
        while ix2 < i_n:
            # for ix2 in range(len(a[:,0])):
            if abs(a[ix2][i]) > max:
                max = abs(a[ix2][i])
                ix1 = ix2
            ix2 += 1

        class DetermExeption(Exception):
            def __init__(self, value):
                self.value = value

            def __str__(self):
                return repr(self.value)

        if abs(max) < eps:
            raise DetermExeption("Check determinant")

        if ix1 != i:
            b = copy.deepcopy(a[i])
            a[i] = copy.deepcopy(a[ix1])
            a[ix1] = copy.deepcopy(b)

        aii = float(a[i][i])
        print(a)
        print('/n')

        jx1 = i
        while jx1 < j_n:
            a[i][jx1] = a[i][jx1] / aii
            jx1 += 1

        j = i + 1

        while j < i_n:
            b = a[j][i]
            jx1 = i

            while jx1 < j_n:
                a[j][jx1] = a[j][jx1] - a[i][jx1] * b
                jx1 += 1
            j += 1
    print('Матрица по Гауссу:')
    print(a)
    a = backTrace(a, i_n, j_n)
    return a


def backTrace(a, i_n, j_n):
    a = numpy.array(a)
    i = i_n - 1
    while i > 0:
        j = i - 1

        while j >= 0:
            #print(float(a[j][j_n]))
            a[j][i_n] = a[j][i_n] - a[j][i] * a[i][i_n]
            #print(float(a[j][i]))
            j -= 1
        i -= 1
    return a[:, j_n - 1]


