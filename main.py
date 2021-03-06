from bs4 import BeautifulSoup
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
home_url="https://footystats.org"
clubs_url="https://footystats.org/england/premier-league"
session = HTMLSession()
r = session.get(clubs_url)
wc=BeautifulSoup(r.text,features="html.parser")
team_name=wc.find_all('td',{"class":"team borderRightContent"})
team_page=wc.find_all('td',{"class":"team borderRightContent"})
link=[]
for i in team_page:
    link.append(i.a)
team=[]
clubs={}
for i in team_name:
    team.append(i.text)
for i in range (len(team_name)):
    clubs[team[i]]=home_url+link[i]['href']
sorted(clubs)
count=1
for y in clubs:
    print(count,':',y)
    count+=1
list_link=list(clubs.values())
a=int(input("Choose the corresponding number of the team you want to get stats of:"))
stats_url=list_link[a-1]
print(stats_url)
m=session.get(stats_url)
ac=BeautifulSoup(m.text,features="html.parser")
result=ac.select('div.scoreline')
result1=[]
for i in result:
    result1.append(i.a)

stats=[]
for i in range(11,16):
    if i>=5:
        stats.append(home_url+result1[i]['href'])
print(stats)
possession=[]
shots=[]
corners=[]
offside=[]
fouls=[]
opp_team=[]
for i in range (len(stats)):
    cur_stats=stats[i]
    tab_num=pd.read_html(cur_stats)
    tab_num=tab_num[0]
    s=list(clubs.keys())[a-1]
    s=s.replace(" FC", "")
    print(tab_num)
    stats_tab=tab_num[[s]]
    pos=(list(stats_tab.iloc[0]))
    shots_list=(list(stats_tab.iloc[1]))
    corners_list=(list(stats_tab.iloc[3]))
    offsides_list=(list(stats_tab.iloc[5]))
    fouls_list=(list(stats_tab.iloc[6]))
    opp=list(tab_num.columns.values)
    for j in opp:
        if j!=s:
            if j!="Data":
                opp_team.append(j)


    for j in shots_list:
        j=int(j)
        shots.append(j)

    for j in corners_list:
        j = int(j)
        corners.append(j)

    for j in offsides_list:
        j = int(j)
        offside.append(j)

    for j in fouls_list:
        j = int(j)
        fouls.append(j)

    for j in pos:
        j=j.replace("%","")
        j=int(j)
        possession.append(j)
    print(possession)
    print(stats_tab)
print(possession)
print(shots)
print(corners)
print(opp_team)
plt.plot(opp_team,possession)
plt.figure()
plt.plot(opp_team,shots)
plt.figure()
plt.plot(opp_team,corners)
plt.figure()
plt.plot(opp_team,offside)
plt.figure()
plt.plot(opp_team,fouls)
plt.figure()
plt.show()