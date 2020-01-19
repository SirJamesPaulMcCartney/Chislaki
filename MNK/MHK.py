import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy
mpl.rcParams['font.family'] = 'fantasy'

x=[10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86]
y=[0.1, 0.0714, 0.0556, 0.0455, 0.0385, 0.0333, 0.0294, 0.0263, 0.0238, 0.0217,
   0.02, 0.0185, 0.0172, 0.0161, 0.0152, 0.0143, 0.0135, 0.0128, 0.0122, 0.0116]
st = 2

def MNK(x,y,st):

        n = len(x)
        s = sum(y)

        fp, residuals, rank, sv, rcond = scipy.polyfit(x, y, st, full=True)
        f = scipy.poly1d
        print('a =', round(fp[0], 4))
        print('b =', round(fp[1], 4))
        print('c =', round(fp[2], 4))
        y1 = [fp[0] * x[i] ** 2 + fp[1] * x[i] + fp[2] for i in range(n)]
        s1 = sum([1/x[i] for i in range(n)]) #  сумма 1/x
        s2 = sum([(1/x[i])**2 for i in range(n)]) #  сумма (1/x)**2
        s3 = sum([y[i]/x[i] for i in range(n)])  # сумма y/x
        a = round((s*s2-s1*s3)/(n*s2-s1**2),3) # коэфициент а с тремя дробными цифрами
        b = round((n*s3-s1*s)/(n*s2-s1**2),3)# коэфициент b с тремя дробными цифрами
        s4 = [a+b/x[i] for i in range(n)] # список значений гиперболической функции

        so = round(sum([abs(y[i] - y1[i]) for i in range(0, len(x))]) / (len(x) * sum(y)) * 100,4)  # средняя ошибка аппроксимации
        plt.plot(x, s4, color='black', linewidth=2)
        plt.legend(loc='best')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(x, y, color='deeppink', linestyle=' ', marker='o')
        plt.grid(True)
        plt.show()

MNK(x,y,st)