import gauss
import numpy

a = numpy.array([[1., 2, 1, 1],
                [1, 67, 1, 1],
                [0, 1, 13, 2]])
print('Исходная матрица:')
print(a)
print("\n")

b = gauss.gaussFunc(a)
print("Ответ:")
print(b)