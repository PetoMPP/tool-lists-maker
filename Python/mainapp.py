from os import path
import time, pyodbc, getpass, os.path
from modules import dirmod, toolgetmod, tdmsql
from distutils.dir_util import copy_tree
import distutils.errors

def main():
    #wybór trybu
    while True:
        while True:
            try:
                mode_sel=int(input("Wybierz tryb działania:\n(1)Tworzenie plików tekstowych z programów z Shopturna;\n(2)Stworznie listy narzędziowej w TDM z pliku MPF;\n(3)Masowe dodawanie list narzędziowych na datrona;\n:"))
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
            mpfdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/Folder na pliki mpf"
            NCfiles = dirmod.getfiles(mpfdir)
            print(mpfdir)
            print("Wybierz plik MPF, z którego chcesz stworzyć listę narzędziową w TDM:\n")
            i = 0
            for file in NCfiles:
                print(str(i) + " - " + NCfiles[i])
                i += 1
            while True:
                try:
                    sel = int(input("\nWybór (0, 1, 2, etc...):"))
                    NCpath = mpfdir + "/" + NCfiles[sel]
                    break
                except IndexError:
                    print("Podaj poprawną wartość!")
                except ValueError:
                    print("Podaj poprawną wartość!")
            print("Program rozpoczyna pracę")
            start_time = time.time()
            NCprogram = ""
            for char in NCfiles[sel]:
                if char != '.':
                    NCprogram += char
                else:
                    break
            try:
                print("Łączenie z bazą danych TDM...")
                cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=uhlplvm03;DATABASE=TDMPROD;UID=tms;PWD=tms')
                print("Połączono!")
            except pyodbc.OperationalError:
                print("Brak połączenia z bazą TDM!")
                input("Naciśnij ENTER aby zamknąć okno")
                break
            listID = tdmsql.tdmGetMaxListID(cnxn)
            user = getpass.getuser()
            user = user.upper()
            timestamp = round(time.time())
            username = tdmsql.tdmGetUserName(cnxn, user)
            try:
                tlist = toolgetmod.fileTlistLimited(NCpath, 100)
            except FileNotFoundError:
                print("Nie można było znaleźć pliku!")
                break
            validTools = tdmsql.tdmCheckIfToolsExists(cnxn, tlist)
            if validTools:
                tdmsql.tdmCreateList(cnxn, NCprogram, listID, username, timestamp)
                tdmsql.tdmAddTools(cnxn, listID, tlist, timestamp)
                tdmsql.tdmAddLogfile(cnxn, listID, user, timestamp)
                tdmsql.tdmDisconnect(cnxn)
                print("Stworzenie listy zajęło %s sekund!" % (start_time - time.time()))
            else:
                print("Program zawiera narzędzia, których nie ma w TDM!")
            input("Naciśnij ENTER aby zamknąć okno")
            break
        elif mode_sel == 3:
            fusiondir = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/fusion"
            fusion_dirs = dirmod.getDir(fusiondir)
            fusion_files = dirmod.getfiles(fusiondir)
            d2_dict = {
                "8000": "435.B-0800-A1-XF H10F DATRON",
                "0068820B": "0068820E",
                "0068041": "0068081L",
                "T1608": "1.78766-12",
                "0068798010": "0068798",
                "0068034": "0068034A",
                "0068814A": "0068814E"
            }
            while True:
                print("Wszystkie foldery w folderze fusion zostaną dodane do TDM!")
                print("Aby wyświetlić listę folderów, które zostaną dodane/usuniętę napisz \"foldery\"")
                print("Aby usunąć listy na podstawie nazw plików napisz \"purge\"")
                print("Aby utworzyć plik z listą narzędzi, których nie można łatwo odnaleźć w TDM wpisz \"braki\"")
                print("Aby zaciągnąć foldery do folderu fusion napisz \"zbierz\"")
                print("Aby zaciągnąć wszystkie foldery z \"M:\MMLCUBEB\" do folderu fusion napisz \"zbierz wszystko\"")
                print("Aby przekonwertować listy zaciągnięte do fusion raw na mocowania napisz \"konwertuj\"")
                print("Aby dodać listy narzędziow do TDM napisz \"kasjan to chuj\"")
                bsel = input(":")
                if bsel == "foldery":
                    print("\n")
                    for dir in fusion_dirs:
                        print(dir)
                    print("\n")
                    input("Kontynuuj enterem...")
                elif bsel == "braki":
                    try:
                        print("Łączenie z bazą danych TDM...")
                        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=uhlplvm03;DATABASE=TDMPROD;UID=tms;PWD=tms')
                        print("Połączono!")
                    except pyodbc.OperationalError:
                        print("Brak połączenia z bazą TDM!")
                        input("Naciśnij ENTER aby zamknąć okno")
                        break
                    mega_list = []
                    for dir in fusion_dirs:
                        dirpath = fusiondir + "\\" + dir
                        for file in dirmod.getfiles(dirpath):
                            tlist = toolgetmod.fileTlistFUSION(dirpath + "\\" + file)
                            for ele in tlist:
                                mega_list.append(toolgetmod.clearFUSION(ele))
                    creation_time = round(time.time())
                    err_list_d = []
                    for ele in mega_list:
                        try:
                            ele = d2_dict[ele]
                            err_list_d.append(ele)
                        except KeyError:
                            err_list_d.append(ele)
                    err_list_d = tdmsql.tdmFindInvalidComps(cnxn, err_list_d)
                    err_list_d = list(set(err_list_d))
                    err_names = []
                    for comp in err_list_d:
                        for file in dirmod.getfiles(dirpath):
                            ncprg = open(dirpath + "\\" + file)
                            for line in ncprg.readlines():
                                if not toolgetmod.findNamesFUSION(line, comp):
                                    continue
                                else:
                                    err_names.append(toolgetmod.findNamesFUSION(line, comp))
                    err_file = open(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\" + "Lista narzędzi do dodania" + str(creation_time) + ".txt", 'a')
                    err_file.write("Lista narzędzi do poprawienia:\n")
                    for ele in err_list_d:
                        err_file.write(str(ele) + "\n")
                    err_file.write("Lista opisów:\n")
                    for ele in err_names:
                        err_file.write(str(ele) + "\n")
                    err_file.close()
                    print("lista narzędzi została zapisana w głównym katalogu programu pod nazwą: Lista narzędzi do dodania" + str(creation_time) + ".txt")                    
                    input("Kontynuuj enterem...")
                    """elif bsel == "purge":
                    NCprogram_list = []
                    for dir in fusion_dirs:
                        NCprogram = ""
                        for char in dir:
                            if char != '.':
                                NCprogram += char
                            else:
                                break
                        NCprogram_list.append(NCprogram)
                    print(NCprogram_list)
                    print("Listy z powyższymi numerami zostaną usunięte z TDM")
                    conf = input("Aby kontynuować wpisz \"PURGE\"\n:")
                    if conf == "PURGE":
                        try:
                            print("Łączenie z bazą danych TDM...")
                            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=uhlplvm03;DATABASE=TDMPROD;UID=tms;PWD=tms')
                            print("Połączono!")
                        except pyodbc.OperationalError:
                            print("Brak połączenia z bazą TDM!")
                            input("Naciśnij ENTER aby zamknąć okno")
                            break
                        count = 0
                        for prog in NCprogram_list:
                            if tdmsql.tdmListCheckbyNC(cnxn, prog):
                                tdmsql.tdmDeleteListbyNC(cnxn, prog)
                                count += 1
                            else:
                                print("Nie znaleziono listy o numerze operacji %s" % (str(prog)))
                        if count == 0:
                            print("Nie usunięto żadnej listy")
                        elif count == 1:
                            print("Usunięto %d listę" % (count))
                        elif count % 10 < 5:
                            print("Usunięto %d listy" % (count))
                        elif count % 10 >= 5:
                            print("Usunięto %d list" % (count))                         
                    else: 
                        print("Do zobaczenia!")
                        input("Kontynuuj enterem...")"""  

                elif bsel == "Kasjan to chuj":
                    print("kasjan z dużej? nie przejdzie..")
                    input("Kontynuuj enterem...")
                elif bsel == "kasjan to chuj":
                    start_time = time.time()
                    try:
                        print("Łączenie z bazą danych TDM...")
                        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=uhlplvm03;DATABASE=TDMPROD;UID=tms;PWD=tms')
                        print("Połączono!")
                    except pyodbc.OperationalError:
                        print("Brak połączenia z bazą TDM!")
                        input("Naciśnij ENTER aby zamknąć okno")
                        break
                    for dir in fusion_dirs:
                        NCprogram = dir
                        '''for char in dir:
                            if char != '.':
                                NCprogram += char
                            else:
                                break'''
                        user = getpass.getuser()
                        user = user.upper()
                        username = tdmsql.tdmGetUserName(cnxn, user)
                        for dir in fusion_dirs:
                            dirpath = fusiondir + "\\" + dir
                            d2list = []
                            d2list_r = []
                            for file in dirmod.getfiles(dirpath):
                                listID = tdmsql.tdmGetMaxListID(cnxn)
                                timestamp = round(time.time())
                                dirty_list = toolgetmod.fileTlistFUSION(fusiondir + "\\" + dir + "\\" + file)
                                for ele in dirty_list:
                                    d2list.append(toolgetmod.clearFUSION(ele))
                            for ele in d2list:
                                try:
                                    ele = d2_dict[ele]
                                    d2list_r.append(ele)
                                except KeyError:
                                    d2list_r.append(ele)
                            clist = tdmsql.tdmGetCompsID(cnxn, d2list_r)
                            clist = list(set(clist))
                            print(clist)
                            if clist[0] != '':
                                tdmsql.tdmCreateList(cnxn, NCprogram, listID, username, timestamp)
                                tdmsql.tdmAddComps(cnxn, listID, clist, timestamp)
                                tdmsql.tdmAddLogfile(cnxn, listID, user, timestamp)
                                tdmsql.tdmDisconnect(cnxn)
                            else:
                                print("Program zawiera narzędzia, których nie ma w TDM!")
                                input("Naciśnij ENTER kontynuować")
                    print("Stworzenie list zajęło %s sekund!" % (time.time() - start_time))
                    print("Dziękuję za wspólną zabawę!")
                    input("Wciśnij ENTER, żeby kontynuować")
                elif bsel == "zbierz":
                    fusion_programs_dir = "M:\MMLCUBEB"
                    while True:
                        try:
                            sel_dir = input("Wpisz numer programu\n:")
                            src_dir = fusion_programs_dir + "//" + sel_dir
                            trg_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\" + "fusion raw" + "\\" + sel_dir
                            copy_tree(src_dir, trg_dir)
                            break
                        except distutils.errors.DistutilsFileError:
                            print("Spróbuj jeszcze raz")
                elif bsel == "zbierz wszystko":
                    pass
                elif bsel == "konwertuj":
                    pass
                else:
                    print("Spróbuj jeszcze raz")
                    input("Kontynuuj enterem...")

        else:
            print("Podaj poprawną wartość!")
    
if __name__ == '__main__':
    main()