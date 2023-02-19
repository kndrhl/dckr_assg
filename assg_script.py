import os
import socket
from collections import Counter

Counter = Counter()

def getIP():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return IPAddr

def numOfWords(file):
    count = 0
    with open(file, 'r') as file:
        for line in file:
            if (line != '\n'):
                if (file.name.endswith("IF.txt")):
                    Counter.update(line.replace("Â", "").split())
                count = count + len(line.replace("Â", "").split())
    return count

fileWordCount = {}
path ="/home/data"
if os.path.exists(path + "/" +"result.txt"):
  os.remove(path + "/" +"result.txt")
outputString="Text file is at location: /home/data \n"
for eachFile in os.listdir(path):
    if eachFile.endswith(".txt"):
        outputString=outputString+eachFile+"\n"
        fileWordCount[eachFile] = numOfWords(path + "/" + eachFile)
		
outputString=outputString+"\n"
totalWords = 0
fileName = ""
for eachkey in fileWordCount.keys():
    fileName = fileName + eachkey + ","
    totalWords = totalWords + fileWordCount.get(eachkey)
    outputString = outputString +"Total number of words in " + eachkey + " is : " + str(fileWordCount.get(eachkey))+"\n"

outputString = outputString +"Total words in both files " + fileName[0:len(fileName) - 1] + " is: " + str(totalWords)+"\n"

outputString = outputString +"\n"
outputString = outputString +"Top 3 words in IF.txt\n"
outputString = outputString +str(Counter.most_common(3))+"\n"

outputString = outputString +"\n"
outputString = outputString +"IP Address:" + getIP()

resultsTextFile = open(path + "/" +"result.txt","w")
resultsTextFile.write(outputString)
resultsTextFile.close()
for eachline in open(path + "/" +"result.txt","r").readlines():
    print(eachline.replace("\n",""))
