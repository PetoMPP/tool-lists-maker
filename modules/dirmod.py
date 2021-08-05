from os import listdir, name, walk
from os.path import isfile, join

#Pobranie listy folderów z programami
def getDir(path):
    dirlist = []
    for (dirpath, dirnames, filenames) in walk(path):
        dirlist.extend(dirnames)
    return dirlist

#Pobranie listy programów (Działa)
def getfiles(path):
    filelist = [file for file in listdir(path) if isfile(join(path,file))]
    return filelist

#Stworzenie pliku dla listy narzędzi (pliki w folderze) (Działa)
def createlistfiles(flist):
    i = 0
    while i < len(flist):
        listfile = open("ToolList"+flist[i]+".txt", "a")
        i += 1
        return listfile

#Stworzenie pliku dla listy narzędzi (pliki w podfolderach) (Działa)
def createlistdirs(dirlist):
    i = 0
    while i < len(dirlist):
        listfile = open(dirlist[i]+".txt", "a")
        i += 1
        return listfile