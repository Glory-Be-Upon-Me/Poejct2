import tkinter as tk
from tkinter import ttk, messagebox
import admin
import voter

def switch_to_register():
    login_button.pack_forget()
    register_button.pack(side='right', pady=20, padx=(0, 10))
    toggle_button.config(text="Login", command=switch_to_login)
    title_label.config(text="Register")
    role_label.pack()
    role_option.pack()

def switch_to_login():
    register_button.pack_forget()
    login_button.pack(side='right', pady=20, padx=(0, 10))
    toggle_button.config(text="Sign Up", command=switch_to_register)
    title_label.config(text="Login")
    role_label.pack_forget()
    role_option.pack_forget()

def read_user_db():
    with open('user_db.txt', 'r') as file:
        users = file.readlines()
    user_db = {}
    for user in users:
        username, password, role = user.strip().split(',')
        user_db[username] = {'password': password, 'role': role}
    return user_db

def write_user_db(username, password, role):
    with open('user_db.txt', 'a') as file:
        file.write(f'{username},{password},{role}\n')

def login(username, password, user_db):
    if username in user_db and user_db[username]['password'] == password:
        messagebox.showinfo("Login Success", f"You are now logged in as {user_db[username]['role']}.")
        root.destroy()  # Destroy the login window
        if user_db[username]['role'] == 'admin':
            admin.start_admin_system(username)
        else:
            voter.start_voting_system(username)
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password!")

def validate_entries():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    role = role_var.get()
    if not username or not password or role not in ["admin", "voter"]:
        messagebox.showerror("Validation Error", "All fields are required.")
        return False
    return True

def register(username, password, role, user_db):
    if username in user_db:
        messagebox.showerror("Register Failed", "User already exists!")
    else:
        write_user_db(username, password, role)
        messagebox.showinfo("Register Success", f"You are registered as {role} and now logged in.")
        root.destroy()  # Destroy the login window
        if role == 'admin':
            admin.start_admin_system(username)
        else:
            voter.start_voting_system(username)

def submit_action():
    if validate_entries():
        user_db = read_user_db()
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        role = role_var.get()
        if title_label['text'] == "Login":
            login(username, password, user_db)
        else:
            register(username, password, role, user_db)

root = tk.Tk()
root.title("Voting System Login")
root.geometry('1200x800')
root.configure(bg='#0d1117')

style = ttk.Style()
style.theme_use('clam')
style.configure('TEntry', foreground='white', fieldbackground='#0d1117')
style.configure('TLabel', background='#0d1117', foreground='white')
style.configure('TButton', background='#0d1117', foreground='white')

login_frame = tk.Frame(root, bg='#162447', relief='groove')
login_frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=500)

title_label = ttk.Label(login_frame, text='Login', font=('Segoe UI', 24, 'bold'))
title_label.pack(pady=(40, 20))

username_label = ttk.Label(login_frame, text='Username or Email')
username_label.pack()
username_entry = ttk.Entry(login_frame)
username_entry.pack(fill='x', padx=50)

password_label = ttk.Label(login_frame, text='Password')
password_label.pack(pady=(20, 0))
password_entry = ttk.Entry(login_frame, show='*')
password_entry.pack(fill='x', padx=50)

role_label = ttk.Label(login_frame, text='Select Role')
role_var = tk.StringVar(value='voter')
role_option = ttk.Combobox(login_frame, textvariable=role_var, values=['admin', 'voter'], state='readonly')

login_button = ttk.Button(login_frame, text='Login', command=submit_action)
login_button.pack(side='right', pady=20, padx=(0, 10))

register_button = ttk.Button(login_frame, text='Register', command=submit_action)

toggle_button = ttk.Button(login_frame, text="Sign Up", command=switch_to_register)
toggle_button.pack(side='left', pady=20, padx=(10, 0))

root.mainloop()
