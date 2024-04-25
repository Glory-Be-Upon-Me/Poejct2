Enter "sudo" into the input at the bottom and click the button for administrative access.

Adding a candidate adds them to 'candidateList' if they aren't already there, and summons an error message if they are.

Clicking 'Switch to a new voter' will reset the ID system, leaving any votes locked in.

Registering as a voter creates an ID one higher than the highest existing ID number, or just starts at 100. It automatically sets your ID variable (defaulting to None) to that value.

Inputting an ID and clicking the button will also set the ID variable, and it's protected against typos. No passwords, though.

Voting is done through the STV system of voting: select the favorite candidate, enter the choice, and repeat until none are left. This allows you to place your first vote for an unpopular candidate without wasting your vote. Votes are stored as a list in a dictionary; any attempt to vote twice overwrites the previous one.

The vote tallyer takes the lists from the voterdict values (sorted by popularity, descending), put those in a larger list, and then finds the least popular first value. (If two are tied, find which one is the least popular second value, etc., then pick at random if it hits the end.) Then removes that first value from all the lists, in every position, add it to the front of a list of candidates, and repeat.
It ends up with a list with the least popular people at the back. First one is the winner.
Testing for it:
![Screenshot (119)](https://github.com/Glory-Be-Upon-Me/Poejct2/assets/162057176/e6a85a8d-5dca-49da-9f88-ce93eb1fa386)

Buttons are done using Tkinter.
