from tkinter import *
from tkinter.messagebox import *


'''
#202225
#292B2F
#2F3136
#36393F
#6F85D2
'''

root = Tk()
size_w = 600
size_h = 270
w = (root.winfo_screenwidth() - size_w) / 2
h = (root.winfo_screenheight() - size_h) / 2
root.geometry('%dx%d+%d+%d' % (size_w, size_h, w, h))
root.resizable(True, False)
# root.config(bg='#2F3136')
root.title('Поиск MAX')


def pressbutton(event):
    x = entX.get()
    y = entY.get()
    z = entZ.get()
    if x > y and x > z:
        lres['text'] = x
    elif y > z and y > x:
        lres['text'] = y
    else:
        lres['text'] = z

fr_ent = Frame(root, bg='#202225')
fr_res = LabelFrame(root, bg='#292B2F', fg='#6F85D2', text='Поиск максимума из 3-ёх чисел', relief='flat', font='bold')

lb_x = Label(fr_ent, text='x = ', fg='#6F85D2', bg='#2F3136', font='bold').pack(side=LEFT, padx=20, pady=20)
entX = Entry(fr_ent, cursor= 'pencil', relief=FLAT, fg='#6F85D2', bg='#2F3136')
entX.insert(0, 0)
entX.focus()
entX.pack(side=LEFT)


lb_y = Label(fr_ent, text='y = ', fg='#6F85D2', bg='#2F3136', font='bold').pack(side=LEFT, padx=20, pady=20)
entY = Entry(fr_ent, cursor= 'pencil', relief=FLAT, fg='#6F85D2', bg='#2F3136')
entY.insert(0, 0)
entY.pack(side=LEFT)


lb_z = Label(fr_ent, text='z = ', fg='#6F85D2', bg='#2F3136', font='bold').pack(side=LEFT, padx=20, pady=20)
entZ = Entry(fr_ent, cursor= 'pencil', relief=FLAT, fg='#6F85D2', bg='#2F3136')

entZ.insert(0, 0)
entZ.pack(side=LEFT)


bt = Button(fr_res, text='MAX', bg='#2F3136', fg='#6F85D2', relief='ridge', highlightbackground='#6F85D2', font='bold')  # flat, groove, raised, ridge, solid, or sunken
bt.bind('<Button-1>', pressbutton)
bt.pack(side=LEFT, padx=20)
lr = Label(fr_res, text='Ответ: ', bg='#2F3136', fg='#6F85D2', font='bold').pack(side=LEFT)
lres = Label(fr_res, text='%answer here%', bg='#2F3136', fg='#6F85D2', font='bold')
fr_ent.pack(side=TOP, expand=YES, fill=BOTH)
fr_res.pack(side=TOP, expand=YES, fill=BOTH)
lres.pack(side=LEFT, padx=20)

root.mainloop()

