# Torrent Download

## General
This program uses a webscrapper to automatically access torrents and collect relevent files to bulk download a show.
It requires the user to enter:
- Show name
- Season
- Starting Episode
- Ending Episode

It uses this information to then use the website 1337x.to to search and find the episode with the highest amount of seeders
It then downloads the torrent file and continues until all episodes are downloaded.

## Requirements
Python
Beautiful Soup 4
Selenium Python
ChromeDriver

## Instalation
    * Download Python package from python website and follow instructions or on OSX/Linux `sudo apt-get install python`
    * Then clone git project
    * Go into directory and run the command `pip install -r requiremnets.txt`
    * Then just use `python torrentDownloader.py`
    * If you experiance a ChromeDriver error follow instructions in Extra

## Extras
Selenium browser does not run in docker

#### Chrome Driver Error
If you run the program and you recive an error regarding the chrome driver you have to:
* Find out the version of your chrome browser using Help > About Chrome
* Go to https://chromedriver.chromium.org/ and download the corasponding driver
* Place the driver in the working directory of the project.
