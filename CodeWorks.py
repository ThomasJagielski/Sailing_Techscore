from pandas import *
import numpy as np
import math

engine='python'

teamsSheet=pandas.read_csv('https://docs.google.com/spreadsheets/d/1oDTZazH5M4ErQVKs3YtdrKEDRSgwDWMY_AM40SSpmjY/export?format=csv&gid=0', header=0, index_col=0)
linksSheet= pandas.read_html('https://docs.google.com/spreadsheets/d/1FG4fDoh5nt_hqBfj6m8Ndt0qsKWJYDmauJHY5tUu1HQ/edit#gid=0', header=0, index_col=0)

teams = teamsSheet
teams.columns = [ 'School', 'Conference', 'Code','Membership', 'Club_or_Var', 'Team_Email', 'Contact', 'Email']
links=linksSheet[0]
links.columns = ['regatta', 'link', 'type']
num_regatta = len(links.link)

teams.School = teams.index
teams.index=pandas.RangeIndex(len(teams.index))

tally3 = [teams.School, teams.Conference]
allTeams = pandas.concat(tally3, axis = 1)


scoringfile = pandas.ExcelFile('Rank_Values2.xlsx')
scoringTable_sc = pandas.read_excel(scoringfile, 'SC')
scoringTable_sc_alt = pandas.read_excel(scoringfile, 'SC_alt')
scoringTable_coed_a = pandas.read_excel(scoringfile, "Coed A")
scoringTable_coed_b = pandas.read_excel(scoringfile, 'Coed B')
scoringTable_coed_c = pandas.read_excel(scoringfile, 'Coed C')
scoringTable_w_sc = pandas.read_excel(scoringfile, 'W SC')
scoringTable_w_a = pandas.read_excel(scoringfile, "Women's A")
scoringTable_w_b = pandas.read_excel(scoringfile, "Women's B")


bigList = DataFrame()

for i in range(2, num_regatta+1):
   
    link = links.link[i]
    #print(link)
    resultsTable = pandas.read_html(link, header=0, index_col=0)       
    results = resultsTable[0]
    #print(results)
    

    results.columns = [c.replace('Unnamed: 1', 'Place') for c in results.columns]

    num_teams = len(results.Place)

    scoringSheet = pandas.read_excel(scoringfile, links.type[i])
    scoringTable = scoringSheet[scoringSheet.columns[(20-num_teams)]]
    scoringTable.dropna(inplace=True)
    scoringTable.index=pandas.RangeIndex(len( scoringTable.index))
    scoringTable.columns = ['points'] 
    results.index=pandas.RangeIndex(len(results.index))
    
  
    tally = [results.Place, results.School,results.Team, scoringTable]
    results2 = pandas.concat(tally, axis = 1)

    results2.columns = ['Place', 'School', 'Team', 'Points']
    
    

    x = np.where(results2['Team'].str.contains('2')|results2['Team'].str.contains('3'))
    
    j=0

    while j < len(x):
        y = x[j]
        results2.at[y, 'Points'] = 0
        j += 1
    
        # print(results2)
    
    bigList = bigList.append(results2)



bigList=bigList.sort_values(['School', 'Points'], ascending = [1, 0], )

bigListLength = len(bigList)

bigList.index=pandas.RangeIndex(len(bigList.index))
# finalList = {}
finalList=pandas.DataFrame(columns=['School','Score'])
j=0
k=0
for i in range(0,bigListLength):
    if (i==0):
        currentRank=pandas.DataFrame({'School':[bigList.School[0]],'Score':[bigList.Points[0]]},index=[0])
        j=1
    else:
        if i==bigListLength-1:
            finalList= pandas.concat([finalList,currentRank])
        else:
            if (bigList.School[i]!=bigList.School[i-1]):
                finalList= pandas.concat([finalList,currentRank])
                j+=1
        
                currentRank=pandas.DataFrame({'School':[bigList.School[i]],'Score':[bigList.Points[i]]},index=[j])
            else: 
                if i<=5:
                    currentRank.Score=currentRank.Score+bigList.Points[i]
                else:
                    if bigList.School[i]==bigList.School[i-5]:
                        'none'
                    else:
                        currentRank.Score= currentRank.Score+bigList.Points[i]


#print(finalList)
z = np.where(allTeams['Conference'].str.contains('NEISA'))[0]

teamsNEISA = []
j=0

while j < len(z):
    y = z[j]
    teamsNEISA.append(teams.School[y])
    j += 1

teamsNEISA = pandas.Series(np.array(teamsNEISA))
#print(teamsNEISA)


for i in finalList.index:

    # if teamsNEISA.School.str.contains(finalList.School[i]).any():
    if not teamsNEISA.str.match(finalList.School[i]).any():
        #print('True')
        finalList.Score[i]=np.nan
finalList.replace(["NaN", 'NaT'], np.nan, inplace = True)
finalList=finalList.dropna()

finalList=finalList.sort_values(['Score'], ascending = [0], )
finalList.index=pandas.RangeIndex(start=1,stop=len(finalList.index)+1)
print(finalList)