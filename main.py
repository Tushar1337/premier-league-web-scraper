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
print(clubs)
count=1
for y in clubs:
    print(count,':',y)
    count+=1
list_link=list(clubs.values())
a=int(input("Choose the corresponding number of the team you want to get stats of:"))
stats_url=list_link[a-1]
print(stats_url)
'''
m=requests.get(stats_url)
ac=BeautifulSoup(m.text,features="html.parser")
match_url="https://www.premierleague.com/match/59146"
n=requests.get(match_url)
bc=BeautifulSoup(n.text,features="html.parser")
print(bc)'''