import time
from modules import dirmod
from modules import toolgetmod

start_time = time.time()

#Stworzenie klasy dla pliku narzędzia
class NCfile:
    def __init__(self, dir, fname):
        self.dir = dir
        self.fname = fname


#NCpath = input("Podaj ścieżkę do folderu z programami")
NCpath = "NC_Programs"

#Zasada działania: Krok 1 odczytać foldery i pliki z programami (Działa)
dirs = dirmod.getDir(NCpath) #lista folderów
i = 0
while i < len(dirs):
    NCfiles = dirmod.getfiles(NCpath+"/"+dirs[i]) #lista plików w folderze
    j = 0
    while j < len(NCfiles):
        tname = dirs[i]+"-"+NCfiles[j] #nazwa pliku
        tdir = dirs[i]+"/"+NCfiles[j] #ścieżka do pliku
        tfile = open("Lista"+tname+".txt", "w") #stworzenie pliku numer-mocx
        tlist = toolgetmod.fileTlist(NCpath+"/"+tdir) #lista numerów T w pliku
        k = 0
        while k < len(tlist):
            tfile.write(tlist[k]+"\n") #wpisanie narzędzi do plików
            k += 1
        j += 1
    i += 1
print("-done in %s seconds-" % (time.time() - start_time))
