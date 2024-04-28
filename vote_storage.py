def write_vote(candidate):
    with open("votes_db.txt", "a") as file:
        file.write(candidate + "\n")

def read_votes():
    try:
        with open("votes_db.txt", "r") as file:
            votes = file.readlines()
        votes = [vote.strip() for vote in votes]
    except FileNotFoundError:
        votes = []
    return votes

def count_votes():
    votes = read_votes()
    vote_count = {}
    for vote in votes:
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1
    return vote_count
