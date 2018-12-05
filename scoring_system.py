from pandas import *
import numpy as np
import math

engine='python'

# Test Link: https://scores.collegesailing.org/f18/victorian-urn/

#link = input('Link to Results = ')
#event = input("Event Type (SC, SC_alt, Coed A, Coed B, Coed C, W SC, Women's A, Women's B)= ")

###Evaluate Link Data
teams=pandas.read_html('https://docs.google.com/spreadsheets/d/1oDTZazH5M4ErQVKs3YtdrKEDRSgwDWMY_AM40SSpmjY/edit', header=0, index_col=0)
linksSheet= pandas.read_html('https://docs.google.com/spreadsheets/d/1FG4fDoh5nt_hqBfj6m8Ndt0qsKWJYDmauJHY5tUu1HQ/edit#gid=0', header=0, index_col=0)

scoringfile = pandas.ExcelFile('Rank_Values2.xlsx')
scoringTable_sc = pandas.read_excel(scoringfile, 'SC')
scoringTable_sc_alt = pandas.read_excel(scoringfile, 'SC_alt')
scoringTable_coed_a = pandas.read_excel(scoringfile, "Coed A")
scoringTable_coed_b = pandas.read_excel(scoringfile, 'Coed B')
scoringTable_coed_c = pandas.read_excel(scoringfile, 'Coed C')
scoringTable_w_sc = pandas.read_excel(scoringfile, 'W SC')
scoringTable_w_a = pandas.read_excel(scoringfile, "Women's A")
scoringTable_w_b = pandas.read_excel(scoringfile, "Women's B")

"""events = Array[SC, SC_alt, Coed A, Coed B, Coed C, W SC, Women's A, Women's B]


"""

#print(scoringTable_coed_b)

links=linksSheet[0]
links.columns = ['regatta', 'link', 'type']
num_regatta = len(links.link)

#print(links.type[4])
##print(links)
##print(list (links))


for i in range(2, num_regatta+1):
   
    link = links.link[i]
    #print(link)
    resultsTable = pandas.read_html(link, header=0, index_col=0)       
    results = resultsTable[0]

    

    results.columns = [c.replace('Unnamed: 1', 'Place') for c in results.columns]

    num_teams = len(results.Place)

    scoringSheet = pandas.read_excel(scoringfile, links.type[i])
    scoringTable = scoringSheet[scoringSheet.columns[(20-num_teams)]]
    scoringTable.dropna(inplace=True)
    scoringTable.columns = ['points']
    #print(links.type[i])
    #print(num_teams)
    #print(20-num_teams)
    print(scoringTable)

    tally = [results.Place, results.School]
    results2 = pandas.concat(tally, axis = 1)

    #results['scoring'] = scoringTable

    #results2.assign(Score=scoringTable)

    # print(results2)
    #print(results.School)
    

    
   

    #print(num_teams)

    #print(scoringTable)
    
    

   
    #regattaType.append(links.type[i])
    


    #print(regattaType)


    #print(results2)

    """results_final = results.set_index('Unnamed: 1')

    results_school = results.School
    print(results_school)
    print(results_final)"""

    #print(results)
    
#print(regattaType)
# for i in links.B:
#     table = pandas.read_html('links.B[i]', header=0, index_col=0)
#     print(table)





### End Evaluate Link Data







#link = input('Regatta Results Link = ')

#table = pandas.read_html(link, header=0, index_col=0)


"""table = pandas.read_html('https://scores.collegesailing.org/f18/victorian-urn/', header=0, index_col=0)


table2 = table[0] 
table2.columns = ['Position', 'Flag', print(results.B)
    print(link) 
                  'School', 'Team', 'A', 'Pa', 
                  'B', 'Pb', 'Total']

table3 = table2.set_index('Unnamed: 1')

'''if event = 'A'
    column=1

    for i in range(0, 34)'''

#print(table3)

#print(table3.shape)

#print(table3.School)

c = len(table3.School)
#print(c)



#scoring = pandas.ExcelFile('/home/thomas/Documents/Code/Sailing_Techscore/Rank_Values.xls')

score = pandas.read_excel(
    'Rank_Values.xlsx', event)

#score.columns = ['Place1', 'Score1', 'Na', 'Place2', 'Score2']

# print(score.Place)
# print(score.Place)

##print(list(score))
print(score)

teams=pandas.read_html('https://docs.google.com/spreadsheets/d/1oDTZazH5M4ErQVKs3YtdrKEDRSgwDWMY_AM40SSpmjY/edit', header=0, index_col=0)
#print(teams)"""

