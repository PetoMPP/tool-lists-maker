import time
import re
from os import listdir, name, walk
from os.path import isfile, join
start_time = time.time()

#Pobranie listy folderów z programami
def getDir(path):
    dirlist = []
    for (dirpath, dirnames, filenames) in walk(path):
        dirlist.extend(dirnames)
    return dirlist

print(getDir("../ToolLists/NC_Programs"))

#Pobranie listy programów (Działa)
def getfiles(path):
    filelist = [file for file in listdir(path) if isfile(join(path,file))]
    return filelist

#Stworzenie pliku dla listy narzędzi (Działa)
def createlist(flist):
    i = 0
    while i < len(flist):
        listfile = open("ToolList"+flist[i]+".txt", "a")
        i += 1


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

#Zasada działania: Krok 1 odczytać wszystkie pliki
pliki = getfiles("../ToolLists/NC_Programs")

#Stworznienie plików do listy narzędzi
createlist(pliki)
#W jednym poleceniu musi być zgarnięcie numerów T i wpisanie ich do plików
i = 0
while i < len(pliki):
    tlist = makeTlist(pliki[i])
    tfile = open("ToolList"+pliki[i]+".txt", "a")
    j = 0
    while j < len(tlist):
        tfile.write(tlist[j]+"\n")
        j += 1      
    i += 1

print("-done in %s seconds-" % (time.time() - start_time))

#sex ma sie dodać do dev i pullnąć ręcznie do maina