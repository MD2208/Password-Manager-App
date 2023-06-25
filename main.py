import tkinter
from tkinter import messagebox
import random
import pyperclip
sites = {}
exists_info=""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    password_entry.delete(0,'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    gen_password = "".join(password_list)

    password_entry.insert(0,gen_password)
    #copy the password
    pyperclip.copy(gen_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_entry.get().lower().capitalize()
    email = email_entry.get().lower()
    password = password_entry.get()
    # Check the website and email exists already
    global sites
    global exists_info
    try:
        with open("registeration_data.csv",mode="r") as file:
            registered_sites = file.read().split('\n')
            for site_info in registered_sites:
                if site_info!="":
                    site_info=site_info.split(',')
                    sites[site_info[0]]=site_info[1]
                    exists_info=site_info[2]
    except FileExistsError:
        with open("registeration_data.csv", mode='w') as file:
            file.write("Website,Email,Password\n")
    if website_name in sites and sites[website_name]==email:
        messagebox.showerror(title="Website Exists", message="You have already registered this website by same email!\n"
                             f"Here is your password: {exists_info}")
    elif len(website_name)==0 or len(email)==0 or len(password)==0:
        messagebox.showerror(title="Validation Error", message="Please do not leave any empty fields!")
    else:
        user_okay=messagebox.askokcancel(title="Website", message=f"These are the details to save:\n"
                               f"Website: {website_name}\nEmail: {email}\nPassword: {password}")
        if user_okay:
            with open("registeration_data.csv",mode="a") as file:
                file.write(f"{website_name},{email},{password}\n")
            website_entry.delete(0,'end')
            password_entry.delete(0,'end')
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
# window.minsize(width=400,height=400)
window.config(bg="white",padx=30,pady=30)
window.title("Password Manager") 
# CANVAS
canvas = tkinter.Canvas(width=210,height=210,bg="white",highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)
# LABELS
website_lb = tkinter.Label(text="Website:",bg="white",pady=2)
website_lb.grid(column=0,row=1)

email_lb = tkinter.Label(text="Email/Username:",bg="white",pady=2)
email_lb.grid(column=0,row=2)

password_lb = tkinter.Label(text="Password:",bg="white",pady=2)
password_lb.grid(column=0,row=3)
# INPUTS/ENTRIES
website_entry = tkinter.Entry(width=40)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_entry = tkinter.Entry(width=40)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"your@gmail.com")

password_entry = tkinter.Entry(width=22)
password_entry.grid(column=1,row=3)

#BUTTONS
generate_btn = tkinter.Button(text="Generate Password",highlightthickness=0,bg="white", command=generator)
generate_btn.grid(column=2,row=3)

add_btn = tkinter.Button(text="Add",width=34,highlightthickness=0, bg="white", command=save_password)
add_btn.grid(column=1,row=4,columnspan=2)







window.mainloop()
