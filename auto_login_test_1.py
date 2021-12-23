import tkinter as tk
import time
from pywinauto import Application
import json


wow_dir = r'"C:\\Games\\World of Warcraft\\_classic_\\WowClassic.exe"'
cpu = 12
login_wait = 12

win = tk.Tk()
win.title('Game Launcher')
win.geometry('600x400')
win.resizable(True, True)

current_row = 1
accounts = {}
saved_rows = {}


def add_row():
    global current_row
    global saved_rows

    tk.Label(win, text=f'{current_row}').grid(row=current_row, column=0)
    tk.Label(win, text='Login').grid(row=current_row, column=1)
    tk.Label(win, text='Password').grid(row=current_row, column=3)

    login = tk.Entry(win)
    login.grid(row=current_row, column=2)
    if str(current_row) in saved_rows:
        login.insert(0, saved_rows[str(current_row)][0])

    password = tk.Entry(win)
    password.grid(row=current_row, column=4)
    if str(current_row) in saved_rows:
        password.insert(0, saved_rows[str(current_row)][1])

    accounts[current_row] = [login, password]

    current_row += 1


def delete_last_row():
    global current_row
    if current_row > 1:
        for i in win.grid_slaves(row=current_row - 1):
            i.grid_remove()
        accounts.pop(current_row - 1)
        # launch_queue.pop(current_row - 1)
        current_row -= 1


def launch_all_windows():
    for key, value in accounts.items():
        wow = Application(backend='uia')
        wow.start(wow_dir)
        wow.wait_cpu_usage_lower(threshold=cpu)
        wow.window().type_keys(value[0].get() + '{TAB}')
        wow.window().type_keys(value[1].get())
        # wow.window().type_keys('{ENTER}')
        # time.sleep(login_wait)
        # wow.window().type_keys('{ENTER}')


def save_rows():
    saved_rows = {}
    for key, value in accounts.items():
        saved_rows[key] = [value[0].get(), value[1].get()]
    # print(saved_rows)
    with open('accounts.json', 'w') as json_file:
        json.dump(saved_rows, json_file, indent=3)


def load_rows():
    global saved_rows
    global current_row

    with open('accounts.json', 'r') as json_file:
        saved_rows = json.load(json_file)

    for _ in saved_rows:
        add_row()


tk.Button(win, text='Add row', command=add_row).grid(row=0, column=0)
tk.Button(win, text='Delete row', command=delete_last_row).grid(row=0, column=1)
tk.Button(win, text='Launch all windows', command=launch_all_windows).grid(row=0, column=2)
tk.Button(win, text='Save', command=save_rows).grid(row=0, column=3)
tk.Button(win, text='Load', command=load_rows).grid(row=0, column=4)



# def on_exit(event):
#   win.destroy()
#
# win.bind('<Destroy>', on_exit)


win.mainloop()