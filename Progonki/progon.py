import numpy
import copy


def progon(a):

    a = numpy.array(a)

    i_n = len(a[:, 0])
    alpha = numpy.zeros(i_n)
    betta = numpy.zeros(i_n)
    x = numpy.zeros(i_n+1)
    k = i_n - 1


    for i in range(i_n):
        y = a[i,i] + a[i,i-1]*alpha[i-1]
        alpha[i] = -a[i,i+1]/y
        betta[i] = (a[i,i_n] - a[i-1,i]*betta[i-1])/y

    print("alpha =", alpha)
    print("betta =", betta)
    print("------------------------------")

    while k >= 0:
        x[k] = alpha[k]*x[k+1] + betta[k]
        k -= 1
    print("x =", x[0:i_n])
    return x[0:i_n]