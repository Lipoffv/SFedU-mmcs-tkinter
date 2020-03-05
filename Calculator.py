from tkinter import *  # подключаем tkinter
from tkinter.messagebox import *  # подключаем диалоговые окна tkinter
'''
#202225 — Черно-серый
#292B2F
#2F3136 — Гранитный
#36393F
#6F85D2 — Индиго Крайола
'''
root = Tk()  # создаем главное окно
root['bg'] = '#202225'
# Устанавливаем минимальные и максимальные размеры окна:
size_w = 350
size_h = 200
w = (root.winfo_screenwidth() - size_w) / 2
h = (root.winfo_screenheight() - size_h) / 2
root.geometry('%dx%d+%d+%d' % (size_w, size_h, w, h))
root.minsize(width=350, height=200)
root.maxsize(width=500, height=300)
root.title("Калькулятор")  # заголовок окна

# Создадим 3 фрейма: fr_xy, fr_op и fr_res для размещения компонент.
fr_xy = Frame(root, bg='#292B2F')  # фрейм fr_xy (компоненты для ввода чисел x, y).
fr_xy.pack(side=TOP, expand=YES, fill=X)

# На нем размещаем две метки и два редактора для ввода чисел x, y:
lx = Label(fr_xy, text="x = ", fg='#6F85D2', bg='#36393F')
lx.pack(side=LEFT, padx=10, pady=10)
entX = Entry(fr_xy, cursor= 'pencil', bg='#40444B', relief=FLAT, fg='#6F85D2')
entX.insert(0, 0)  # – в редактор записываем в позицию 0 число 0
entX.pack(side=LEFT, padx=10, pady=10)
entX.focus()  # – редактор будет выбран при старте (иметь фокус ввода)

ly = Label(fr_xy, text="y = ", fg='#6F85D2', bg='#36393F')
ly.pack(side=LEFT, padx=10, pady=10)
entY = Entry(fr_xy, cursor= 'pencil', bg='#40444B', relief=FLAT, fg='#6F85D2')
entY.insert(0, 0)
entY.pack(side=LEFT, padx=10, pady=10)

# Создание фрейма с заголовком fr_op (выбор операции):
fr_op = LabelFrame(root, relief=FLAT, text="Операция:",bg='#292B2F', fg='#6F85D2', font=('sans', 12, 'bold'))
fr_op.pack(side=TOP, expand=YES, fill=X)

# Операцию будем выбирать с помощью виджета Radiobutton:
oper = ['+', '-', '*', '/']  # – список операций

# Вводим строковую переменную tkinter, ее свяжем с выбором Radiobutton
varOper = StringVar()

# В цикле создаем 4 кнопки Radiobutton (связываем их с переменной):
for op in oper:
    Radiobutton(fr_op, text=op, variable=varOper, value=op, bg='#36393F', fg='#6F85D2').pack(side=LEFT,
                                                                 padx=20, pady=10)
varOper.set(oper[0])  # Устанавливаем текущее значение ‘+’

# Создаем 3-й фрейм fr_res (вычисление значения и вывод результата):
fr_res = Frame(root, bg='#292B2F')
fr_res.pack(side=TOP, expand=YES, fill=BOTH)


# Обработчик кнопки:
def OnButtunResult():
    # Защищенный блок, будем пытаться перевести текст из редактора в число:
    try:
        x = float(entX.get())  # извлекаем число из 1-го редактора
    except ValueError:  # если не получилось, выдаем сообщение и выходим
        showerror("Ошибка заполнения", "Переменная x не является числом")
        return
    # Защищенный блок 2:
    try:
        y = float(entY.get())
    except ValueError:
        showerror("Ошибка заполнения", "Переменная y не является числом")
        return

    # В переменную op записываем выбранную операцию:
    op = varOper.get()

    # Вычисляем:
    if op == '+':
        res = x + y
    elif op == '-':
        res = x - y
    elif op == '*':
        res = x * y
    elif op == '/':
        if y != 0:
            res = x / y
        else:
            res = 'NAN'
    else:
        res = 'операция выбрана неправильно'

    # Вывод результата на метку:
    lres['text'] = res
    # Обработчик кнопки закончился.

# Создаем кнопку и метку, к кнопке присоединяем обработчик:
Button(fr_res, text="=", fg='#6F85D2',bg='#36393F', relief=FLAT, cursor='spider', width=10, command=OnButtunResult).pack(side=LEFT,
                                                                padx=30, pady=20)
lres = Label(fr_res, fg='#6F85D2', bg='#36393F')
lres.pack(side=LEFT, padx=30, pady=20)

# Запуск цикла обработки сообщений:
root.mainloop()
