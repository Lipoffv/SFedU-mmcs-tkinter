# Рекурсивная функцию для вычисления F(p):
# p — номер элемента последовательности Фибоначчи, являющийся параметром функции.
def Fib1(k):
    if k == 1 or k == 0:
        return 1
    else:
        return Fib1(k - 2) + Fib1(k - 1)


# Напечатает последовательность F(0), F(1),..., F(n):
def Fib2(n):
    fib = 1
    past = 1
    k = 1
    print(fib, end=' ')
    while k != n:
        print(fib, end=' ')
        past, fib = fib, (past + fib)
        k += 1
    return fib


# Находит номер k и значение первого элемента последовательности Фибо-наччи F(k), который больше, чем заданное число m.
def Fib3(m):
    fib = 1
    past = 1
    k = 1
    while fib <= m:
        past, fib = fib, (past + fib)
        k += 1
    print('Число F(%d) = %d > %d.' % (k, fib, m))


k = int(input('p = '))
n = int(input('n = '))
m = int(input('m = '))

print('F(%d) = %d' % (k, Fib1(k)))
print()
print(Fib2(n))
print()
Fib3(m)