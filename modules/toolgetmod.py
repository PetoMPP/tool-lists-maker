import re

#Przechwycenie nr T (Działa)
def findTnums(line):
    TNumRegex = re.compile(r'T\d+')
    hits = TNumRegex.findall(line)
    return hits

#Stworzenie listy narzędzi z pliku nazwa po pliku (Działa)
def fileTlist(NCP, path):
    ncprg = open(path+NCP)
    tlist = []
    for line in ncprg.readlines():
        tlist.extend(findTnums(line))
    set(tlist)
    return tlist

#Stworzenie listy narzędzi z pliku nazwa po pliku (Nie działa)
def dirTlist(NCP,path):
    ncprg = open(path+NCP)
    tlist = []
    for line in ncprg.readlines():
        tlist.extend(findTnums(line))
    set(tlist)
    return tlist
