import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import random


def start_voting_system(username):
    # Initialize main window
    global options
    root = tk.Tk()
    root.title("Advanced STV Voting System")
    root.geometry('1200x800')
    root.configure(bg='#0d1117')

    futuristic_font = tkfont.Font(family="Montserrat", size=12)

    # Styling
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TFrame', background='#0d1117')
    style.configure('TButton', background='#21262d', foreground='#c9d1d9', font=futuristic_font, borderwidth=0,
                    focusthickness=3, focuscolor='#6e768d')
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

    welcome_label = ttk.Label(root, text=f"Welcome {username}", font=("Helvetica", 16), background='#0d1117',
                              foreground='white')
    welcome_label.place(relx=0.9, rely=0.05, anchor='center')

    # Voter registration and candidate entry
    register_button = ttk.Button(form_frame, text='Register as a Voter', command=lambda: register_voter())
    register_button.grid(row=0, column=0, padx=10, pady=10)
    candidate_entry = ttk.Entry(form_frame, width=20)
    candidate_entry.grid(row=0, column=1, padx=10, pady=10)
    add_candidate_button = ttk.Button(form_frame, text='Add Candidate',
                                      command=lambda: add_candidate(candidate_entry.get()))
    add_candidate_button.grid(row=0, column=2, padx=10, pady=10)

    code_entry = ttk.Entry(form_frame, width=20)
    code_entry.grid(row=2, column=1, padx=10, pady=10)
    # Initialize clicked variable and candidate_list
    clicked = tk.StringVar()
    clicked.set("Select a candidate")

    candidate_list = []
    options = []
    # Dropdown for voting
    vote_options = ttk.OptionMenu(button_frame, clicked, "Select a candidate", *options)
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

    # Functions
    def generate_id():
        return max(voter_dict.keys(), default=99) + 1

    def add_candidate(name):
        if name and name not in candidate_list:
            candidate_list.append(name)
            options.append(name)
            update_vote_options()
            status_label.config(text=f"Added new candidate: {name}")

    def register_voter():
        global ID
        ID = generate_id()
        voter_dict[ID] = []
        status_label.config(text=f'Registered with Voter ID: {ID}')

    def cast_vote():
        if ID and clicked.get() != "Select a candidate" or 'Select your next favorite':
            global options
            if len(voter_dict[ID])==len(candidate_list):
                voter_dict[ID]= []
            voter_dict[ID].append(clicked.get())
            status_label.config(text=f'Vote cast for {clicked.get()} by Voter ID {ID}')
            options.remove(clicked.get())
            update_vote_options()
            clicked.set('Select your next favorite')
            if len(options) == 0:
                for i in candidate_list:
                    options.append(i)
                update_vote_options()
                status_label.config(text='Done voting! Vote again to redo it.')

    def update_vote_options():
        global vote_options
        vote_options = ttk.OptionMenu(button_frame, clicked, "Select a candidate", *options)
        vote_options.grid(row=1, column=0, columnspan=2, padx=20, pady=10)
        vote_options['menu'].add_command(command=lambda: clicked.set("Select a candidate"))
        if candidate_list:
            clicked.set('Select a candidate')

    def tally_votes():  # returns the candidates in order, winner to loser.
        print(voter_dict)
        if code_entry.get() == 'sudo':
            global resultList
            resultList = []
            print(tallier(voter_dict, candidate_list))


    def tallier(voters, candidates):
        for i in voters.keys():  # remove all results not corresponding to an undecided candidate
            for j in range(len(voters[i])):
                try:
                    if voters[i][j] not in candidates:
                        voters[i].pop(j)
                except:
                    None

        def find_worst(degree, tempDict):  # search through the votes for the least popular first choice, then repeat for further choices for a tiebreaker, then choose at random for a tiebreakerbreaker
            for i in voters.values():
                try:
                    x = i[degree]
                    tempDict[x] += 1
                except:
                    None
            loser = [None, list(tempDict.values())[0] + 1]
            tie = False
            for i in (tempDict.keys()):
                if tempDict[i] <= loser[1]:
                    loser = [i, tempDict[i]]
                    tie= False
                elif tempDict[i] == loser[1]:
                    tie= True
                    seed = float(random.randrange(0, 2))
                    if degree == len(candidate_list) and seed >=1:
                        loser = [i, tempDict[i]]
            if tie == True:
                loser = find_worst(degree+1,tempDict)
            return loser

        tempDict={}
        for i in candidates:
            tempDict[i] = 0
        loser = find_worst(0,tempDict)
        resultList.append(loser[0])
        candidates.remove(str(loser[0]))
        if len(candidates) == 0:
            final = []
            for i in range(len(resultList)):
                final.append(' ')
            for i in range(len(resultList)):
                final[-i] = resultList[i - 1]
            return final
        else:
            return tallier(voters, candidates)  # recursion!

    code_button = ttk.Button(form_frame, text='Enter secret code', command=tally_votes)
    code_button.grid(row=2, column=2, padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    start_voting_system('me')
