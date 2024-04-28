import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
from vote_storage import write_vote, count_votes

def start_voter_system(username):
    root = tk.Tk()
    root.title("STV Voting System - Voter")
    root.geometry('1200x800')
    root.configure(bg='#0d1117')

    futuristic_font = tkfont.Font(family="Montserrat", size=12)
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TFrame', background='#0d1117')
    style.configure('TButton', background='#21262d', foreground='#c9d1d9', font=futuristic_font)
    style.configure('TLabel', background='#0d1117', foreground='#c9d1d9', font=futuristic_font)
    style.configure('TEntry', foreground='#474747', font=futuristic_font)

    header_frame = ttk.Frame(root)
    header_frame.pack(fill='x', pady=20)
    button_frame = ttk.Frame(root)
    button_frame.pack(pady=20)
    status_frame = ttk.Frame(root)
    status_frame.pack(fill='x', pady=10)

    header_label = ttk.Label(header_frame, text="STV Voting System", font=("Montserrat", 24, "bold"))
    header_label.pack()
    welcome_label = ttk.Label(root, text=f"Welcome, {username}", font=("Helvetica", 16), background='#0d1117', foreground='white')
    welcome_label.place(relx=0.9, rely=0.05, anchor='center')

    # Voting management
    clicked = tk.StringVar()
    clicked.set("Select a candidate")
    candidate_list = ["Candidate A", "Candidate B", "Candidate C"]

    vote_options = ttk.OptionMenu(button_frame, clicked, "Select a candidate", *candidate_list)
    vote_options.pack()
    vote_button = ttk.Button(button_frame, text="Cast Vote", command=lambda: cast_vote())
    vote_button.pack()

    status_label = ttk.Label(status_frame, text="", font=("Montserrat", 14))
    status_label.pack()

    def cast_vote():
        candidate = clicked.get()
        if candidate != "Select a candidate":
            write_vote(candidate)
            status_label.config(text=f'Thank you for voting for {candidate}, {username}!')

    root.mainloop()

if __name__ == "__main__":
    start_voter_system("VoterUser")
