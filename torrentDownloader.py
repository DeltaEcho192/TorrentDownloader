import sys
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import difflib
import tkinter as tk
from selenium.webdriver.chrome.options import Options

#Created By DeltaEcho
#TODO If an episode is not found print a remark and continue to the next one

#Function Takes input from GUI and makes sure all variables are valid for program
def check():
    #Use of Global variable because of Tkinter limitations on returning
    global nameG,seasonG,sEpG,eEpG
    try:
        nameG = str(nameE.get())
        seasonG = int(seasonE.get())
        sEpG = int(sEpE.get())
        eEpG = int(eEpE.get())
        if sEpG > eEpG:
            raise Exception("Starting episode number cant be greater then last episode")
        if sEpG < 1 or eEpG < 1:
            raise Exception("Cant have a episode less then 1")
    except ValueError:
        error = tk.Toplevel()
        errorL = tk.Label(error,text="A character has been entered instead of number.")
        errorL.pack()
        error.mainloop()
    except Exception as a:
        error = tk.Toplevel()
        errorL = tk.Label(error, text=a)
        errorL.pack()
        error.mainloop()

    window.destroy()

#GUI Code
window = tk.Tk()
window.geometry("300x200")
name = tk.Label(text="Enter Show name:")
nameE = tk.Entry(width=40)
season = tk.Label(text="Enter Season:")
seasonE = tk.Entry(width=20)
sEp = tk.Label(text="Enter Start Episode:")
sEpE = tk.Entry(width=20)
eEp = tk.Label(text="Enter End Episode:")
eEpE = tk.Entry(width=20)
button = tk.Button(text="Run",command=check)
name.pack()
nameE.pack()
season.pack()
seasonE.pack()
sEp.pack()
sEpE.pack()
eEp.pack()
eEpE.pack()
button.pack()

window.mainloop()

#Functions uses the given inputs to create Array of the searchable episode names.
def epListMaker():
    SeriesName = nameG
    season = seasonG
    firstEp = sEpG
    lastEP = eEpG

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


#Takes the list of amount of seeds and finds the position of the torrent with the most seeds
#Usually 1st one because default is to sort my seeds. More for redunecy
def seedSorter(seedersC):
    c = 0
    seedCount = []
    while c < len(seedersC):
        seedCount.append(int(seedersC[c].text))
        c = c + 1
    slctSeed = max(seedCount)
    posSeed = seedCount.index(slctSeed)
    return posSeed

#Function to do actual download of torrent as this cant be done in headless mode.
def torrentOpener(link):
    driverOpen = webdriver.Chrome()
    driverOpen.get(link)
    #Allows for cloudflare to proccess request and download
    time.sleep(10)
    driverOpen.close()

x = 0
ep = []
listEP,season,ep = epListMaker()

#Option to make the browser to run in headless mode
options = Options()
options.headless = True

while x < len(listEP):
    name = listEP[x]
    i = 0
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://1337x.to")

    #Completes search field and clicks button
    driver.find_element_by_id("autocomplete").send_keys(name)
    driver.find_element_by_xpath('//*[@id="search-index-form"]/button').click()

    content = driver.page_source
    soup = BeautifulSoup(content,'html.parser')
    #Collects all the seed numbers for the torrents
    seedersC = soup.find_all("td",{'class',"coll-2 seeds"})
    fnlPosSeed = seedSorter(seedersC)
    #To Open link of a torrent.
    firstC = soup.find_all("td",{'class',"coll-1 name"})
    #Uses the seed pos to find the name and link values for torrent.
    name1 = firstC[fnlPosSeed].find_all("a")
    nameProp = name1[1].text
    #Uses similarity to make sure that the torrent name and user input is mostly similar.
    similarity = difflib.SequenceMatcher(None, name, nameProp).ratio()
    #Sudo makes sure torrent has the season number and episode number in the name.
    if nameProp.find(str(season)) == -1 | nameProp.find(str(ep[x])) == -1:
        print("Episode or Season did not match torrent.")
        break
    if similarity < 0.5:
        #TODO Cut of end of torrent name to make it easier to guage without all the facts added.
        print("Similarity of torrent names was to low and most likely not the correct episode.")
        break

    link = name1[1].get("href")

    fullLink = "https://www.1337x.to" + link
    driver.get(fullLink)
    #Opens torrent page
    pageContent = driver.page_source
    soup2 = BeautifulSoup(pageContent,'html.parser')
    #Finds the link of the torrent in the dropdown menu of the website.
    torrentLink = soup2.find_all("ul",{'class',"dropdown-menu"})
    torrentHref = torrentLink[0].find("a")
    finalLink = torrentHref.get('href')
    #Does actual download of file
    torrentOpener(finalLink)
    driver.close()
    x = x + 1
