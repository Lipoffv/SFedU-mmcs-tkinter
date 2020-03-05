from tkinter import *
from tkinter.messagebox import *
from math import *
'''
#202225
#292B2F
#2F3136
#36393F
#6F85D2
'''

def pressbutton(event):
    try:
        a = float(entA.get())  # извлекаем число из 1-го редактора
    except ValueError:  # если не получилось, выдаем сообщение и выходим
        showerror("Ошибка заполнения", "Переменная A не является числом.")
        return

    try:
        b = float(entB.get())  # извлекаем число из 1-го редактора
    except ValueError:  # если не получилось, выдаем сообщение и выходим
        showerror("Ошибка заполнения", "Переменная B не является числом.")
        return

    try:
        c = float(entC.get())  # извлекаем число из 1-го редактора
    except ValueError:  # если не получилось, выдаем сообщение и выходим
        showerror("Ошибка заполнения", "Переменная C не является числом.")
        return

    if a == 0:
        if b == 0:
            if c == 0:
                lbRES['text'] = 'x – любое число'
            else:
                lbRES['text'] = 'Нет корней'
        else:
            lbRES['text'] = -c / b
    else:
        D = b ** 2 - 4 * a * c
        if D < 0:
            lbRES['text'] = 'Нет корней'
        elif D == 0:
            x1 = (-b + sqrt(D)) / (2 * a)
            lbRES['text'] = 'x1 = %4.3f' % x1
        else:
            x1 = (-b + sqrt(D)) / (2 * a)
            x2 = (-b - D) / (2 * a)
            lbRES['text'] = 'x1 = %4.3f, x2 = %4.3f' % (x1, x2)


root = Tk()
size_w = 620
size_h = 270
w = (root.winfo_screenwidth() - size_w) / 2
h = (root.winfo_screenheight() - size_h) / 2
root.geometry('%dx%d+%d+%d' % (size_w, size_h, w, h))
root.resizable(True, False)
root.config(bg='#262726')
root.title('Решение квадратного уравнения')

fr_ent = Frame(root, bg='#262726')

lbA = Label(fr_ent, text='A =', bg='#4D1010', fg='#EDE6D5', font=('Sans', 12, 'bold')).pack(side=LEFT, padx=10)
entA = Entry(fr_ent, bg='#FFEBBD', font=('Sans', 10))
# entA.insert(0, 0)
entA.focus()
entA.pack(side=LEFT, padx=5)

lbB = Label(fr_ent, text='B =', bg='#4D1010', fg='#EDE6D5', font=('Sans', 12, 'bold')).pack(side=LEFT, padx=10)
entB = Entry(fr_ent, bg='#FFEBBD', font=('Sans', 10))
# entB.insert(0, 0)
entB.pack(side=LEFT, padx=5)

lbC = Label(fr_ent, text='C =', bg='#4D1010', fg='#EDE6D5', font=('Sans', 12, 'bold')).pack(side=LEFT, padx=10)
entC = Entry(fr_ent, bg='#FFEBBD', font=('Sans', 10))
# entC.insert(0, 0)
entC.pack(side=LEFT, padx=5)

fr_res = Frame(root, bg='#262726')


btn = Button(fr_res, text='x1, x2 =', bg='#4D1010', fg='#EDE6D5',relief=FLAT, font=('Sans', 12, 'bold'))
btn.bind('<Button-1>', pressbutton)
btn.pack(side=LEFT, padx=30)
lbRES = Label(fr_res, fg='#FFEBBD', bg='#262726', font=('Sans', 12, 'bold'))
lbRES.pack(side=LEFT, padx=20)

fr_ent.pack(side=TOP, expand=YES, fill=BOTH)
fr_res.pack(side=TOP, expand=YES, fill=BOTH)
root.mainloop()