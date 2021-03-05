from bs4 import BeautifulSoup
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
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
for i in range (len(stats)):
    cur_stats=stats[i]
    # p=session.get(cur_stats)
    # cr = BeautifulSoup(p.text, features="html.parser")
    # stat_num=cr.find_all('section',{"class":"stat-group stat-box rw100 lh14e ft-data"})
    # num_pos=stat_num[i].find_all("td", string="Possession")
    # print(num_pos)
    # print(cur_stats, stat_num)