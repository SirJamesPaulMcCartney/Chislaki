import numpy
import copy


def eximple(a):
    eps = 1e-3

    a = numpy.array(a)

    i_n = len(a[:, 0])
    j_n = len(a[0, :])
    l = numpy.eye(i_n)

    for i in range(i_n):

        aii = float(a[i][i])
        ix1 = i
        while ix1 < j_n:
            a[i][ix1] = a[i][ix1]/aii
            ix1 =+ 1

        a[i][i] = 0



    vectb = a[:][j_n]
    a = -a
    print(a)
    print(vectb)



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


