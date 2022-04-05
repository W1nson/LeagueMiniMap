import json
import requests
from bs4 import BeautifulSoup

import time
import os
from selenium import webdriver
from selenium.webdriver import chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains


def getChampionWinRate(name):
    result = requests.get(f'https://app.mobalytics.gg/lol/champions/{name}/counters')
    print("the type of result = ", type(result))
    soup = BeautifulSoup(result.content, 'html.parser')
    #print(1, soup)
    divTag = soup.find_all("div", {"class":"m-89mhyo"})
    print(2, divTag, '\n')
    tbodyTag = divTag[0].find_all("tbody", {"class":"m-wsbm9"})
    print(3, tbodyTag, '\n')
    trTag = tbodyTag[0].find_all("tr", {"class":"m-1pkzzoz"})
    print(4, trTag, '\n')
    tdTag = trTag[1].find_all("td", {"class":"m-m7fsih"})
    print(5, tdTag, '\n')
    print(6, tdTag[0].getText(), '\n')
    return tdTag[0].getText()



def getChampionCounters(name):
    champ_list_driver = webdriver.Chrome()
    champ_list_driver.get("https://u.gg/lol/champions")

    html = champ_list_driver.page_source
    heros_soup = BeautifulSoup(html, "html.parser")

    divTag = heros_soup.find_all("a", {"class": "champion-link"})
    heros = []

    for i in divTag:

        heros.append(i.find("div", {"class": "champion-name"}).string)
        # print( i.find("div", {"class": "champion-name"}).string )
    # print(len(heros))
    datas = []

    for i in range (159):
        temp = []
        for j in range(159):
            temp.append(-1)
        datas.append(temp)

    champ_list_driver.quit()


    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.get(f'https://u.gg/lol/champions/{name}/counter')

    search = driver.find_element(by = By.ID, value =  "content")
    a = search.find_element(by = By.XPATH, value = '//*[@id="content"]/div/div[1]/div/div/div[5]/div/div[3]/div')
    a = driver.switch_to.active_element
    # print(a.get_attribute('innerHTML'))
    while(1):
        time.sleep(1)#2
        # a.click()
        ActionChains(driver).move_to_element(a).click(a).perform()
        time.sleep(1)#3
        try:
            main = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div/div/div[5]/div[2]/div[3]/div'))
            )
            a = search.find_element(by = By.XPATH, value = '//*[@id="content"]/div/div/div/div/div[5]/div[2]/div[3]/div')
        except:
            break

    time.sleep(1) #5

    print(driver.title)
    html = driver.page_source
    # time.sleep(2)
    # print(html)

    soup = BeautifulSoup(html, "html.parser")

    divTag = soup.find_all("a", {"class": "counter-list-card best-win-rate"})
    for i in divTag:
        hero_name = i.find("div", {"class": "champion-name"}).string
        winrate = i.find("div", {"class" : "win-rate"}).string[:-3]
        print(heros.index(hero_name), hero_name, winrate)
        datas[heros.index('Zeri')][heros.index(hero_name)] = winrate
    driver.quit()

    print(datas[heros.index('Zeri')])
    #driver.implicitly_wait(15)
    #frame = driver.find_element_by_css_selector('div.tool_forms iframe')
    #iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")
    #driver.switch_to.frame(iframe)
    # driver.implicitly_wait(220)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # a = driver.find_element(By.NAME,"s")
    # a.send_keys("tests")
    # a.send_keys(Keys.RETURN)

    # try:
    #     # element = WebDriverWait(driver, 5).until(
    #     #     EC.presence_of_element_located((By.NAME, "view-more-btn btn-gray"))
    #     # )
    #     driver.find_element(by=By.XPATH, value = '//*[@id="content"]/div/div/div/div/div[5]/div/div[3]/div').click()
    #     # element = WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.NAME,"view-more-btn btn-gray")))
    #     # element.click()
    # except:
    #     print("cant find more bottom")

    # element = driver.find_elements(By.CLASS_NAME,'counters-list best-win-rate') #counter-list-card best-win-rate
    # print("element ", element)
    # for i in element:
    #     print( i.find_element(By.CLASS_NAME,'champion-name') )
    #     print( i.find_element(By.CLASS_NAME,'win-rate') )





    # counters = dict()
    # result = requests.get(f'https://u.gg/lol/champions/{name}/counter')
    # soup = BeautifulSoup(result.content, 'html.parser')
    # divTag = soup.find_all("a", {"class": "counter-list-card best-win-rate"})
    # for i in divTag:
    #     print(i.find("div", {"class": "champion-name"}).string)
    #     print(i.find("div", {"class" : "win-rate"}).string[:-3] )



    # counters = dict()
    # result = requests.get(f'https://u.gg/lol/champions/{name}/counter')
    # soup = BeautifulSoup(result.content, "html.parser")
    # divTag = soup.find("div", {"class":"counters-list best-win-rate"})
    # champName = divTag.find_all("div", {"class": "champion-name"})
    # winrate = divTag.find_all("div", {"class": "win-rate"})
    # print(champName)
    # print(winrate)
    # # print("len of divTag = ", len(divTag))
    # for i in range (len(champName)):
    #     name = champName[i].getText()
    #     print(name)
    #     wr = winrate[i].getText()[:-3]
    #     counters[name] = wr
    # return counters

print(getChampionCounters("zeri"))
# print(getChampionWinRate("zeri"))


# import webdriver


# import Action chains
# from selenium.webdriver.common.action_chains import ActionChains
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get("https://www.python.org")
# print(driver.title)
# search_bar = driver.find_element(by=By.NAME, value="q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)
# driver.close()
