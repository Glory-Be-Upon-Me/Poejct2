import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import random

def start_voting_system(username):
    # Initialize main window
    root = tk.Tk()
    root.title("Advanced STV Voting System")
    root.geometry('1200x800')
    root.configure(bg='#0d1117')

    
    futuristic_font = tkfont.Font(family="Montserrat", size=12)

    # Styling
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TFrame', background='#0d1117')
    style.configure('TButton', background='#21262d', foreground='#c9d1d9', font=futuristic_font, borderwidth=0, focusthickness=3, focuscolor='#6e768d')
    style.configure('TLabel', background='#0d1117', foreground='#c9d1d9', font=futuristic_font)
    style.configure('TEntry', foreground='#474747', font=futuristic_font)
    style.map('TButton', background=[('active', '#6e768d'), ('!active', '#21262d')])

    # Frames for layout
    header_frame = ttk.Frame(root)
    header_frame.pack(fill='x', pady=20)
    form_frame = ttk.Frame(root)
    form_frame.pack(pady=20)
    button_frame = ttk.Frame(root)
    button_frame.pack(pady=20)
    status_frame = ttk.Frame(root)
    status_frame.pack(fill='x', pady=10)

   
    header_label = ttk.Label(header_frame, text="STV Voting System", font=("Montserrat", 24, "bold"))
    header_label.pack()

   
    status_label = ttk.Label(status_frame, text="", font=("Montserrat", 14))
    status_label.pack()
   
    welcome_label = ttk.Label(root, text=f"Welcome {username}", font=("Helvetica", 16), background='#0d1117', foreground='white')
    welcome_label.place(relx=0.9, rely=0.05, anchor='center')

    # Voter registration and candidate entry
    register_button = ttk.Button(form_frame, text='Register as a Voter', command=lambda: register_voter())
    register_button.grid(row=0, column=0, padx=10, pady=10)
    candidate_entry = ttk.Entry(form_frame, width=20)
    candidate_entry.grid(row=0, column=1, padx=10, pady=10)
    add_candidate_button = ttk.Button(form_frame, text='Add Candidate', command=lambda: add_candidate(candidate_entry.get()))
    add_candidate_button.grid(row=0, column=2, padx=10, pady=10)
    

    # Initialize clicked variable and candidate_list
    clicked = tk.StringVar()
    clicked.set("Select a candidate")
    candidate_list = []

    # Dropdown for voting
    vote_options = ttk.OptionMenu(button_frame, clicked, "Select a candidate", *candidate_list)
    vote_options.grid(row=1, column=0, columnspan=2, padx=20, pady=10)
    vote_options['menu'].add_command(label="Select a candidate", command=lambda: clicked.set("Select a candidate"))

    def on_open(event):
        if 'menu' in vote_options.children:
            menu = vote_options.children['menu']
            menu.lift(aboveThis=None)
            for i in range(menu.index('end') + 1):
                menu.entryconfigure(i, background="#21262d", foreground="#c9d1d9")

    vote_options.bind('<ButtonPress-1>', on_open)

   
    vote_button = ttk.Button(button_frame, text="Cast Vote", command=lambda: cast_vote())
    vote_button.grid(row=1, column=2, padx=20, pady=10)

    
    voter_dict = {}
    votes_dict = {}

    # Functions
    def generate_id():
        return max(voter_dict.keys(), default=99) + 1

    def add_candidate(name):
        if name and name not in candidate_list:
            candidate_list.append(name)
            votes_dict[name] = []
            update_vote_options()
            status_label.config(text=f"Added new candidate: {name}")

    def register_voter():
        global ID
        ID = generate_id()
        voter_dict[ID] = None
        status_label.config(text=f'Registered with Voter ID: {ID}')

    def cast_vote():
        if ID and clicked.get() != "Select a candidate":
            voter_dict[ID] = clicked.get()
            status_label.config(text=f'Vote cast for {clicked.get()} by Voter ID {ID}')

    def update_vote_options():
        menu = vote_options['menu']
        menu.delete(0, 'end')
        for candidate in candidate_list:
            menu.add_command(label=candidate, command=lambda value=candidate: clicked.set(value))
        if candidate_list:
            clicked.set(candidate_list[0])

    root.mainloop()


if __name__ == "__main__":
    start_voting_system()

