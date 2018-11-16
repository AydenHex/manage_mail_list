import csv
import os
import requests
import re
import urllib
from bs4 import BeautifulSoup



def getDomain(myMail):
    return re.split(r'@', myMail)[1]

def pingDomain(myDomain):
    response = os.system("ping -c 1 " + myDomain)
    return True if response == 0 else False

print(pingDomain("google.fr"))

def testDomain(myDomain):
    codeResult = str(urllib.request.urlopen("http://" + myDomain).getcode())
    return(codeResult)


def deleteDuplicate(myList):
    return list(set(myList))

def checkMail(myMail):
    return re.match(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', myMail)

def crawlForMail(myUrl):
    plainPage = requests.get(myUrl).text
    beautifulPage = str(BeautifulSoup(plainPage, "html.parser"))
    result = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', beautifulPage)
    return list(set(result))


def readCsv(myFile):
    if os.path.isfile(myFile):
        listResult = list()
        with open(myFile, 'r') as myCsv:
            spamreader = csv.reader(myCsv, delimiter=',', quotechar='|')
            for row in spamreader:
                listResult.append(row)
        return listResult
    return 'No file found'

def writeCsv(myFile, myList):
    with open(myFile, 'w+') as myCsv:
        spamwriter = csv.writer(myCsv, delimiter=' ', quotechar='|')
        print(myList)
        for item in myList:
            spamwriter.writerow([item])
    
