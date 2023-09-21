import csv

with open("C:/Users/craig/MonashPython/Starter_Code/PyPoll/Resources/election_data.csv", 'r') as file:
    heading = next(file)
    csvreader = csv.reader(file)

    total_vote = list()
    candidates = list()
    candidate_votes = {}

    for row in csvreader:
        total_vote.append(row[0])
        candidate = row[2]

        
        if candidate not in candidates:
            candidates.append(candidate)

        
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0

        
        candidate_votes[candidate] += 1

    total_votes = len(total_vote)

    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {total_votes}')
    print("-------------------------")

    for candidate in candidates:
        votes = candidate_votes[candidate]
        percentage = (votes / total_votes) * 100
        print(f'{candidate}: {percentage:.3f}% ({votes})')

    print("-------------------------")

    
    winner = max(candidate_votes, key=candidate_votes.get)

    
    print(f'Winner: {winner}')
    print("-------------------------")