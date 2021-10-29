from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:
        try:
            with open("d:/python/100days/day029_data.json","r") as df:
                #Reading old data
                data = json.load(df)
        except FileNotFoundError:
            with open("d:/python/100days/day029_data.json","w") as df:
                json.dump(new_data, df, indent=4)
        else:
            #Updating old data with new
            data.update(new_data)
            
            with open("d:/python/100days/day029_data.json","w") as df:
                #Saving updated data
                json.dump(data, df, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("d:/python/100days/day029_data.json") as df:
            data = json.load(df)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,)



canvas = Canvas(width=200,height=200, highlightthickness=0)
logo = PhotoImage(file="d:/python/100days/day029_logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

#labels
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label = Label(text = "Password:")
password_label.grid(column=0, row=3)

#entries
website_entry = Entry(width=21)
website_entry.grid(column=1,row=1,)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"anobscurereference@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

#buttons
search_button = Button(text = "Search", width=13, command = find_password)
search_button.grid(row=1,column=2)
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3)
add_button = Button(text="Add",width=36, command = save)
add_button.grid(column=1,row=4,columnspan=2)



window.mainloop()