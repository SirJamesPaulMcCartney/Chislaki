import simple
import numpy

a = numpy.array([[10., 1, 1, 12],
                [2, 10, 1, 13],
                [2, 2, 10, 14]])
print('Исходная матрица:')
print(a)
print("\n")

b = simple.simple(a)