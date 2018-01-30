#!/usr/bin/env python3

import json

# I need to store the team names of all three names in finals
# I need to store the raw score of each team for each finals quiz (could be 1, 2, 3, 4)
# I need to store the team points score of each team for each finals quiz (could be 1, 2, 3, 4)
# I need to calculate 1st, 2nd, 3rd place for each finals quiz (could be 1, 2, 3, 4 quizzes)

# Based on the number of quizzes I need to apply logic to figure out 1st, 2nd and 3rd

# I need the program to return the 1st, 2nd, 3rd place teams

a_tm = input("What is the name of the 1st team in Finals?")
b_tm = input("What is the name of the 2nd team in Finals?")
c_tm = input("What is the name of the 3rd team in Finals?")
teams = [a_tm, b_tm, c_tm]

teams_list = {
    a_tm: [],
    b_tm: [],
    c_tm: [],
 
}

#I got the teams here from the user and stored them in a list
#they're outside a function because I need them in the global namespace
#I also made a teams_list dictionary that will hold team names and raw scores

def get_raw_score():
'''
This gets the raw scores for each of the teams in finals form the user
'''
    for team in teams:
        score = input("What did {} score in raw points in this finals quiz?".format(team))
        teams_list[team].append(score)

get_raw_score()
print(teams_list)
get_raw_score()
print(teams_list)



#writing to a text file is the only way I know how to "save state"
#one use case is a user enters the scores for Quiz 1, then exits the program and comes back to do it for Quiz 2
with open('FinalsScores.txt', 'w') as file:
     file.write(json.dumps(teams_list))

with open('FinalsScores.txt', 'r') as infile:
     for line in infile:
        print('> {}'.format(line))


#I plan to add in a user menu to select from these options:
# Enter teams
# Enter scores
# Request report




