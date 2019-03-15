from tkinter import *


curexpression = ''


def calculate(curexpression):
    outputwindow.configure(text=curexpression)


def makeexp(curexpression, toappend):
    curexpression += toappend
    outputwindow.configure(text=curexpression)


window = Tk()
window.title('Calculator')
positionRight = int(window.winfo_screenwidth()/2 - 400)
positionDown = int(window.winfo_screenheight()/2 - 400)
window.geometry("800x800+{}+{}".format(positionRight, positionDown))


outputwindow = Label(window, text='11111111111', font=('Arial', 30))
outputwindow.pack()
outputwindow.place(anchor='center', height=500, width=1000, x=400, y=50)


buttons = Frame(window)
buttons.pack()
buttons.place(anchor='center', x=400, y=400)


numbers = [[] for _ in range(3)]
for i in range(3):
    for j in range(1, 4):
        numbers[i].append(Button(buttons, text=str(i*3 + j), font=('Arial', 15), command=makeexp(curexpression, str(i*3 + j))))
        numbers[i][j - 1].grid(column=j, row=i)


divide = Button(buttons, text='/', font=('Arial', 15), command=makeexp(curexpression, '/'))
divide.grid(column=4, row=0)

multiply = Button(buttons, text='*', font=('Arial', 15), command=makeexp(curexpression, '*'))
multiply.grid(column=4, row=1)

subtract = Button(buttons, text='-', font=('Arial', 15), command=makeexp(curexpression, '-'))
subtract.grid(column=4, row=2)

addition = Button(buttons, text='+', font=('Arial', 15), command=makeexp(curexpression, '+'))
addition.grid(column=4, row=3)

solve = Button(buttons, text='=', font=('Arial', 15), command=calculate(curexpression))
solve.grid(column=3, row=3)

zero = Button(buttons, text='0', font=('Arial', 15), command=makeexp(curexpression, '0'))
zero.grid(column=1, row=3)

decimal = Button(buttons, text='.', font=('Arial', 15), command=makeexp(curexpression, '.'))
decimal.grid(column=2, row=3)


window.mainloop()
