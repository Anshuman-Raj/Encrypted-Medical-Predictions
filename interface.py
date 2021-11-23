from tkinter import *
import os
import json
import time
root = Tk()
root.title('User\'s Details')
root.geometry("600x600")
entry_list = []
tags = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
x_axis_label = {0: 5, 1: 350}
x_axis_entry = {0: 75, 1: 410}
values = []

T = []


def submit():
    for vals in entry_list:
        values.append(vals.get())
    arguments = " ".join(values)
    print(arguments)
    pop_win = Tk()
    pop_win.geometry("300x300")
    pop_win.title('Confirmation Window')

    message = Label(master=pop_win, text="Your data has been submitted!", justify='center', font=('Arial', 13, 'bold'))
    message.place(x=30, y=30)

    arguments = "python clientside_enc_dec.py "+arguments
    os.system('cmd /c '+arguments)
    pop_win.eval('tk::PlaceWindow . center')
    root.destroy()
    T.append(pop_win)
    submit_button_ = Button(master=pop_win, command=check_result, text='CHECK RESULT', height=2, width=12, padx=10, pady=10)
    submit_button_.place(x=90, y=100)


def check_result():

    result_window = Tk()
    result_window.geometry('400x100')
    result_window.title('Result')
    # Server will be running on AWS Lambda
    time.sleep(12)
    os.system('cmd /c "python clientwork.py"')
    T[0].destroy()

    with open('results.json', 'r') as res_file:
        mes_res = json.load(res_file)
        message = mes_res['result']
        message_box = Label(master=result_window, text=message, font=('Arial', 15, 'bold'))
        message_box.place(x=20, y=20)
    result_window.eval('tk::PlaceWindow . center')
    os.remove('results.json')


for i in range(13):
    datapoint_name = Label(root, text=tags[i].upper())
    datapoint_name.place(x=7 - len(tags[i]) + x_axis_label[i % 2], y=20 + (i // 2) * 85)
    data_entry = Entry(root, width=20, border=5, justify='center')
    data_entry.place(x=x_axis_entry[i % 2], y=20 + (i // 2) * 85)
    entry_list.append(data_entry)

submit_button = Button(master=root, command=submit, text='SUBMIT', height=2, width=10, padx=10, pady=10)
submit_button.place(x=x_axis_entry[1]-30, y=6*85)

mainloop()
