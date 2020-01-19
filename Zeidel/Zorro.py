import numpy

def zorro(a):
    eps = 1e-3

    a = numpy.array(a)


    i_n = len(a[:, 0])
    j_n = len(a[0, :])
    vectb = a[[0, 1, i_n-1], :][:, [j_n - 1]]
    n = 0
    x = numpy.array([[0.],
                    [0],
                    [0]])

    converge = False
    while not converge:
        xnext = numpy.copy(x)
        print(n,'итерация')
        for i in range(i_n):
            s1 = sum(a[i][j] * xnext[j] for j in range(i))
            s2 = sum(a[i][j] * x[j] for j in range(i + 1, i_n))
            xnext[i] = (vectb[i] - s1 - s2) / a[i][i]
        print(xnext)
        n += 1
        converge = abs(sum((xnext[i] - x[i]) for i in range(i_n))) <= eps
        x = xnext

    return x