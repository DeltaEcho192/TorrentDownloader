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

print(listEP)


# Check first episode first character
# Check last episode first Character
# Loop to get all versions of name that is needed

