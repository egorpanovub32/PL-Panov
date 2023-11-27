import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

window = Tk()
window.title("Панов Егор Андреевич")
window.geometry("400x250")

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operator = operator_var.get()

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2

    messagebox.showinfo("Результат", f"Результат: {result}")


tab_control = tk.ttk.Notebook(window)
tab_control.pack()
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')
tab_control.pack()

entry1 = tk.Entry(tab1)
entry1.pack()

operator_var = tk.StringVar(tab1)
operator_var.set("+")
operator_dropdown = tk.OptionMenu(tab1, operator_var, "+", "-", "*", "/")
operator_dropdown.pack()

entry2 = tk.Entry(tab1)
entry2.pack()

calculate_button = tk.Button(tab1, text="Вычислить", command=calculate)
calculate_button.pack()


def show_selected_options():
    selected_options = []
    if checkbox1_var.get():
        selected_options.append("Первый")
    if checkbox2_var.get():
        selected_options.append("Второй")
    if checkbox3_var.get():
        selected_options.append("Третий")
    messagebox.showinfo("Выбор", f"Вы выбрали:{selected_options}  пункт")


tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Чекбоксы')
tab_control.pack()

checkbox1_var = tk.BooleanVar()
checkbox2_var = tk.BooleanVar()
checkbox3_var = tk.BooleanVar()

checkbox1 = tk.Checkbutton(tab2, text="Первый", variable=checkbox1_var)
checkbox1.pack()
checkbox2 = tk.Checkbutton(tab2, text="Второй", variable=checkbox2_var)
checkbox2.pack()
checkbox3 = tk.Checkbutton(tab2, text="Третий", variable=checkbox3_var)
checkbox3.pack()

show_selection_button = tk.Button(tab2, text="Показать выбор", command=show_selected_options)
show_selection_button.pack()


def open_file():
    filename = askopenfilename()


tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Работа с текстом')
tab_control.pack()

open_file_button = tk.Button(tab3, text="Загрузить файл", command=open_file)
open_file_button.pack()


window.mainloop()
