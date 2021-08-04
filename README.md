# tool-lists-maker
Software for analysing the tools used in NC programs and pushing them to TDM database as a Tool List

There's much tbd and almost nothing works

The supported file architecture for the software to work is:
main catalog named NC_Programs containing
folders named after part numbers which contain
mdf files named nafter a part number and operation number

#done

Getting the file architecture
Creating a file for the tool lists
Getting tool numbers from file
Creating the tool list out of the file
Scirpt executing all of the above

#to be done

adjust the script for files in subfolders
removing duplicates
add a switch for looking for files in rootdir or for files in subdirs, or get all files from the dir and subdirs
adding a gui/a local webpage service (Django)
executing a query for making the list in tdm
executing a query for inserting the tools in tool list in tdm
