import LU
import numpy

a = numpy.array([[3., -8, 1, -7, 96],
                [6, 4, 8, 5, -13],
                [-1, 1, -9, -3, -54],
                 [-6, 6, 9, -4, 82]])
print('Исходная матрица:')
print(a)
print("\n")

b = LU.lu(a)
print("Ответ:")
print(b)