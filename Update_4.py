import tkinter as tk

# Initializing global variables ( i also added title for the window and height and width so it doesnt fill up thr whole screen)
root = tk.Tk()
root.title("STV Voting System")
root.geometry('900x600')
voter_dict = {}
candidate_list = []
votes_dict = {candidate: [] for candidate in candidate_list}
ID = None
clicked = tk.StringVar(value="Select a candidate")

# this fucntion generates unique ID for each voter so we can sort out data more efficiently 
def generate_id():
    return max(voter_dict.keys(), default=99) + 1

# Function to add candidates
def add_candidate(name):
    if name not in candidate_list:
        candidate_list.append(name)
        votes_dict[name] = []

# Registering vote function ( ID is set to global variable so it can be used throughout the code)
def register_voter():
    global ID
    ID = generate_id()
    voter_dict[ID] = None
    id_label = tk.Label(root, text=f'Your ID is {ID}')
    id_label.place(x=10, y=100)
    register_button.place_forget()

# Voting function 
def cast_vote():
    if ID in voter_dict:
        voter_dict[ID] = clicked.get()
        update_vote_options()
    else:
        display_error("Please register before voting.")

# Function to update voting options in the dropdown
def update_vote_options():
    drop['menu'].delete(0, 'end')
    for candidate in candidate_list:
        drop['menu'].add_command(label=candidate, command=tk._setit(clicked, candidate))
    clicked.set("Select a candidate")

# tally votes and outcome 
def tally_votes():
    print("Tallying votes...")

# Admin contols ( we still need to make changes to this, cause this this just the code for login, admins have different perms)
def reveal_admin_controls():
    if credential_input.get() == 'admin':
        name_input.place(relx=0.7, rely=0.5, anchor='center')
        name_input_button.place(relx=0.7, rely=0.45, anchor='center')

# this is the error handlijg function 
def display_error(message):
    error_label.config(text=message)
    error_label.place(relx=0.5, rely=0.5, anchor='center')

# UI COMPONENTS SETUP 👇
error_label = tk.Label(root, text='')
register_button = tk.Button(root, text='Register as a voter', command=register_voter)
register_button.place(x=10, y=10)
drop = tk.OptionMenu(root, clicked, *candidate_list)
drop.pack()
vote_button = tk.Button(root, text="Click to vote", command=cast_vote)
vote_button.place(relx=0.5, rely=0.45, anchor='center')
credential_input = tk.Entry()
credential_input.place(rely=0.7, relx=0.5, anchor='center')
credential_button = tk.Button(root, text='Enter secret code', command=reveal_admin_controls)
credential_button.place(rely=0.75, relx=0.5, anchor='center')
name_input = tk.Entry()
name_input_button = tk.Button(root, text='Add candidate', command=lambda: add_candidate(name_input.get()))

tk.mainloop()
