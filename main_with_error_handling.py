from tkinter import *
from tkinter import messagebox
import random
# import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B",
               "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
               "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(numbers) for num in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for sym in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    textbox_pwd.insert(0, password)
    # pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = textbox_web.get()
    username = textbox_email.get()
    password = textbox_pwd.get()

    data_dict = {
        website: {
            "email": username,
            "password": password
        }}

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Blank Information", message="Please fill in all the spaces!")
    else:
        can_save = messagebox.askokcancel(title=website, message="Save Password?")
        if can_save:
            with open("data.json", "r") as data_file:
                # Reading available data
                data = json.load(data_file)
                # Updating available data with new data
                data.update(data_dict)

            with open("data.json", "w") as data_file:
                # Saving new data
                json.dump(data, data_file, indent=4)

            textbox_web.delete(0, END)
            textbox_email.delete(0, END)
            textbox_pwd.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

label_web = Label(text="Website:")
label_web.grid(column=0, row=1)

textbox_web = Entry(width=35)
textbox_web.grid(column=1, columnspan=2, row=1)

label_email = Label(text="Email/ Username:")
label_email.grid(column=0, row=2)

textbox_email = Entry(width=35)
textbox_email.grid(column=1, columnspan=2, row=2)

label_pwd = Label(text="Password:")
label_pwd.grid(column=0, row=3)

textbox_pwd = Entry(width=21)
textbox_pwd.grid(column=1, row=3)

button_generate_pwd = Button(text="Generate Password", command=password_generator)
button_generate_pwd.grid(column=2, row=3)

button_add = Button(text="Add", width=30, command=save)
button_add.grid(column=1, columnspan=2, row=4)

window.mainloop()
