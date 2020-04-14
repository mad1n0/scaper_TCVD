# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:04:41 2020

@author: Marc
"""


from bs4 import BeautifulSoup
import requests

url = "https://www.hltv.org/betting/money"
request = requests.get(url).content


soup = BeautifulSoup(request)

linklist = []

length = len('/betting/analytics/')

for link in soup.find_all('a'):
    stringy = link.get('href').__str__()
    #print(stringy[:19])
    if(stringy[:19] == ('/betting/analytics/')):
        
        stringey = stringy [19:]
        
        stringey2 = stringey.split('/')[0]

        linklist.append(stringey2)

        
print(linklist)



    

def getidlist():
    return(linklist[:len(linklist)//2])    
#print(team_list)