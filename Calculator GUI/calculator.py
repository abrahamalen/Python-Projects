from tkinter import *
from tkinter import messagebox
import math

screen = Tk()
screen.title("Calculator")
screen.geometry("400x515")
screen.resizable(0, 0)
screen.iconbitmap("cal.ico")
screen.configure(bg = '#5e6265')


def click(number):
    global operation
    operation += str(number)
    data.set(operation)


def clear():
    global operation
    operation = ''
    data.set(operation)


def equal():
    global operation
    try:
        result = eval(operation)
        operation = str(result)
        data.set(result)
    except:
        messagebox.showinfo(title = "Notification", message = "No Values Found..!!", )


def backspace():
    global operation
    operation = operation[: -1]
    data.set(operation)


def percentage():
    global operation
    result = eval(operation)
    result = result / 100
    operation = str(result)
    data.set(result)


def sqr():
    global operation
    sq = int(operation)
    result = (sq ** 2)
    operation = str(result)
    data.set(result)


def sqt():
    global operation
    sqt = float(operation)
    result = math.sqrt(sqt)
    operation = str(result)
    data.set(result)


def sin_value():
    global operation
    sinv = float(operation)
    result = math.sin(math.radians(sinv))
    operation = str(result)
    data.set(result)


def cos_value():
    global operation
    cosv = float(operation)
    result = math.sin(math.radians(cosv))
    operation = str(result)
    data.set(result)


def tan_value():
    global operation
    tanv = float(operation)
    result = math.sin(math.radians(tanv))
    operation = str(result)
    data.set(result)


data = StringVar()
operation = ""

display = Label(screen,
                background = "#759c79",
                fg = "#171a17",
                font = ("Verdana", 20),
                text = "Display",
                anchor = SE,
                padx = 10,
                pady = 10,
                relief = SUNKEN,
                border = 8,
                width = 21,
                textvariable = data

                )
display.grid(row = 0, columnspan = 10, )

btn7 = Button(screen, text = '7', font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff",
              command = lambda: click(7))
btn7.grid(row = 1, column = 0, )

btn8 = Button(screen, text = '8', font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff",
              command = lambda: click(8)
              )
btn8.grid(row = 1, column = 1, )

btn9 = Button(screen, text = '9', font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff",
              command = lambda: click(9)
              )
btn9.grid(row = 1, column = 3, )

btn_multi = Button(screen, text = '*', font = ("Verdana", 20), padx = 16, pady = 16,
                   relief = GROOVE,
                   border = 4,
                   background = "#000000",
                   fg = "#ffffff",
                   command = lambda: click('*')
                   )
btn_multi.grid(row = 1, column = 4, )

btn_sqr = Button(screen, text = 'x' + chr(178), font = ("Verdana", 18),
                 padx = 16,
                 pady = 18,
                 relief = GROOVE,
                 border = 4,
                 background = "#000000",
                 fg = "#ffffff",
                 command = sqr,
                 )
btn_sqr.grid(row = 1, column = 5, )

btn4 = Button(screen, text = '4', font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff",
              command = lambda: click(4)
              )
btn4.grid(row = 2, column = 0, )

btn5 = Button(screen, text = '5', font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff",
              command = lambda: click(5)
              )
btn5.grid(row = 2, column = 1, )

btn6 = Button(screen, text = '6', font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff",
              command = lambda: click(6)
              )
btn6.grid(row = 2, column = 3, )

btn_division = Button(screen,
                      text = chr(247),
                      font = ("Verdana", 19),
                      padx = 16,
                      pady = 16,
                      relief = GROOVE,
                      border = 4,
                      background = "#000000",
                      fg = "#ffffff",
                      command = lambda: click('/')
                      )
btn_division.grid(row = 2, column = 4, )

btn_sqt = Button(screen,
                 text = u"\u221ax",
                 font = ("Verdana", 17),
                 padx = 15,
                 pady = 19,
                 relief = GROOVE,
                 border = 4,
                 background = "#000000",
                 fg = "#ffffff",
                 command = sqt,
                 )
btn_sqt.grid(row = 2, column = 5, )

btn1 = Button(screen, text = '1', font = ("Verdana", 18), padx = 19, pady = 18,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff",
              command = lambda: click(1))
btn1.grid(row = 3, column = 0, )

btn2 = Button(screen, text = '2', font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff",
              command = lambda: click(2)
              )
btn2.grid(row = 3, column = '1', )

btn3 = Button(screen, text = 3, font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff",
              command = lambda: click(3)
              )
btn3.grid(row = 3, column = 3, )

btn_subtract = Button(screen, text = '-', font = ("Verdana", 20), padx = 19, pady = 16,
                      relief = GROOVE,
                      border = 4,
                      background = "#000000",
                      fg = "#ffffff",
                      command = lambda: click('-')
                      )
btn_subtract.grid(row = 3, column = 4, )

btn_sin = Button(screen, text = 'sin', font = ("Verdana", 15),
                 padx = 17,
                 pady = 21,
                 relief = GROOVE,
                 border = 4,
                 background = "#000000",
                 fg = "#ffffff",
                 command = sin_value,
                 )
btn_sin.grid(row = 3, column = 5, )

btn0 = Button(screen, text = '0', font = ("Verdana", 20), padx = 16, pady = 16,
              relief = GROOVE,
              border = 4,
              background = "#000000",
              fg = "#ffffff",
              command = lambda: click(0))
btn0.grid(row = 4, column = 0, )

btn_cancel = Button(screen, text = 'C', font = ("Verdana", 20), padx = 15, pady = 16,
                    relief = GROOVE,
                    border = 4,
                    background = "#000000",
                    fg = "#ffffff",
                    command = clear,
                    )
btn_cancel.grid(row = 4, column = 1, )

btn_equal = Button(screen, text = '=', font = ("Verdana", 20), padx = 13, pady = 12,
                   relief = GROOVE,
                   border = 4,
                   background = "#035efc",
                   fg = "#ffffff",
                   command = equal,
                   )
btn_equal.grid(row = 5, column = 4, )

btn_add = Button(screen,
                 text = '+',
                 font = ("Verdana", 20),
                 padx = 14,
                 pady = 15,
                 relief = GROOVE,
                 border = 4,
                 background = "#000000",
                 fg = "#ffffff",
                 command = lambda: click('+')
                 )
btn_add.grid(row = 4, column = 4, )
btn_cos = Button(screen,
                 text = 'cos',
                 font = ("Verdana", 15),
                 padx = 16,
                 pady = 21,
                 relief = GROOVE,
                 border = 4,
                 background = "#000000",
                 fg = "#ffffff",
                 command = cos_value,
                 )
btn_cos.grid(row = 4, column = 5, )

btn_point = Button(screen, text = '.', font = ("Verdana", 20),
                   padx = 19, pady = 13,
                   relief = GROOVE,
                   border = 4,
                   background = "#000000",
                   fg = "#ffffff",
                   command = lambda: click('.'))
btn_point.grid(row = 5, column = 0, )

btn_per = Button(screen,
                 text = '%',
                 font = ("Verdana", 16),
                 padx = 16,
                 pady = 19,
                 relief = GROOVE,
                 border = 4,
                 background = "#000000",
                 fg = "#ffffff",
                 command = percentage
                 )
btn_per.grid(row = 5, column = 1, )

btn_p_m = Button(screen, text = '+/-', font = ("Verdana", 14),
                 padx = 12,
                 pady = 21,
                 relief = GROOVE,
                 border = 4,
                 background = "#000000",
                 fg = "#ffffff",
                 command = lambda: click('-'),
                 )
btn_p_m.grid(row = 5, column = 3, )

btn_back = Button(screen,
                  text = u"\u2190",
                  font = ("Verdana", 18),
                  padx = 14,
                  pady = 17,
                  relief = GROOVE,
                  border = 4,
                  background = "#000000",
                  fg = "#ffffff",
                  command = backspace,
                  )
btn_back.grid(row = 4, column = 3, )

btn_tan = Button(screen,
                 text = 'tan',
                 font = ("Verdana", 15),
                 padx = 16,
                 pady = 19,
                 relief = GROOVE,
                 border = 4,
                 background = "#000000",
                 fg = "#ffffff",
                 command = tan_value,
                 )
btn_tan.grid(row = 5, column = 5, )

screen.mainloop()