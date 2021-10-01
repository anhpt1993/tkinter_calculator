from tkinter import *

def button_press(button):
    global input_text

    input_text = input_text + str(button)
    input_lable.set(input_text)

def equals():
    global input_text

    try:
        total = str(eval(input_text))
        input_lable.set(total)
        input_text = total
    except ZeroDivisionError:
        input_lable.set("Lỗi chia cho số 0")
        input_text = ""
    except SyntaxError:
        input_lable.set("Lạy má, tính không nổi")
        input_text = ""

def clear():
    global input_text
    input_lable.set("")
    input_text = ""

def backspace():
    global input_text
    input_text = input_text[:len(input_text) - 1]
    input_lable.set(input_text)

window = Tk()
window.title("Basic Calculator")
window.geometry("364x501")
window.resizable(False, False)

# tạo màn hình nhập liệu
input_text = ""
input_lable = StringVar()
nhap_lieu = Label(window,
                  textvariable=input_lable,
                  font = ("calibri", 20),
                  bg = "white",
                  width = 25,
                  height = 2)
nhap_lieu.pack()

# tạo frame chứa number
frame1 = Frame(window)
frame1.pack(side=LEFT)

# tạo các nút bấm và số
button_reset = Button(frame1,
                      text = "AC",
                      font = 35,
                      width = 9,
                      height = 4,
                      command=clear)
button_reset.grid(row=0, column=0)

button_divide = Button(frame1,
                       text = "/",
                       font = 35,
                       width = 9,
                       height = 4,
                       command = lambda: button_press("/"))
button_divide.grid(row=0, column=1)

button_multiply = Button(frame1,
                        text = "*",
                        font = 35,
                        width = 9,
                        height = 4,
                        command = lambda: button_press("*"))
button_multiply.grid(row=0, column=2)

button_7 = Button(frame1,
                  text = 7,
                  font = 35,
                  width = 9,
                  height = 4,
                  command = lambda: button_press(7))
button_7.grid(row=1, column=0)

button_8 = Button(frame1,
                  text = 8,
                  font = 35,
                  width = 9,
                  height = 4,
                  command = lambda: button_press(8))
button_8.grid(row=1, column=1)

button_9 = Button(frame1,
                  text = 9,
                  font = 35,
                  width = 9,
                  height = 4,
                  command = lambda: button_press(9))
button_9.grid(row=1, column=2)

button_4 = Button(frame1,
                  text = 4,
                  font = 35,
                  width = 9,
                  height = 4,
                  command = lambda: button_press(4))
button_4.grid(row=2, column=0)

button_5 = Button(frame1,
                  text = 5,
                  font = 35,
                  width = 9,
                  height = 4,
                  command = lambda: button_press(5))
button_5.grid(row=2, column=1)

button_6 = Button(frame1,
                  text = 6,
                  font = 35,
                  width = 9,
                  height = 4,
                  command = lambda: button_press(6))
button_6.grid(row=2, column=2)

button_1 = Button(frame1,
                  text = 1,
                  font = 35,
                  width = 9,
                  height = 4,
                  command = lambda: button_press(1))
button_1.grid(row=3, column=0)

button_2 = Button(frame1,
                  text = 2,
                  font = 35,
                  width = 9,
                  height = 4,
                  command = lambda: button_press(2))
button_2.grid(row=3, column=1)

button_3 = Button(frame1,
                  text = 3,
                  font = 35,
                  width = 9,
                  height = 4,
                  command = lambda: button_press(3))
button_3.grid(row=3, column=2)

button_0 = Button(frame1,
                  text = 0,
                  font = 35,
                  width = 9,
                  height = 4,
                  command = lambda: button_press(0))
button_0.grid(row=4, column=0)

button_del = Button(frame1,
                    text = "Del",
                    font = 35,
                    width = 9,
                    height = 4,
                    command= backspace)
button_del.grid(row=4, column=1)

button_decimal = Button(frame1,
                        text = ".",
                        font = 35,
                        width = 9,
                        height = 4,
                        command = lambda: button_press("."))
button_decimal.grid(row=4, column=2)

# tạo frame chứa các nút bấm -, + & =
frame2 = Frame(window)
frame2.pack(side=LEFT)

# tạo các nút bấm -, + & =
button_minus = Button(frame2,
                      text = "-",
                      font = 35,
                      width = 9,
                      height = 4,
                      command = lambda: button_press("-"))
button_minus.grid(row=0, column=0)

button_plus = Button(frame2,
                     text = "+",
                     font = 35,
                     width = 9,
                     height = 9,
                     command = lambda: button_press("+"))
button_plus.grid(row=1, column=0)

button_equal = Button(frame2,
                      text = "=",
                      font = 35,
                      width = 9,
                      height = 9,
                      command = equals)
button_equal.grid(row=2, column=0)


window.mainloop()