import numpy
import copy
import gausss
from gausss import DetermExeption


def lu(a):
    eps = 1e-3

    a = numpy.array(a)

    i_n = len(a[:, 0])
    j_n = len(a[0, :])
    l = numpy.eye(i_n)

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

        if abs(max) < eps:
            raise DetermExeption("Check determinant")

        if ix1 != i:
            b = copy.deepcopy(a[i])
            a[i] = copy.deepcopy(a[ix1])
            a[ix1] = copy.deepcopy(b)

        for r in range(i_n-i):
            y = r + i
            l[y, i] = a[y, i]


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

    print('U:')
    #print(float(i))
    print(a[0:i_n, 0:i_n])
    print('L:')
    print(l[0:i_n, 0:i_n])
    a = gausss.backTrace(a, i_n, j_n)
    return a


