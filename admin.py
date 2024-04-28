import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import time
from vote_storage import count_votes, read_votes

def start_admin_system(username):
    root = tk.Tk()
    root.title("STV Voting System - Admin")
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
    form_frame = ttk.Frame(root)
    form_frame.pack(pady=20)
    results_frame = ttk.Frame(root)
    results_frame.pack(fill='x', pady=20)
    status_frame = ttk.Frame(root)
    status_frame.pack(fill='x', pady=10)

    header_label = ttk.Label(header_frame, text="STV Admin Dashboard", font=("Montserrat", 24, "bold"))
    header_label.pack()
    welcome_label = ttk.Label(root, text=f"Welcome, {username}", font=("Helvetica", 16), background='#0d1117', foreground='white')
    welcome_label.place(relx=0.9, rely=0.05, anchor='center')

    status_label = ttk.Label(status_frame, text="", font=("Montserrat", 14))  # Define status_label
    status_label.pack()

    results_labels = {}
    vote_counts = count_votes()
    candidates = set(read_votes())  # Extract unique candidates from votes

    # Candidate management
    candidate_entry = ttk.Entry(form_frame, width=20)
    candidate_entry.grid(row=0, column=1, padx=10, pady=10)
    add_candidate_button = ttk.Button(form_frame, text='Add Candidate', command=lambda: add_candidate(candidate_entry.get()))
    add_candidate_button.grid(row=0, column=2, padx=10, pady=10)

    candidate_list = ["Candidate A", "Candidate B", "Candidate C"]
    votes_dict = {candidate: 0 for candidate in candidate_list}  # Simulated vote counts

    # Displaying results
    for candidate in candidate_list:
        count = vote_counts.get(candidate, 0)
        label = ttk.Label(results_frame, text=f"{candidate}: {count} votes", font=("Helvetica", 14))
        label.pack()
        results_labels[candidate] = label
    def refresh_votes():
        vote_counts = count_votes()
        for candidate, label in results_labels.items():
            count = vote_counts.get(candidate, 0)
            label.config(text=f"{candidate}: {count} votes")
        root.after(5000, refresh_votes)

    def add_candidate(name):
        if name and name not in candidate_list:
            candidate_list.append(name)
            votes_dict[name] = 0  # Initialize vote count
            ttk.Label(results_frame, text=f"{name}: 0 votes", font=("Helvetica", 14)).pack()
            status_label.config(text=f"Added new candidate: {name}")
        else:
            status_label.config(text="Candidate already exists or invalid name.")
    root.after(100, refresh_votes)  # Start the periodic refresh
    root.mainloop()

if __name__ == "__main__":
    start_admin_system("AdminUser")
