from tkinter import * # подключаем tkinter
from tkinter.messagebox import * # подключаем диалоговые окна tkinter
from math import *

#202225 — Черно-серый
#292B2F
#2F3136 — Гранитный
#36393F
#6F85D2 — Индиго Крайола

root = Tk( )
# создаем главное окно
def count_roots(a, b, c):
    roots=set()
    d = b * b - 4 * a * c
    if d > 0 :
        roots.add((-b+d)/(2*a))
        roots.add((-b-d)/(2*a))
    elif d == 0:
        roots.add((-b+d)/(2*a))

    return roots


# Устанавливаем минимальные и максимальные размеры окна:
root.minsize(width = 350, height = 150)
root.maxsize(width = 500, height = 300)
root.title("Калькулятор") # заголовок окна

# Создадим 3 фрейма: fr_xy, fr_op и fr_res для размещения компонент.
fr_xy = Frame(root, bg='#202225') # фрейм fr_xy (компоненты для ввода чисел x, y).
fr_xy.pack(side = TOP, expand = YES, fill = X)


# На нем размещаем две метки и два редактора для ввода чисел x, y:
lx = Label(fr_xy, text = "a = ", font=('Showcard Gothic', 12))
lx.pack(side = LEFT, padx = 10, pady = 10)
entX = Entry(fr_xy, bg='yellow', fg='blue')
entX.insert(0, 0)

# – в редактор записываем в позицию 0 число 0
entX.pack(side = LEFT, padx=10, pady=10)
entX.focus( )

# – редактор будет выбран при старте (иметь фокус ввода)
ly = Label(fr_xy, text = "b = ", font=('Showcard Gothic', 13))
ly.pack(side=LEFT, padx=10, pady=10)
entY = Entry(fr_xy, bg='yellow', fg='blue')
entY.insert(0, 0)
entY.pack(side = LEFT, padx=10, pady=10)

lz = Label(fr_xy, text = "c = ", font=('Showcard Gothic', 13))
lz.pack(side = LEFT, padx = 10, pady = 10)
entZ = Entry(fr_xy, bg='yellow', fg='blue')
entZ.insert(0, 0)
entZ.pack(side = LEFT, padx=10, pady=10)

# Создание фрейма с заголовком fr_op (выбор операции):
fr_op = LabelFrame(root, text = "Операция:", font=('Showcard Gothic', 13), bg='#202225')
fr_op.pack(side = TOP, expand=YES, fill=X)


# Операцию будем выбирать с помощью виджета Radiobutton:
oper = ['Найти решения квадратного уравнения'] # – список операций


# Вводим строковую переменную tkinter, ее свяжем с выбором Radiobutton
varOper = StringVar( )


# В цикле создаем 4 кнопки Radiobutton (связываем их с переменной):
for op in oper:
    Radiobutton(fr_op, text = op, variable = varOper, value = op, font=('Sans', 13)).pack(side = LEFT, padx = 20, pady = 10)
    varOper.set(oper[0])
# Устанавливаем текущее значение ‘+’

# Создаем 3-й фрейм fr_res (вычисление значения и вывод результата):
fr_res = Frame(root, bg='#202225')
fr_res.pack(side = TOP, expand = YES, fill = BOTH)

# Обработчик кнопки:
def OnButtunResult( ):
    # Защищенный блок, будем пытаться перевести текст из редактора в число:
    try:
        x = float(entX.get()) # извлекаем число из 1-го редактора
    except ValueError: # если не получилось, выдаем сообщение и выходим
        showerror("Ошибка заполнения", "Переменная x не является числом")
        return
    # Защищенный блок 2:
    try:
        y = float(entY.get())
    except ValueError:
        showerror("Ошибка заполнения", "Переменная y не является числом")
        return
    # Защищенный блок 3:
    try:
        z = float(entZ.get())
    except ValueError:
        showerror("Ошибка заполнения", "Переменная z не является числом")
        return
    # В переменную op записываем выбранную операцию:
    op = varOper.get( )
    # Вычисляем:
    res=''
    a = x
    b = y
    c = z
    roots = count_roots(a, b, c)
    if len(roots) == 0:
        showinfo('Решение', 'Действительных корней нет')
    else:
        showinfo('Решение', 'Действительных корней %2d'%len(roots))
        k = 0
        for elem in roots:
            k+=1
            res+=('x%s = ' %k) + str(elem) +'; '
    lres['text'] = res
    return
# Обработчик кнопки закончился.

# Создаем кнопку и метку, к кнопке присоединяем обработчик:
Button(fr_res, text = "=", width = 10, command = OnButtunResult).pack(side = LEFT,padx = 30, pady = 20)

lres = Label(fr_res, text = "", font=('Showcard Gothic', 13))
lres.pack(side = LEFT, padx = 30, pady = 20)


# Запуск цикла обработки сообщений:
root.mainloop()