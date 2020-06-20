import time
from bs4 import BeautifulSoup
from selenium import webdriver
import difflib

#Created By DeltaEcho
#TODO If an episode is not found print a remark and continue to the next one
#TODO Build a basic GUI for user interface
#TODO Check that file with Highest seaders has correct episode number in and Correct name


def epListMaker():
    # TODO Adjust episode namer
    #TODO Remember to add season and episode for checking.
    firstEp = int(input("Please enter first episodes number: "))
    lastEP = int(input("Please enter last episode: "))
    SeriesName = input("PLease input shows Name: ")
    i = 1
    epNum = firstEp
    listEP = []
    while i < lastEP - firstEp + 2:
        workingVar = SeriesName.split("E0")
        episodeVar = workingVar[1]
        episodeVar = episodeVar[1:]
        episodeVar = episodeVar.split("[")
        episodeVar = episodeVar[0] + " [" + episodeVar[1]
        if epNum < 10:
            finalName = workingVar[0] + "E0" + str(epNum) + episodeVar
            print(finalName)
            listEP.append(finalName)
        else:
            finalName = workingVar[0] + "E" + str(epNum) + episodeVar
            print(finalName)
            listEP.append(finalName)
        i = i + 1
        epNum = epNum + 1
    return listEP
    print(listEP)

#listEP = epListMaker()
listEP = ["test"]

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
while x < len(listEP):
    #name = listEP[x].replace('.',' ')
    name = "The Blacklist S07E05"
    i = 0
    driver = webdriver.Chrome()
    driver.get("https://1337x.to")

    driver.find_element_by_id("autocomplete").send_keys(name)
    driver.find_element_by_xpath('//*[@id="search-index-form"]/button').click()

    #
    #
    #


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
    if nameProp.find(season) == -1 | nameProp.find(ep) == -1:
        print("Episode or Season did not match torrent.")
        break
    if similarity < 0.5:
        #TODO Cut of end of torrent name to make it easier to guage without all the facts added.
        print("Similarity of torrent names was to low and most likely not the correct episode.")
        break

    link = name1[1].get("href")

    #
    #
    #

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
    break
    x = x + 1
