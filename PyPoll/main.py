import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, 'r', newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    
    #read and store headers
    headers = next(reader)
    
    #variables and lists for analysis
    voterid = []
    candidate_list = []
    vote = []
    lastrow = None
    can1_total = 0
    can2_total = 0
    can3_total = 0
    
    #for loop looking row by row
    for row in reader:
        
        vote.append(row[2])
        #adding voter id to a list
        if row[0] != voterid:
            voterid.append(row[0])
          
        #adding unique candidates to list
        candidate = row[2]
        if candidate != lastrow and candidate not in candidate_list:
            candidate_list.append(row[2])
        lastrow = candidate
    
    #total votes = length of voter id list
    vote_total = len(voterid)
    
    #checking to see if there are any duplicate voter ids with set function
    ordered =set(voterid)
    ordered_total = len(ordered)
    
    can1 = candidate_list[0]
    can2 = candidate_list[1]
    can3 = candidate_list[2]
   
    for i in vote:
        if i == can1:
            can1_total = int(can1_total) + 1
        elif i ==can2:
            can2_total = int(can2_total) + 1
        elif i ==can3:
            can3_total = int(can3_total) + 1
    
    can1_percent = round((can1_total/vote_total)*100,1)
    can2_percent = round((can2_total/vote_total)*100,1)
    can3_percent = round((can3_total/vote_total)*100,1)
    
    can_totals = [int(can1_total), int(can2_total), int(can3_total)]
    winner_total = max(can_totals)
    
    winner_index = 0
    for x in can_totals:
        if x == winner_total:
            winner_index = can_totals.index(x)  
    winner = candidate_list[winner_index]

    print("Election Results")
    print("-------------------------------------------------")
    if ordered_total ==vote_total:
        print("Total Votes Cast: " + str(vote_total))
    else:
        print("Duplicate Voter IDs recorded")
    print("-------------------------------------------------")
    print(str(can1) + ": " + str(can1_total) + " votes, " + str(can1_percent) + "%")
    print(str(can2) + ": " + str(can2_total) + " votes, " + str(can2_percent) + "%")
    print(str(can3) + ": " + str(can3_total) + " votes, " + str(can3_percent) + "%")
    
    print("Winner: " + str(winner))
    print("-------------------------------------------------")
   
output = os.path.join ( "Analysis", "Voting_Analysis.txt")

with open(output, 'w', newline="") as outputfile:
    writer = csv.writer(outputfile, delimiter=",")
    writer.writerow(["Voting Analysis"])
    writer.writerow([" Election Results"])
    writer.writerow(["-------------------------------------------------"])
    writer.writerow(["Total Votes Cast: " + str(vote_total)])
    writer.writerow([str(can1) + ": " + str(can1_total) + " votes, " + str(can1_percent) + "%"])
    writer.writerow([str(can2) + ": " + str(can2_total) + " votes, " + str(can2_percent) + "%"])
    writer.writerow([str(can3) + ": " + str(can3_total) + " votes, " + str(can3_percent) + "%"])
    writer.writerow([" "])
    writer.writerow(["-------------------------------------------------"])
    writer.writerow(["Winner: " + str(winner)])