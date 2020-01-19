import quadr
import numpy

x = numpy.array([1., 2, 3, 4, 5])
y = numpy.array([5.3, 6.3, 4.8, 3.8, 3.3])

print('Исходная матрица:')
print(x)
print(y)
print("\n")

qqq = quadr.quadr(x,y)
print("Ответ:")
print(qqq)