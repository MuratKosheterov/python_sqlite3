import tkinter
import sqlite3

def clear():
    name_entry.delete(0, tkinter.END)
    surname_entry.delete(0, tkinter.END) 

def send_data():
    name = name_entry.get()
    surname = surname_entry.get()
    
    
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, surname TEXT)")

    cursor.execute(
        "INSERT INTO users (name, surname) VALUES (?,?)",
        (name, surname)
    )
    db.commit()



window = tkinter.Tk()
window.title('Registration')
window.geometry('400x500')
window.config(bg='lightgray')

name_lbl = tkinter.Label(text='Name:', font=('Arial', 14), bg='lightgray')
name_lbl.place(x=20, y=50)

name_entry = tkinter.Entry(font=('Arial', 14), width=25)
name_entry.place(x=100, y=50)

surname_lbl = tkinter.Label(text='Surname:', font=('arial', 14), bg='lightgray')
surname_lbl.place(x=20, y=100)

surname_entry = tkinter.Entry(font=('Arial', 14), width=25)
surname_entry.place(x=100, y=100)


send_btn = tkinter.Button(
    text='Send', font=('Arial', 14), bg='lightblue', command=lambda: send_data()
)

send_btn.place(x=200, y=450)

clear_btn = tkinter.Button(
    text='Clear', font=('Arial', 14), bg='lightblue', command=lambda: clear()
)

clear_btn.place(x=300, y=450)


window.mainloop()