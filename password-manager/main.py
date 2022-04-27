from tkinter import *
from tkinter import messagebox  # module that creates pop up boxes
import random
import pyperclip  # copy/paste module
import json

RED = '#FD5D5D'
PINK = '#FF8080'
YELLOW = '#FFF7BC'
GREEN = '#C0EDA6'
GRAY = '#ECECEC'

# ---------------------------SEARCH FOR PASSWORD---------------------------- #


def find_password():
    try:
        with open('data.json', "r") as data_file:
            data = json.load(data_file)
            web = website.get()
    except FileNotFoundError:
        messagebox.askokcancel(message="Password not found.\nEnter a password to add.")

    else:
        if web in data:
            email_data = data[web]["email"]
            password_data = data[web]["password"]
            messagebox.showinfo(title=web, message=f'Email: {email_data}\nPassword: {password_data}')
            ## title doesn't seem to work on my mac
        else:
            messagebox.showinfo(message="Website not found. Enter a password to add.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    characters = ['#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
                  '[', ']', '^', '_', '`', '{', '|', '}', '~', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                  'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    random_pw = random.sample(characters, k=random.randint(8, 12))
    password = "".join(random_pw)
    pw.insert(0, password)
    pyperclip.copy(password)  # copies to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = website.get()
    password = pw.get()
    user_mail = email.get()
    new_data = {
        web: {
            "email": user_mail,
            "password": password,
        }
    }

    if len(web) and len(password) > 0:
        is_ok = messagebox.askokcancel(
            message=f'Click ok if correct.\n Website: {web}\nEmail: {user_mail}\n Password: {password}')

        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)  # reading old data

            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                data.update(new_data) # updating old data with new data
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4) # saving updated data

            finally:
                # Clear all fields after add button is pressed
                website.delete(0, END)
                pw.delete(0, END)
    else:
        messagebox.showinfo(title='Oops', message="Please don't leave blank fields!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
window.configure(bg=YELLOW)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)
canvas.config(bg=YELLOW)

website_label = Label(text='Website:', bg=YELLOW)
website_label.grid(column=0, row=1)

website = Entry(width=21, highlightthickness=0)
website.grid(column=1, row=1)
website.focus()  # puts cursor in this field

user_label = Label(text='Email/Username:', bg=YELLOW)
user_label.grid(column=0, row=2)

email = Entry(width=36, highlightthickness=0)
email.grid(row=2, column=1, columnspan=2)
email.insert(0, 'lynn@email.com')  # can set index to END to put cursor at end of prepopulated text

pw_label = Label(text='Password:', bg=YELLOW)
pw_label.grid(column=0, row=3)

add_button = Button(text='Add', width=37, highlightbackground=GRAY, activeforeground=RED, highlightthickness=0,
                    command=save)
add_button.grid(row=4, column=1, columnspan=2)

pw = Entry(width=21, highlightthickness=0)
pw.grid(column=1, row=3)

gen_pw_button = Button(text='Generate Password', width=15, highlightbackground=PINK, activeforeground=YELLOW,
                       highlightthickness=0, command=generate_password)
gen_pw_button.grid(column=2, row=3)

search_button = Button(width=15, text='Search', highlightbackground=GRAY, activeforeground=YELLOW, highlightthickness=0, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
