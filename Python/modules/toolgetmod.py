import re

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
