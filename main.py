from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters_list = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters_list + password_symbols_list + password_numbers_list
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', mode='r') as file:
                data = json.load(file)
                data.update(new_data)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = new_data
        finally:
            with open('data.json', mode='w') as file:
                json.dump(data, file, indent=4)
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    ## Open file
    try:
        with open('data.json', mode='r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showinfo(title="Not Found", message="The user and password for that website was not found.")
    else:
    ## Get the data
        website = website_entry.get()
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"These are the details: \nEmail: {email} \nPassword: {password}") 
        else:
            messagebox.showinfo(title="Not Found", message="The user and password for that website was not found.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=190)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 95, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry()
website_entry.grid(row=1, column=1, sticky='EW')
website_entry.focus()

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, sticky='EW')

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry()
email_entry.insert(0, string='andre@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2, sticky='EW')

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky='EW')

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky='EW')

add_button = Button(text="Add", command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

window.mainloop()