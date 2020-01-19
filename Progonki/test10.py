import progon
import numpy

a = numpy.array([[-11., 9, 0, 0, 0, -114],
                [-2., -11, 5, 0, 0, 8],
                [0., -1, -12, -6, 0, 48],
                 [0., 0, 3, -14, 7, -38],
                 [0., 0, 0, 8, 10, 144]])
print('Исходная матрица:')
print(a)
print("\n")

b = progon.progon(a)
print("Ответ:")
print(b)