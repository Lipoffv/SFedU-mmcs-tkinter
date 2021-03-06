# 4 Синусы и косинусы
from tkinter import * # подключаем tkinter
from tkinter.messagebox import * # подключаем диалоговые окна tkinter
from math import *

root = Tk( )
# создаем главное окно


# Устанавливаем минимальные и максимальные размеры окна:
root.minsize(width = 350, height = 150)
root.maxsize(width = 500, height = 300)
root.title("Калькулятор") # заголовок окна

# Создадим 3 фрейма: fr_xy, fr_op и fr_res для размещения компонент.
fr_xy = Frame(root) # фрейм fr_xy (компоненты для ввода чисел x, y).
fr_xy.pack(side = TOP, expand = YES, fill = X)


# На нем размещаем две метки и два редактора для ввода чисел x, y:
lx = Label(fr_xy, text = "x = ")
lx.pack(side = LEFT, padx = 10, pady = 10)
entX = Entry(fr_xy)
entX.insert(0, 0)

# – в редактор записываем в позицию 0 число 0
entX.pack(side = LEFT, padx=10, pady=10)
entX.focus()

# – редактор будет выбран при старте (иметь фокус ввода)
ly = Label(fr_xy, text = "y = ")
ly.pack(side=LEFT, padx=10, pady=10)
entY = Entry(fr_xy, state = 'disabled')
entY.insert(0, 0)
entY.pack(side = LEFT, padx=10, pady=10)


# Создание фрейма с заголовком fr_op (выбор операции):
fr_op = LabelFrame(root, text = "Операция:")
fr_op.pack(side = TOP, expand=YES, fill=X)


# Операцию будем выбирать с помощью виджета Radiobutton:
oper = ['sin/cos'] # – список операций


# Вводим строковую переменную tkinter, ее свяжем с выбором Radiobutton
varOper = StringVar( )


# В цикле создаем 4 кнопки Radiobutton (связываем их с переменной):
for op in oper:
    Radiobutton(fr_op, text = op, variable = varOper, value = op).pack(side = LEFT, padx = 20, pady = 10)
    varOper.set(oper[0])
# Устанавливаем текущее значение ‘+’

# Создаем 3-й фрейм fr_res (вычисление значения и вывод результата):
fr_res = Frame(root)
fr_res.pack(side = TOP, expand = YES, fill = BOTH)

# Обработчик кнопки:
def OnButtunResult( ):
    # Защищенный блок, будем пытаться перевести текст из редактора в число:
    try:
        x = float(entX.get()) # извлекаем число из 1-го редактора
    except ValueError: # если не получилось, выдаем сообщение и выходим
        showerror("Ошибка заполнения", "Переменная x не является числом")
        return

    # В переменную op записываем выбранную операцию:
    op = varOper.get()
    # Вычисляем:
    if op == 'sin/cos' and x % 2 != 1: res = ((sin(pi*(x*x-x-2)))/(cos(pi*x)+1))
    else:
        showerror('Error', 'Выход за ООП')
        res = 'Выход за ООП'
    # Вывод результата на метку:
    lres['text'] = res
# Обработчик кнопки закончился.

# Создаем кнопку и метку, к кнопке присоединяем обработчик:
Button(fr_res, text = "=", width = 10, command = OnButtunResult).pack(side = LEFT,padx = 30, pady = 20)

lres = Label(fr_res, text = "")
lres.pack(side = LEFT, padx = 30, pady = 20)


# Запуск цикла обработки сообщений:
root.mainloop( )