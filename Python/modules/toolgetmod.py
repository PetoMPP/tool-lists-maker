import re

#Przechwycenie nr T (Działa)
def findTnums(line):
    TNumRegex = re.compile(r'T\d+')
    hits = TNumRegex.findall(line)
    return hits

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

#Stworzenie listy numerów T z ogranicznikiem czytanych wierszy
def fileTlistLimited(path, limit):
    ncprg = open(path)
    tlist = []
    i = 0
    for line in ncprg.readlines():
        while i < limit:
            tlist.extend(findTnums(line))
            i += 1
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
