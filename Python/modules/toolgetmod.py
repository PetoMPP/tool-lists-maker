import re
from typing import Pattern

#Przechwycenie nr T (Działa)
def findTnums(line):
    TNumRegex = re.compile(r'T\d+')
    hits = TNumRegex.findall(line)
    '''filters = ["r'T\d+'", "r'FZ\d+\D'", "r'W\d"]
    i = 0
    hits = []
    for filter in filters:
        TNumRegex = re.compile(filters[i])
        hits = hits + TNumRegex.findall(line)
        i += 1'''
    return hits

def findTnumsMPF(line):
    mpfPattern = re.compile(r'\D\w+')
    hits = mpfPattern.findall(line)
    return hits

def findTnumsFUSION(line):
    mpfPattern = re.compile(r'"ArticleNr":"\w+"')
    hit = mpfPattern.findall(line)
    return hit


def findNamesFUSION(line, comp):
    mpfPattern = re.compile(r'"Name":"\w+"')
    if re.search(comp, line, re.IGNORECASE) is not None:
        hit = comp + "    " + mpfPattern.findall(line)[0]
        return hit
    return False

def clearFUSION(element):
    toolPattern = re.compile(r'":"\w+')
    element = toolPattern.findall(element)
    element = element[0]
    element = re.sub('[^A-Za-z0-9\-]+', '', element)
    element = element.upper()
    return element

#Stworzenie listy narzędzi z pliku nazwa po pliku (Działa)
def fileTlist(path):
    ncprg = open(path)
    tlist = []
    for line in ncprg.readlines():
        tlist.extend(findTnums(line))
    tlist = set(tlist)
    tlist = list(tlist)
    tlist.sort()
    return tlist

#Stworzenie listy narzędzi FUSION
def fileTlistFUSION(path):
    ncprg = open(path)
    tlist = []
    for line in ncprg.readlines():
        tlist.extend(findTnumsFUSION(line))
    tlist = set(tlist)
    tlist = list(tlist)
    tlist.sort()
    return tlist

#Stworzenie listy numerów T z ogranicznikiem czytanych wierszy
def fileTlistLimited(path, limit):
    ncprg = open(path)
    tlist = []
    for i, line in zip(range(limit), ncprg.readlines()):
        tlist.extend(findTnumsMPF(line))
    tlist = set(tlist)
    tlist = list(tlist)
    tlist.sort()
    return tlist


#Stworzenie listy narzędzi z pliku nazwa po pliku (Nie działa)
def dirTlist(NCP,path):
    ncprg = open(path+NCP)
    tlist = []
    for line in ncprg.readlines():
        tlist.extend(findTnums(line))
    tlist = set(tlist)
    tlist = list(tlist)
    tlist.sort()
    return tlist

def getsuffix(str):
    pattern1 = re.compile(r'_\w+')
    str = pattern1.findall(str)
    try:
        str = str[0]
    except IndexError:
        result = "_000"
        return result
    result = ""
    for char in str:
        result = result + char
    return result
