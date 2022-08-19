polls = ['Ben', 'Andy', 'Ben', 'Andy', 'Carol', 'Carol', 'Carol', 'Andy', 'Ben', 'Andy', 'Carol', 'Andy', 'Carol', 'Carol']

candidates = []

votes = []
for person in polls:
    if person not in candidates:
        candidates.append(person)
        votes.append(1)
    else:
        candidate_index = candidates.index(person)
        votes[candidate_index] += 1
max_vote = 0
max_candidates = []
for i in range(len(votes)):
    if votes[i] > max_vote:
        max_vote = votes[i]
        candidate = candidates[i]
        max_candidates = []
        max_candidates.append(candidate)
    elif votes[i] == max_vote:
        candidate = candidates[i]
        max_candidates.append(candidate)
print('The highest vote goes to: ')
print(*max_candidates, sep='\n')
print('Each person had ' + str(max_vote) + ' votes.')
