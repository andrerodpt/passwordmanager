from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open('data.txt', mode='a') as file:
                file.write(f"{website} | {email} | {password}\n")    
                website_entry.delete(0,END)
                password_entry.delete(0,END)
    

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
website_entry.grid(row=1, column=1, columnspan=2, sticky='EW')
website_entry.focus()

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