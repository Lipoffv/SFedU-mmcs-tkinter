'''
12.
Используя методы строк выяснить, является ли данный текст десятичной записью целого числа. Не используя защищенные блоки.
Алгоритм проверки оформить в виде функции.
Учесть, что число может быть со знаком “–5” или “+4” и удалить начальные и завершающие пробелы.
'''

# 13
# hello
# "  -13"
# " +25  "

from tkinter import *
from tkinter.messagebox import *

def GiGiZaWaGi(event):
    s = entN.get()
    s.strip()
    if s == '':
        lbRES['text'] = 'Строка не введена.'
        return
    if s.isdigit():
        lbRES['text'] = 'Строка является целым числом.'
    elif s[0] == '-' or s[0] == '+':
        if s[1:len(s)].isdigit():
            lbRES['text'] = 'Строка является целым числом.'
        else:
            lbRES['text'] = 'Строка не является целым числом.'
    else:
        lbRES['text'] = 'Строка не является целым числом.'


root = Tk()
size_w = 620
size_h = 270
w = (root.winfo_screenwidth() - size_w) / 2
h = (root.winfo_screenheight() - size_h) / 2
root.geometry('%dx%d+%d+%d' % (size_w, size_h, w, h))
root.resizable(True, False)
root.config(bg='#FFFFFF')
root.title('Проверка строки')

fr_ent = Frame(root, bg='#FFFFFF')

lbN = Label(fr_ent, text='s =', bg='#FFFFFF', fg='black', font=('Futura', 12, 'bold')).pack(side=LEFT, padx=10)
entN = Entry(fr_ent, bg='#FFFFFF', font=('sans', 12, 'bold'), fg='black')
entN.insert(0, 0)
entN.focus()
entN.pack(side=LEFT, padx=5)


fr_lf = Frame(root, bg='#FF6800', width=25)
fr_lf.pack(side=LEFT, fill=BOTH)

fr_res = LabelFrame(root, bg='#FF9218', fg='white', highlightcolor='#FFFFFF', text='Проверо4ка строки', font=('Futura', 16, 'bold'), bd=0)


btn = Button(fr_res, text='Проверо4ка ;3', bg='#FFFFFF', fg='#EA7500',relief=FLAT, font=('Sans', 12, 'bold'))
btn.bind('<Button-1>', GiGiZaWaGi)
btn.pack(side=LEFT, padx=30)
lbRES = Label(fr_res, fg='#FFFFFF', bg='#FF9218', font=('sans', 16, 'bold'))
lbRES.pack(side=LEFT, padx=20)

fr_ent.pack(side=TOP, expand=YES, fill=BOTH)
fr_res.pack(side=TOP, expand=YES, fill=BOTH)
root.mainloop()