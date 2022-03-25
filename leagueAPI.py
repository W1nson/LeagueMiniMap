import json 
import requests
from bs4 import BeautifulSoup


def getChampionWinRate(name):
    result = requests.get(f'https://app.mobalytics.gg/lol/champions/{name}/counters')
    soup = BeautifulSoup(result.content, 'html.parser')
    divTag = soup.find_all("div", {"class":"m-89mhyo"})
    tbodyTag = divTag[0].find_all("tbody", {"class":"m-wsbm9"})
    trTag = tbodyTag[0].find_all("tr", {"class":"m-1pkzzoz"})
    tdTag = trTag[1].find_all("td", {"class":"m-m7fsih"})
    return tdTag[0].getText()



def getChampionCounters(name):
    counters = dict()
    result = requests.get(f'https://app.mobalytics.gg/lol/champions/{name}/counters')
    soup = BeautifulSoup(result.content, "html.parser")
    divTag = soup.find_all("div", {"class":"m-1p8lnhy"})
    for i in divTag:
        counter_name = i.find_all("div",{"class":"m-1j4udfm"})[0].getText()
        counter_wr = i.find_all("div", {"class":"m-oft0zz"})[0].getText()
        counters[counter_name] = counter_wr
    return counters

print(getChampionCounters("zeri"))
print(getChampionWinRate("zeri"))

