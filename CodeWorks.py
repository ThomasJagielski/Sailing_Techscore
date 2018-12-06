from pandas import *
import numpy as np
import math

engine='python'

teams=pandas.read_html('https://docs.google.com/spreadsheets/d/1oDTZazH5M4ErQVKs3YtdrKEDRSgwDWMY_AM40SSpmjY/edit', header=0, index_col=0)
linksSheet= pandas.read_html('https://docs.google.com/spreadsheets/d/1FG4fDoh5nt_hqBfj6m8Ndt0qsKWJYDmauJHY5tUu1HQ/edit#gid=0', header=0, index_col=0)

links=linksSheet[0]
links.columns = ['regatta', 'link', 'type']
num_regatta = len(links.link)


scoringfile = pandas.ExcelFile('Rank_Values2.xlsx')
scoringTable_sc = pandas.read_excel(scoringfile, 'SC')
scoringTable_sc_alt = pandas.read_excel(scoringfile, 'SC_alt')
scoringTable_coed_a = pandas.read_excel(scoringfile, "Coed A")
scoringTable_coed_b = pandas.read_excel(scoringfile, 'Coed B')
scoringTable_coed_c = pandas.read_excel(scoringfile, 'Coed C')
scoringTable_w_sc = pandas.read_excel(scoringfile, 'W SC')
scoringTable_w_a = pandas.read_excel(scoringfile, "Women's A")
scoringTable_w_b = pandas.read_excel(scoringfile, "Women's B")



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
    scoringTable.index=pandas.RangeIndex(len( scoringTable.index))
    scoringTable.columns = ['points'] 
    results.index = pandas.RangeIndex(len(results.index))
    
    #print(links.type[i], num_teams)
    #print(results.index)
    #print(scoringTable.index)
    tally = [results.Place, results.School,scoringTable]

    #tally = [results.Place, results.School, scoringTable]
    results2 = pandas.concat(tally, axis = 1)
    results_final = results2.set_index('Place')

    print(results_final)
    #else:
     #   tally = [results.Place, results.School]
    
    

    #print(links.type[i])
    #print(num_teams)
    #print(results2)
    # #print(scoringTable)