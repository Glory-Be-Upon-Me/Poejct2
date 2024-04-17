The vote tallyer takes the lists from the voterdict values (sorted by popularity, descending), put those in a larger list, and then finds the least popular first value. (If two are tied, find which one is the least popular second value, etc., then pick at random if it hits the end.) Then removes that first value from all the lists, in every position, add it to the front of a list of candidates, and repeat.

it ends up with a list with the least popular people at the back. First one is the winner.
