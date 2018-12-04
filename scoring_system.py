from pandas import *
import numpy as np
engine='python'

# Test Link: https://scores.collegesailing.org/f18/victorian-urn/

#link = input('Link to Results = ')
#event = input("Event Type (SC, SC_alt, Coed A, Coed B, Coed C, W SC, Women's A, Women's B)= ")

event = 'Coed A'

#link = input('Regatta Results Link = ')

#table = pandas.read_html(link, header=0, index_col=0)

table = pandas.read_html('https://scores.collegesailing.org/f18/victorian-urn/', header=0, index_col=0)

table2 = table[0]
"""table2.columns = ['Position', 'Flag',
                  'School', 'Team', 'A', 'Pa', 
                  'B', 'Pb', 'Total']"""

table3 = table2.set_index('Unnamed: 1')

"""if event = 'A'
    column=1

    for i in range(0, 34)"""

print(table3)

#print(table3.shape)

print(table3.School)

c = len(table3.School)
print(c)



#scoring = pandas.ExcelFile('/home/thomas/Documents/Code/Sailing_Techscore/Rank_Values.xls')

score = pandas.read_excel(
    'Rank_Values.xlsx', event)

#score.columns = ['Place1', 'Score1', 'Na', 'Place2', 'Score2']

# print(score.Place)
# print(score.Place)

print(list(score))
print(score)

teams=pandas.read_html('https://docs.google.com/spreadsheets/d/1oDTZazH5M4ErQVKs3YtdrKEDRSgwDWMY_AM40SSpmjY/edit', header=0, index_col=0)
print(teams)