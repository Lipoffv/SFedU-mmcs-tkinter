'''
14.
Элементы массива А – целые числа.
Напишите функцию, находящую максимальное число среди отрицательных чисел массива.
Если отрицательных чисел нет, выдать сообщение об этом (для поиска максимума напишите функцию).
'''

# 5456 76 32 876
# 545 878 -3 -546 = -32 e
# -13 4 12 -20 -1 3 13 5

from tkinter import *
from tkinter.messagebox import *


def IWantToBreakFree(event):
    s = entN.get()
    lst = (s.strip()).split()
    m = 0
    M = -1000000
    for i in lst:
        try:
            t = float(i)
        except ValueError:
            showerror("Ошибка заполнения", "Элемент массива не является числом.")
            return
        if t < 0:
            if t > M:
                M = t
            if t < m:
                m = t
    if m == 0:
        lbRES['text'] = 'Нет отрицательных чисел.'
    else:
        lbRES['text'] = '| MAX: %4.2f, MIN: %4.2f |' % (M, m)


root = Tk()
size_w = 620
size_h = 270
w = (root.winfo_screenwidth() - size_w) / 2
h = (root.winfo_screenheight() - size_h) / 2
root.geometry('%dx%d+%d+%d' % (size_w, size_h, w, h))
root.resizable(True, False)
root.config(bg='#FFFFFF')
root.title('Поиск максимального отрицательного числа')

fr_ent = Frame(root, bg='#FFFFFF')

lbN = Label(fr_ent, text='//AN ARRAY// =', bg='#FFFFFF', fg='#434C5D', font=('futura', 12, 'bold')).pack(side=LEFT,
                                                                                                         padx=10)
entN = Entry(fr_ent, bg='#FFFFFF', font=('sans', 12, 'bold'), fg='#434C5D')
entN.insert(0, 0)
entN.focus()
entN.pack(side=LEFT, padx=5)

fr_res = LabelFrame(root, bg='#00AEEF', fg='#FFFFFF', highlightcolor='#FFFFFF', text='Поиск отрицательного числа',
                    font=('Futura', 16, 'bold'), bd=0)

btn = Button(fr_res, text='► Пуск', bg='#FFFFFF', fg='#00AEEF', relief=FLAT, font=('Sans', 12, 'bold'))
btn.bind('<Button-1>', IWantToBreakFree)
btn.pack(side=LEFT, padx=30)
lbRES = Label(fr_res, fg='#FFFFFF', bg='#00AEEF', font=('sans', 16, 'bold'))
lbRES.pack(side=LEFT, padx=20)

fr_ent.pack(side=TOP, expand=YES, fill=BOTH)
fr_res.pack(side=TOP, expand=YES, fill=BOTH)
root.mainloop()
