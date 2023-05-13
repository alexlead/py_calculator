import tkinter as tk
from tkinter import messagebox

def clear():
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, '0')
    calc['state'] = tk.DISABLED
def addNum(num):
    value = calc.get()
    if value == '0':
        value = ''
    calc['state'] = tk.NORMAL
    calc.delete(0,tk.END)  
    calc.insert(0, value + str(num))
    calc['state'] = tk.DISABLED

def addOperation(oper):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0, value + str(oper))
    calc['state'] = tk.DISABLED

def addFloat():
    value = calc.get()
    if not '.' in value:
        value = value + '.'
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        pointIndex = value[value.index('.'):]
        if not '.' in pointIndex[1:]:
            value = value + '.'
    calc['state'] = tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0, value)
    calc['state'] = tk.DISABLED
def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        operation = value[-1]
        value = value[:-1] + operation + value[:-1]
    calc['state'] = tk.NORMAL
    calc.delete(0,tk.END)
    try:
        calc.insert(0, eval(value))
        calc['state'] = tk.DISABLED
    except (NameError, SyntaxError):
        messagebox.showinfo('Error','Incorrect calculation statement')
        clear()
        calc['state'] = tk.DISABLED
    except ZeroDivisionError:
        messagebox.showinfo('Error','I/O dividing to zero')
        clear()
        calc['state'] = tk.DISABLED

def keyPress(event):
    if event.char.isdigit():
        addNum(event.char)
    elif event.char == '.':
        addFloat()
    elif event.char in '+-*/':
        addOperation(event.char)
    elif event.char == '\r':
        calculate()

win = tk.Tk()
h = 250
w = 250
win.title('Application title') #Application title

photo = tk.PhotoImage(file ='calculator.png')
win.iconphoto(False, photo) # set applications icon

win.geometry(f"{w}x{h}+10+20")

win.bind('<Key>', keyPress)

for i in range(4):
    win.grid_columnconfigure(i, minsize=60)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15))
calc['state'] = tk.DISABLED
calc.grid(row=0, column=0, columnspan=4, sticky='ew', padx=5, pady=5)

clear()

tk.Button(text='C', command=lambda: clear(),).grid(row=1, column=3, sticky='ew', padx=5, pady=5)

j = 1
for i in range(1, 11):
    if ((i-1)%3) == 0:
        j += 1
    tk.Button(text=f'{i%10}', command=lambda i=i%10: addNum(i),).grid(row=j, column=(i-1)%3, sticky='ew', padx=5, pady=5)

j = 1
for i in '+-*/':
    j += 1
    tk.Button(text=f'{i}', command=lambda i=i: addOperation(i),).grid(row=j, column=3, sticky='ew', padx=5, pady=5)

tk.Button(text='.', command=lambda: addFloat(),).grid(row=j, column=1, sticky='ew', padx=5, pady=5)

tk.Button(text='=', command=lambda i=i: calculate(),).grid(row=j, column=2, sticky='ew', padx=5, pady=5)

win.mainloop()

