# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 18:27:59 2023

@author: taylo
"""

import pandas as pd
import math

#read the shots data csv into a pandas dataframe
df = pd.read_csv('shots_data.csv')
#create a new dataframe for each team
teamA= df[df['team']=='Team A']
teamB= df[df['team']=='Team B']

distance_A = (teamA['x']**2 + teamA['y']**2).apply(math.sqrt)
distance_B = (teamB['x']**2 + teamB['y']**2).apply(math.sqrt)

#next caculate all "Non Corner 3s' made by each team
#For all “Non Corner” 3’s (where Y > 7.8), the 3PT line is 23.75 ft from the center of the hoop
NC3_teamA = teamA[(teamA['y'] > 7.8 ) &  (distance_A > 23.75)]
NC3_teamB = teamB[(teamB['y'] > 7.8)  & (distance_B > 23.75)]


#calculate all Corner 3s made by each team
#For all “Corner” 3’s (where Y <= 7.8), the 3PT line is 22 feet from the court’s Y-axis at all points
C3_teamA = teamA[(teamA['y']<=7.8) & ((teamA['x'] > 22.0) | (-22.0 > teamA['x'])) ]
C3_teamB = teamB[(teamB['y']<=7.8) & ((teamB['x']>22.0) | (-22.0 > teamB['x'])) ]


# Calculate 2-Pointers (2PT)
teamA_2PT = teamA[~((teamA['y'] > 7.8) & (distance_A > 23.75)) & ~((teamA['y'] <= 7.8) & ((teamA['x'] > 22.0) | (teamA['x'] < -22.0)))]
teamB_2PT = teamB[~((teamB['y'] > 7.8) & (distance_B > 23.75)) & ~((teamB['y'] <= 7.8) & ((teamB['x'] > 22.0) | (teamB['x'] < -22.0)))]

#Calculate shot distribution for both teams
team_a_2pt_percentage = round((len(teamA_2PT)/len(teamA))*100, 2)
team_a_nc3_percentage = round((len(NC3_teamA)/len(teamA))*100,2)
team_a_c3_percentage = round((len(C3_teamA)/len(teamA))*100,2)
team_b_2pt_percentage = round((len(teamA_2PT)/len(teamB))*100,2)
team_b_nc3_percentage = round((len(NC3_teamB)/len(teamB))*100,2)
team_b_c3_percentage = round((len(C3_teamB)/len(teamB))*100,2)

#eFG%
FGM_teamA = len(teamA[teamA['fgmade']==1])
FGM_teamB = len(teamB[teamB['fgmade']==1])
threes_made_teamA = len(NC3_teamA[NC3_teamA['fgmade']==1]) + len(C3_teamA[C3_teamA['fgmade']==1])
threes_made_teamB= len(NC3_teamB[NC3_teamB['fgmade']==1]) + len(C3_teamB[C3_teamB['fgmade']==1])
eFG_teamA = round((FGM_teamA + (.5 * threes_made_teamA)) / len(teamA) , 2)
eFG_teamB = round((FGM_teamB + (.5 * threes_made_teamB)) / len(teamB) ,2)

print('Team A:')
print(f'two-pointers: {team_a_2pt_percentage}%')
print(f'non-corner threes: {team_a_nc3_percentage}%')
print(f'corner threes: {team_a_c3_percentage}%')
print(f'eFG%: {eFG_teamA}\n')
print('Team B:')
print(f'two-pointers: {team_b_2pt_percentage}%')
print(f'non-corner threes: {team_b_nc3_percentage}%')
print(f'corner threes: {team_b_c3_percentage}%')
print(f'eFG%: {eFG_teamB}')



