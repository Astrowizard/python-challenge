import os
import csv
#----------------------------------------------------------------------------
def get_candidate(can):
    bool = False
    for i in candidates:
        if can == i:
            bool = True
    
    if not bool:
        candidates.append(can)
        c_votes.append(0)
        
def count_vote(can):
    index = 0
    for i in candidates:
        if can == i:
            c_votes[index] += 1
        index += 1
        
def calc_percent():
    for i in c_votes:
        c_percent.append((i/t_votes)*100)
        
def get_winner():
    h = 0
    index = -1
    can = 0
    for i in c_votes:
        index += 1
        if i > h:
            h = i
            can = index
    return can
#-----------------------------------------------------
ifile1 = os.path.join("Resources","election_data.csv")

ofile = os.path.join("results.txt")

t_votes = 0
candidates = []
c_percent = []
c_votes = []
winner = ''

#---------------------------------------------------------------------
with open(ifile1, newline = '') as csv_file:

    data = csv.reader(csv_file, delimiter = ',')
    
    head = next(data)
    
    for row in data:
        t_votes += 1
        get_candidate(row[2])
        count_vote(row[2])
#----------------------------------------------------------------------------
calc_percent()
f = get_winner()
winner = candidates[f]

print(f"Election Results")
print(f"-------------------")
print(f"Total Votes: {t_votes}")
print(f"-------------------")
for i in range(0,len(candidates)):
    print(f"{candidates[i]}:{c_percent[i]:.0f}% ({c_votes[i]})")
print(f"------------------")
print(f"Winner: {winner}")
print(f"------------------")
#--------------------------------------------------------------------
with open(ofile,'w') as out:
    out.write(f"Election Results")
    out.write(f"-------------------")
    out.write(f"Total Votes: {t_votes}")
    out.write(f"-------------------")
    for i in range(0,len(candidates)):
        out.write(f"{candidates[i]}:{c_percent[i]:.0f}% ({c_votes[i]})")
    out.write(f"------------------")
    out.write(f"Winner: {winner}")
    out.write(f"------------------")