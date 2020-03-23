'''
8.Дано целое n и вещественное x. Найти значение полинома Чебышева в точке F{n}(x).
'''

def Cheb(n):
    global x
    if n == 0:
        return 0
    elif n == 1:
        return x
    else:
        return 2 * x * Cheb(n - 1) - Cheb(n - 2)


x = float(input('x = '))
n = int(input('n = '))

print('Ответ: %7.3f' % Cheb(n))