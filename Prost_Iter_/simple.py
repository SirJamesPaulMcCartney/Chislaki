import numpy
import copy


def simple(a):
    eps = 1e-3

    a = numpy.array(a)

    i_n = len(a[:, 0])
    j_n = len(a[0, :])

    for i in range(i_n):

        aii = float(a[i][i])
        jx1 = 0
        while jx1 < j_n:
            a[i][jx1] = a[i][jx1] / aii
            jx1 += 1
        a[i][i] = 0

    vectb = a[[0,1,i], :][:, [j_n-1]]
    a = -a
    alpha = a[[0,1,i], :][:, [0,1,i]]
    print('alpha:')
    print(alpha)
    print('betta')
    print(vectb)

    #xbefore = numpy.zeros((i_n,))
    #xbefore = xbefore.transpose()
    # print(xbefore)
    #xbefore = numpy.array([0 for i in range(i_n)])
    #    xbefore = xbefore.transpose()
    #   print(xbefore)
    xbefore = numpy.array([[0],
                           [0],
                           [0]])
    eii = 1
    for i in range(i_n):
        n = 0
        while eii > eps:
            x = vectb + alpha.dot(xbefore)
            e = x - xbefore
            max = abs(e[i][0])
            ix1 = i
            ix2 = i
            ex1 = copy.deepcopy(e)
            while ix2 < i_n:
                if abs(ex1[ix2][0]) > max:
                    max = abs(ex1[ix2][0])
                    ix1 = ix2
                ix2 += 1
            eii = abs(ex1[ix1][0])
            xbefore = x
            print(n,'итерация')
            n += 1
            print(x)
            print('eps = ')
            print(eii)
    return a



