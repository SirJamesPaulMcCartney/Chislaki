import eximple
import numpy

a = numpy.array([[1., 2, 1, 1],
                [1, 67, 1, 1],
                [0, 1, 13, 2]])
print('Исходная матрица:')
print(a)
print("\n")

b = eximple.eximple(a)
print("Ответ:")
print(b)