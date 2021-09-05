import time, pyodbc, getpass, os.path
from modules import dirmod, toolgetmod, tdmsql

def main():
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
            mdfdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/Folder na pliki mdf"
            NCfiles = dirmod.getfiles(mdfdir)
            print("Wybierz plik MDF, z którego chcesz stworzyć listę narzędziową w TDM:\n")
            i = 0
            for file in NCfiles:
                print(str(i) + " - " + NCfiles[i])
                i += 1
            sel = int(input("\nWybór (0, 1, 2, etc...):"))
            NCpath = mdfdir + "/" + NCfiles[sel]
            #NCpath = "Python/" + input("Podaj nazwę pliku: ")
            NCprogram = ""
            for char in NCpath:
                if char != '.':
                    NCprogram += char
                else:
                    break
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=testdb;UID=tms;PWD=tms')
            listID = tdmsql.tdmGetMaxListID(cnxn)
            user = getpass.getuser()
            timestamp = round(time.time())
            try:
                tlist = toolgetmod.fileTlistLimited(NCpath, 100)
            except FileNotFoundError:
                print("Nie można było znaleźć pliku!")
                break
            tdmsql.tdmCreateList(cnxn, NCprogram, listID, user, timestamp)
            tdmsql.tdmAddTools(listID, tlist)
            tdmsql.tdmAddLogfile
            tdmsql.tdmDisconnect(cnxn)
            break
        else:
            print("Podaj poprawną wartość!")
    
if __name__ == '__main__':
    main()