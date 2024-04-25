import tkinter as tk
from tkinter import ttk, messagebox
import voting_system

def switch_to_register():
    login_button.pack_forget()
    register_button.pack(side='right', pady=20, padx=(0, 10))
    toggle_button.config(text="Login", command=switch_to_login)
    title_label.config(text="Register")

def switch_to_login():
    register_button.pack_forget()
    login_button.pack(side='right', pady=20, padx=(0, 10))
    toggle_button.config(text="Sign Up", command=switch_to_register)
    title_label.config(text="Login")

def read_user_db():
    with open('user_db.txt', 'r') as file:
        users = file.readlines()
    user_db = {}
    for user in users:
        username, password = user.strip().split(',')
        user_db[username] = password
    return user_db

def write_user_db(username, password):
    with open('user_db.txt', 'a') as file:
        file.write(f'{username},{password}\n')

def login(username, password, user_db):
    if username in user_db and user_db[username] == password:
        messagebox.showinfo("Login Success", "You are now logged in.")
        root.destroy()  # Destroy the login window
        voting_system.start_voting_system(username)  # Start the voting system
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password!")

def validate_entries():
    # Get the username and password from the entry fields
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    # Check if either the username or password is empty
    if not username or not password:
        # If they are, show an error messagebox and return False
        messagebox.showerror("Validation Error", "Username and password are required.")
        return False
    # If both fields are filled, return True
    return True
def register(username, password, user_db):
    if username in user_db:
        messagebox.showerror("Register Failed", "User already exists!")
    else:
        write_user_db(username, password)
        messagebox.showinfo("Register Success", "You are registered and now logged in.")
        root.destroy()  # Destroy the login window
        voting_system.start_voting_system(username)  # Start the voting system

def submit_action():
    # Validate the entries first
    if validate_entries():
        # Read the current 'database' of users
        user_db = read_user_db()
        # Depending on the current mode, perform login or registration
        if title_label['text'] == "Login":
            login(username_entry.get(), password_entry.get(), user_db)
        else:
            register(username_entry.get(), password_entry.get(), user_db)

# Main window setup
root = tk.Tk()
root.title("Voting System Login")
root.geometry('1200x800')
root.configure(bg='#0d1117')

# Style configuration
style = ttk.Style()
style.theme_use('clam')
style.configure('TEntry', foreground='white', fieldbackground='#0d1117', borderwidth=0)
style.configure('TLabel', background='#0d1117', foreground='white')
style.configure('TButton', background='#0d1117', foreground='white', borderwidth=0)

# Center login frame
login_frame = tk.Frame(root, bg='#162447', borderwidth=2, relief='groove')
login_frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=500)

# Title
title_label = ttk.Label(login_frame, text='Login', style='TLabel', font=('Segoe UI', 24, 'bold'))
title_label.pack(pady=(40, 20))

# Username entry
username_label = ttk.Label(login_frame, text='Username or Email', style='TLabel')
username_label.pack()
username_entry = ttk.Entry(login_frame, style='TEntry')
username_entry.pack(fill='x', padx=50)

# Password entry
password_label = ttk.Label(login_frame, text='Password', style='TLabel')
password_label.pack(pady=(20, 0))
password_entry = ttk.Entry(login_frame, style='TEntry', show='*')
password_entry.pack(fill='x', padx=50)

# Login and Register buttons
login_button = ttk.Button(login_frame, text='Login', style='TButton', cursor='hand2', command=submit_action)
login_button.pack(side='right', pady=20, padx=(0, 10))
register_button = ttk.Button(login_frame, text='Register', style='TButton', cursor='hand2', command=submit_action)

# Toggle button to switch between login and register
toggle_button = ttk.Button(login_frame, text="Sign Up", style='TButton', cursor='hand2', command=switch_to_register)
toggle_button.pack(side='left', pady=20, padx=(10, 0))

root.mainloop()
