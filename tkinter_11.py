'''
Составьте программу, которая находит наибольший общий делитель двух натуральных чисел м и н.
'''

# 25 10
# 150 95

from tkinter import *
from tkinter.messagebox import *


def HOD(event):
    try:
        a = int(entN.get())
    except ValueError:
        showerror("Ошибка заполнения", "Переменная n не является числом.")
        return
    try:
        b = int(entM.get())
    except ValueError:
        showerror("Ошибка заполнения", "Переменная n не является числом.")
        return

    while b != 0:
        a, b = b, a % b
    lbRES['text'] = 'НОД (n, m)  =  %d' % a


root = Tk()
size_w = 620
size_h = 270
w = (root.winfo_screenwidth() - size_w) / 2
h = (root.winfo_screenheight() - size_h) / 2
root.geometry('%dx%d+%d+%d' % (size_w, size_h, w, h))
root.resizable(True, False)
root.config(bg='#FFFFFF')
root.title('Поиск НОД')

fr_ent = Frame(root, bg='#FFFFFF')

lbN = Label(fr_ent, text='n =', bg='#FFFFFF', fg='#434C5D', font=('Sans', 12, 'bold')).pack(side=LEFT, padx=10)
entN = Entry(fr_ent, bg='#FFFFFF', font=('Sans', 12, 'bold'), fg='#434C5D')
# entA.insert(0, 0)
entN.focus()
entN.pack(side=LEFT, padx=5)

lbM = Label(fr_ent, text='m =', bg='#FFFFFF', fg='#434C5D', font=('Sans', 12, 'bold')).pack(side=LEFT, padx=10)
entM = Entry(fr_ent, bg='#FFFFFF', font=('Sans', 12, 'bold'), fg='#434C5D')
# entB.insert(0, 0)
entM.pack(side=LEFT, padx=5)

fr_lf = Frame(root, bg='#0059A0', width=25)
fr_lf.pack(side=LEFT, fill=BOTH)

fr_res = LabelFrame(root, bg='#00AEEF', fg='#FFFFFF', highlightcolor='#FFFFFF', text='Поиск НОД',
                    font=('Sans', 16, 'bold'), bd=0)

btn = Button(fr_res, text='Найти НОД', bg='#FFFFFF', fg='#00AEEF', relief=FLAT, font=('Sans', 12, 'bold'))
btn.bind('<Button-1>', HOD)
btn.pack(side=LEFT, padx=30)
lbRES = Label(fr_res, fg='#FFFFFF', bg='#00AEEF', font=('Sans', 16, 'bold'))
lbRES.pack(side=LEFT, padx=20)

fr_ent.pack(side=TOP, expand=YES, fill=BOTH)
fr_res.pack(side=TOP, expand=YES, fill=BOTH)
root.mainloop()
