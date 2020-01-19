import Zorro
import numpy

a = numpy.array([[10., -1, -2, 5],
                [4, 28, 7, 9],
                [6, 5, -23, 4]])
print('Исходная матрица:')
print(a)
print("\n")

b = Zorro.zorro(a)