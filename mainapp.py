import time
from modules import dirmod
from modules import toolgetmod

start_time = time.time()

#Zasada działania: Krok 1 odczytać wszystkie pliki
pliki = dirmod.getfiles("../NC_Programs")

#Stworznienie plików do listy narzędzi
dirmod.createlist(pliki)

#W jednym poleceniu musi być zgarnięcie numerów T i wpisanie ich do plików

#NCpath = input("Podaj ścieżkę do folderu z programami")
NCpath = 
i = 0
while i < len(pliki):
    tlist = toolgetmod.fileTlist(pliki[i],NCpath)
    tfile = open("ToolList"+pliki[i]+".txt", "a")
    j = 0
    while j < len(tlist):
        tfile.write(tlist[j]+"\n")
        j += 1      
    i += 1

print("-done in %s seconds-" % (time.time() - start_time))