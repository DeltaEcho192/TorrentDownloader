import time
from bs4 import BeautifulSoup
from selenium import webdriver
import difflib

#Created By DeltaEcho
#TODO If an episode is not found print a remark and continue to the next one
#TODO Build a basic GUI for user interface
#TODO Run the browser but headless

def epListMaker():
    SeriesName = input("PLease input shows Name: ")
    season = int(input("Please enter the Season: "))
    firstEp = int(input("Please enter first episodes number: "))
    lastEP = int(input("Please enter last episode: "))

    # SeriesName+S0+Season+E0+Episode... Format of string

    i = 1
    epNum = firstEp
    listEP = []
    epNumL = []
    while i < lastEP - firstEp + 2:

        if season < 10:
            seasonName = SeriesName + " S0" + str(season)
        else:
            seasonName = SeriesName + " S" + str(season)

        if epNum < 10:
            finalName = seasonName + "E0" + str(epNum)
            print(finalName)
            listEP.append(finalName)
        else:
            finalName = seasonName + "E" + str(epNum)
            print(finalName)
            listEP.append(finalName)
        i = i + 1
        epNumL.append(epNum)
        epNum = epNum + 1
    return listEP,season,epNumL
    print(listEP)



def seedSorter(seedersC):
    c = 0
    seedCount = []
    while c < len(seedersC):
        seedCount.append(int(seedersC[c].text))
        c = c + 1
    slctSeed = max(seedCount)
    posSeed = seedCount.index(slctSeed)
    return posSeed


x = 0
ep = []
listEP,season,ep = epListMaker()
while x < len(listEP):
    name = listEP[x]
    i = 0
    driver = webdriver.Chrome()
    driver.get("https://1337x.to")

    driver.find_element_by_id("autocomplete").send_keys(name)
    driver.find_element_by_xpath('//*[@id="search-index-form"]/button').click()

    content = driver.page_source
    soup = BeautifulSoup(content,'html.parser')
    seedersC = soup.find_all("td",{'class',"coll-2 seeds"})
    fnlPosSeed = seedSorter(seedersC)
    print(fnlPosSeed)
    #To Open link of a torrent.
    firstC = soup.find_all("td",{'class',"coll-1 name"})
    name1 = firstC[fnlPosSeed].find_all("a")
    nameProp = name1[1].text
    similarity = difflib.SequenceMatcher(None, name, nameProp).ratio()
    if nameProp.find(season) == -1 | nameProp.find(ep[x]) == -1:
        print("Episode or Season did not match torrent.")
        break
    if similarity < 0.5:
        #TODO Cut of end of torrent name to make it easier to guage without all the facts added.
        print("Similarity of torrent names was to low and most likely not the correct episode.")
        break

    link = name1[1].get("href")

    fullLink = "https://www.1337x.to" + link
    driver.get(fullLink)
    pageContent = driver.page_source
    soup2 = BeautifulSoup(pageContent,'html.parser')

    torrentLink = soup2.find_all("ul",{'class',"dropdown-menu"})
    torrentHref = torrentLink[0].find("a")
    finalLink = torrentHref.get('href')
    print(finalLink)
    driver.get(finalLink)
    time.sleep(15)
    driver.close()
    x = x + 1
