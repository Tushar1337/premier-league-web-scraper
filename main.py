from bs4 import BeautifulSoup
from requests_html import HTMLSession
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from time import sleep
# from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
home_url = "https://footystats.org"
clubs_url = "https://footystats.org/england/premier-league"
session = HTMLSession()
r = session.get(clubs_url)
wc = BeautifulSoup(r.text, features="html.parser")
team_name = wc.find_all('td', {"class": "team borderRightContent"})
team_page = wc.find_all('td', {"class": "team borderRightContent"})
link = []
team = []
clubs = {}
stats = []


def dis_team():
    for i in team_page:
        link.append(i.a)
    for i in team_name:
        team.append(i.text)
    for i in range(len(team_name)):
        clubs[team[i]] = home_url+link[i]['href']
    sorted(clubs)
    count = 1
    for y in clubs:
        print(count, ':', y)
        count += 1


dis_team()
a = int(input("Choose the corresponding number of the team you want to get stats of:"))
club_name_clean = list(clubs.keys())[a-1]
club_name_clean = club_name_clean.replace(" FC", "")


def team_stats():
    list_link = list(clubs.values())
    stats_url = list_link[a-1]
    print(stats_url)
    m = session.get(stats_url)
    ac = BeautifulSoup(m.text, features="html.parser")
    result = ac.select('div.scoreline')
    result1 = []
    for i in result:
        result1.append(i.a)

    for i in range(11, 16):
        if i >= 5:
            stats.append(home_url+result1[i]['href'])
    print(stats)


team_stats()
possession = []
shots = []
corners = []
offside = []
fouls = []
opp_team = []


def ask():
    count = 1
    print(count, "Possession")
    count += 1
    print(count, "Shots")
    count += 1
    print(count, "Corners")
    count += 1
    print(count, "Offsides")
    count += 1
    print(count, "Fowls")
    count += 1
    print("Exit?")
    ask.v = int(input("Which stats would you like to see?"))


def data_pos():
    pos = (list(data_table.stats_tab.iloc[0]))
    for j in pos:
        j = j.replace("%", "")
        j = int(j)
        possession.append(j)
    print(possession)


def data_fouls():
    fouls_list = (list(data_table.stats_tab.iloc[6]))
    for j in fouls_list:
        j = int(j)
        fouls.append(j)


def data_table():
    v = 0
    for i in range(len(stats)):
        cur_stats = stats[i]
        tab_num = pd.read_html(cur_stats)
        tab_num = tab_num[0]
        data_table.tab_num = tab_num
        print(tab_num)
        data_table.stats_tab = tab_num[[club_name_clean]]

        if i == 0:
            ask()
        if ask.v == 1:
            data_pos()

        elif ask.v == 2:
            data_shots()
        elif ask.v == 3:
            data_corners()
        elif ask.v == 4:
            data_offsides()
        elif ask.v == 5:
            data_fouls()
        elif ask.v == 6:
            break
        opp = list(data_table.tab_num.columns.values)
        for j in opp:
            if j != club_name_clean:
                if j != "Data":
                    opp_team.append(j)
        print(data_table.stats_tab)
    print(possession)
    print(shots)
    print(corners)
    print(opp_team)


data_table()


def data_shots():
    shots_list = (list(data_table.stats_tab.iloc[1]))
    for j in shots_list:
        j = int(j)
        shots.append(j)


data_shots()


def data_corners():
    corners_list = (list(data_table.stats_tab.iloc[3]))
    for j in corners_list:
        j = int(j)
        corners.append(j)


data_corners()


def data_offsides():
    offsides_list = (list(data_table.stats_tab.iloc[5]))
    for j in offsides_list:
        j = int(j)
        offside.append(j)


data_offsides()


def plot_data():
    if ask.v == 1:
        plt.plot(opp_team, possession)

    if ask.v == 2:
        plt.plot(opp_team, shots)

    if ask.v == 3:
        plt.plot(opp_team, corners)

    if ask.v == 4:
        plt.plot(opp_team, offside)

    if ask.v == 5:
        plt.plot(opp_team, fouls)
    plt.show()
    data_table()


plot_data()
