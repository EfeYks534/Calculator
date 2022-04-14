from Lexer import *
from Parser import *
from tkinter import *
from tkinter import ttk

calc_text = " "
label = ""

def calculate():
	global calc_text, label
	lexer  = Lexer(calc_text)
	parser = Parser(lexer)

	result = parser.parse()
	calc_text = str(result)

	label.config(text = calc_text)
def plus():
	global calc_text, label
	calc_text = calc_text + " + "
	label.config(text = calc_text)
def minus():
	global calc_text, label
	calc_text = calc_text + " - "
	label.config(text = calc_text)
def multiply():
	global calc_text, label
	calc_text = calc_text + " * "
	label.config(text = calc_text)
def divide():
	global calc_text, label
	calc_text = calc_text + " / "
	label.config(text = calc_text)
def number0():
	global calc_text, label
	calc_text = calc_text + "0"
	label.config(text = calc_text)
def number1():
	global calc_text, label
	calc_text = calc_text + "1"
	label.config(text = calc_text)
def number2():
	global calc_text, label
	calc_text = calc_text + "2"
	label.config(text = calc_text)
def number3():
	global calc_text, label
	calc_text = calc_text + "3"
	label.config(text = calc_text)
def number4():
	global calc_text, label
	calc_text = calc_text + "4"
	label.config(text = calc_text)
def number5():
	global calc_text, label
	calc_text = calc_text + "5"
	label.config(text = calc_text)
def number6():
	global calc_text, label
	calc_text = calc_text + "6"
	label.config(text = calc_text)
def number7():
	global calc_text, label
	calc_text = calc_text + "7"
	label.config(text = calc_text)
def number8():
	global calc_text, label
	calc_text = calc_text + "8"
	label.config(text = calc_text)
def number9():
	global calc_text, label
	calc_text = calc_text + "9"
	label.config(text = calc_text)
def power():
	global calc_text, label
	calc_text = calc_text + "^"
	label.config(text = calc_text)
def dot():
	global calc_text, label
	calc_text = calc_text + "."
	label.config(text = calc_text)
def goback():
	global calc_text, label
	calc_text = calc_text[:-1]
	label.config(text = calc_text)
def clear():
	global calc_text, label
	calc_text = ""
	label.config(text = calc_text)
def factorial():
	global calc_text, label
	calc_text = calc_text + "!"
	label.config(text = calc_text)

# Program başlangıç noktası
def main():
	global calc_text, label
	root = Tk()
	frm2 = ttk.Frame(root, padding=20)
	frm = ttk.Frame(root, padding=20)
	frm2.grid()
	frm.grid()

	label = ttk.Label(frm2, text=" ")
	label.grid(column=0,row=0)

	ttk.Button(frm, text="x", command=multiply).grid(column=1, row=1)
	ttk.Button(frm, text="/", command=divide).grid(column=2, row=1)

	ttk.Button(frm, text="9", command=number9).grid(column=3, row=2)
	ttk.Button(frm, text="8", command=number8).grid(column=2, row=2)
	ttk.Button(frm, text="7", command=number7).grid(column=1, row=2)
	ttk.Button(frm, text="6", command=number6).grid(column=3, row=3)
	ttk.Button(frm, text="5", command=number5).grid(column=2, row=3)
	ttk.Button(frm, text="4", command=number4).grid(column=1, row=3)
	ttk.Button(frm, text="3", command=number3).grid(column=3, row=4)
	ttk.Button(frm, text="2", command=number2).grid(column=2, row=4)
	ttk.Button(frm, text="1", command=number1).grid(column=1, row=4)
	ttk.Button(frm, text="0", command=number0).grid(column=1, row=5)
	ttk.Button(frm, text="^", command=power).grid(column=2, row=5)
	ttk.Button(frm, text="=", command=calculate).grid(column=3, row=5)
	ttk.Button(frm, text=".", command=dot).grid(column=4, row=5)
	ttk.Button(frm, text="+", command=plus).grid(column=3, row=1)
	ttk.Button(frm, text="-", command=minus).grid(column=4, row=1)
	ttk.Button(frm, text="<", command=goback).grid(column=4, row=2)
	ttk.Button(frm, text="C", command=clear).grid(column=4, row=4)
	ttk.Button(frm, text="!", command=factorial).grid(column=4, row=3)


	root.mainloop()

if __name__ == "__main__":
	main()
