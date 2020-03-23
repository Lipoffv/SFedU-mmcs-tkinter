'''
1.Вычислить элемент последовательности по заданному номеру n:
'''

def Rec(n):
    if n == 1:
        return 1
    else:
        ans = Rec(n - 1) + 2 * Rec(n - 1) ** 2 + 1
        return ans


n = int(input('n = '))
print(Rec(n))