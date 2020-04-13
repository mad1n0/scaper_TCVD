# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:08:51 2020

@author: Marc
"""


from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://www.hltv.org/stats/teams?startDate=all&matchType=Online&minMapCount=0"
request = requests.get(url).content

soup = BeautifulSoup(request)
main_table = soup.find('table', attrs={'class': 'stats-table player-ratings-table'})
rows = main_table.find_all('tr')
team_list = {}


def substring_after(s, delim):
    return s.partition(delim)[2]


for a in main_table.find_all('a', href=True):
    link = a['href']
    team_id = substring_after(link, 'teams/')
    team_id = team_id[0:4]
    team_name = substring_after(link, team_id + '/')
    team_name = team_name.split('?')[0]
    team_name = team_name
    #team_id = int(team_id)
    team_list[team_id] = team_name.replace('%20'," ")
    
    

#data = {'team_id': team_list.keys(), 'team_name': team_list[team_list.keys()]}
#print(data)
#dfdata=pd.DataFrame(data)
#print(dfdata)
IDdf = pd.DataFrame.from_dict(team_list, orient= 'index', columns = ['name'])
print(IDdf)