'''
17.
(Виджет ползунок Scale) Создайте программу, которая опрашивает пользователя, результат выдает на метку.
В программе используйте виджет Scale для ответов на вопросы с выбором целочисленного значения.
Например, спрашивается ФИО, курс, группа.
Замечание.
Ползунки Scales см. [1, стр. 614, 599 (переменные)] и электронные ресурсы.
'''

from tkinter import *
from tkinter.messagebox import *


def SpulaeMunlae(event):
    FIO = str(name.get())
    if FIO == '':
        showerror('Ошибка', 'ФИО не введено.')
        return
    number = course.get()
    grp = group.get()
    # RES['text'] = 'Да это же', FIO, 'c', number, 'курса', grp, 'группы!'
    RES['text'] = 'Да это же %s с %d курса %d группы!' % (FIO, number, grp)


root = Tk()
size_w = 620
size_h = 270
w = (root.winfo_screenwidth() - size_w) / 2
h = (root.winfo_screenheight() - size_h) / 2
root.geometry('%dx%d+%d+%d' % (size_w, size_h, w, h))
root.resizable(True, False)
root.config(bg='#FFFFFF')
root.title('Божемойужедвачасаночияхочуспать')

lb_choose = Frame(root, )
lbNAME = Label(lb_choose, text='Фамилия Имя Отчество').pack(side=TOP, expand=YES, fill=BOTH)
name = Entry(lb_choose)
name.pack(side=TOP, expand=YES)
# scroll = Scrollbar(lb_choose, command=name.yview)
# scroll.pack(side=LEFT, fill=Y)
lbCOURSE = Label(lb_choose, text='Курс').pack(side=TOP, expand=YES, fill=BOTH)
course = Scale(lb_choose, from_=1, to=4, length=100, orient=HORIZONTAL)
course.pack(side=TOP, expand=YES)

lbGROUP = Label(lb_choose, text='Номер группы').pack(side=TOP)
group = Scale(lb_choose, from_=1, to=12, length=200, orient=HORIZONTAL)
group.pack(side=TOP, expand=YES)

lb_res = LabelFrame(root, text='Результат выбора')
RES = Label(lb_res, )
btn = Button(lb_res, text=' ► ')
btn.bind('<Button-1>', SpulaeMunlae)
btn.pack(side=LEFT)
Label(lb_res, text='Кто этот покемон?').pack(side=TOP)
RES.pack(side=TOP)

lb_choose.pack(side=TOP, expand=YES, fill=BOTH)
lb_res.pack(side=TOP, expand=YES, fill=BOTH)
root.mainloop()
