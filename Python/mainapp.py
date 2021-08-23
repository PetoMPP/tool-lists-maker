import time
from modules import dirmod
from modules import toolgetmod

#wybór trybu
while True:
    while True:
        try:
            mode_sel=int(input("Wybierz tryb działania:\n(1)Tworzenie plików tekstowych z programów z Shopturna;\n(2)Stworznie listy narzędziowej w TDM z pliku MDF.\n:"))
            break
        except ValueError:
            print("Podaj poprawną wartość!")
            
    if mode_sel == 1:
        #NCpath = input("Podaj ścieżkę do folderu z programami")
        NCpath = input("Podaj ścieżkę do folderu z programami (np. M:\\3_Retransmission:")

        start_time = time.time()
        #Zasada działania: Krok 1 odczytać foldery i pliki z programami (Działa)
        dirs = dirmod.getDir(NCpath) #lista folderów
        i = 0
        while i < len(dirs):
            try:
                NCfiles = dirmod.getfiles(NCpath+"/"+dirs[i]) #lista plików w folderze
            except FileNotFoundError:
                print("Podfolder w podfolderze!!")
            j = 0
            while j < len(NCfiles):
                tname = dirs[i]+"-"+NCfiles[j] #nazwa pliku
                tdir = dirs[i]+"/"+NCfiles[j] #ścieżka do pliku
                tfile = open("Lista"+tname+".txt", "w") #stworzenie pliku numer-mocx
                try:
                    tlist = toolgetmod.fileTlist(NCpath+"/"+tdir) #lista numerów T w pliku
                except UnicodeDecodeError:
                    print(tname+" - Zły format pliku!!")
                except FileNotFoundError:
                    print(tname+" - Podfolder w podfolderze!!")
                k = 0
                while k < len(tlist):
                    tfile.write(tlist[k]+"\n") #wpisanie narzędzi do plików
                    k += 1
                j += 1
            i += 1
        print("-done in %s seconds-" % (time.time() - start_time))
        break
    elif mode_sel == 2:
        print("sex")
        break
    else:
        print("Podaj poprawną wartość!")