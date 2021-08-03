import re

#Przechwycenie nr T (Działa)
def findTnums(line):
    TNumRegex = re.compile(r'T\d+')
    hits = TNumRegex.findall(line)
    return hits

#Stworzenie listy narzędzi z pliku (Działa)
def makeTlist(NCP):
    ncprg = open("../ToolLists/NC_Programs/"+NCP)
    tlist = []
    for line in ncprg.readlines():
        tlist.extend(findTnums(line))
    return tlist