import time
from bs4 import BeautifulSoup
from selenium import webdriver

#Created By DeltaEcho
#TODO If an episode is not found print a remark and continue to the next one


def epListMaker():
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

listEP = epListMaker()

x = 0
while x < len(listEP):
    name = listEP[x].replace('.',' ')
    i = 0
    driver = webdriver.Chrome()
    driver.get("https://1337x.to")

    driver.find_element_by_id("autocomplete").send_keys(name)
    driver.find_element_by_xpath('//*[@id="search-index-form"]/button').click()

    content = driver.page_source
    soup = BeautifulSoup(content,'html.parser')

    firstC = soup.find_all("td",{'class',"coll-1 name"})
    while i < len(firstC):
        name1 = firstC[i].find_all("a")
        if str(name) == str(name1[1].text):
            link = name1[1].get('href')

        i = i + 1

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
