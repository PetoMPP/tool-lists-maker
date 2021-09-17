import pyodbc, re

def tdmConnect(cnxn):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=testdb;UID=tms;PWD=tms')

def tdmGetMaxListID(cnxn):
    cursor = cnxn.cursor()
    cursor.execute("Select max(LISTID) from TDM_LIST;")
    maxid = str(cursor.fetchall())
    maxid = re.sub('[^A-Za-z0-9]+', '', maxid)
    maxid = int(maxid) + 1
    maxid = str(maxid)
    while len(maxid) < 7:
        maxid = '0' + maxid
    return maxid

def tdmGetUserName(cnxn, userID):
    cursor = cnxn.cursor()
    cursor.execute("SELECT [FIRSTNAME] FROM TMS_USER WHERE USERNAME = '%s'" % (userID))
    firstname = str(cursor.fetchall())
    firstname = re.sub('[^A-Za-z0-9]+', '', firstname)
    cursor.execute("SELECT [NAME] FROM TMS_USER WHERE USERNAME = '%s'" % (userID))
    lastname = str(cursor.fetchall())
    lastname = re.sub('[^A-Za-z0-9]+', '', lastname)
    username = firstname + " " + lastname
    return username


def tdmGetCompsID(cnxn, d2list):
    cursor = cnxn.cursor()
    clist = []
    for d2 in d2list:
        cursor.execute("SELECT [COMPID] FROM TDM_COMP WHERE USERNAME = '%s'" % (d2))
        compid = str(cursor.fetchall())
        compid = re.sub('[^A-Za-z0-9]+', '', compid)
        clist.append(compid)



def tdmCheckIfToolsExists(cnxn, tlist):
    valid = True
    cursor = cnxn.cursor()
    for tool in tlist:
        cursor.execute("SELECT TOOLID FROM TDM_TOOL WHERE TOOLID = '%s'" % (tool))
        output = str(cursor.fetchall())
        output = re.sub('[^A-Za-z0-9]+', '', output)
        if output == "":
            valid = False
    return valid

def tdmCheckIfCompExists(cnxn, tlist):
    valid = True
    cursor = cnxn.cursor()
    for tool in tlist:
        cursor.execute("SELECT TOOLID FROM TDM_COMP WHERE TOOLID = '%s'" % (tool))
        output = str(cursor.fetchall())
        output = re.sub('[^A-Za-z0-9]+', '', output)
        if output == "":
            valid = False
    return valid

def tdmFindInvalidComps(cnxn, tlist):
    cursor = cnxn.cursor()
    inv_comps = []
    for comp in tlist:
        cursor.execute("SELECT TOOLID FROM TDM_COMP WHERE TOOLID = '%s'" % (comp))
        output = str(cursor.fetchall())
        output = re.sub('[^A-Za-z0-9]+', '', output)
        if output == "":
            inv_comps.append(comp)
    inv_comps = list(set(inv_comps))
    return inv_comps


def tdmListCheckbyNC(cnxn, NCprogram):
    cursor = cnxn.cursor()
    cursor.execute("SELECT LISTID FROM TDM_LIST WHERE NCPROGRAM = '%s'" % (NCprogram))
    output = str(cursor.fetchall())
    output = re.sub('[^A-Za-z0-9]+', '', output)
    if output == "":
        return False
    else:
        return True


def tdmCreateList(cnxn, NCprogram, maxid, user, timestamp):
    cursor = cnxn.cursor()
    #cursor.execute("insert into TDM_LIST (TIMESTAMP, LISTID, NCPROGRAM, PARTNAME, PARTNAME01, WORKPIECEDRAWING, JOBPLAN, WORKPROCESS, MATERIALID, MACHINEID, MACHINEGROUPID, FIXTURE, NOTE, NOTE01, WORKPIECECLASSID, STATEID1, STATEID2, LISTTYPE, USERNAME, ACCESSCODE) values (1628337607, N'0002712', N'5555555', null, null, null, null, null, null, null, null, null, null, null, null, N'TOOL LIST IS PREPARING', null, 2, null, null)")
    cursor.execute("insert into TDM_LIST (TIMESTAMP, LISTID, NCPROGRAM, PARTNAME, PARTNAME01, WORKPIECEDRAWING, JOBPLAN, WORKPROCESS, MATERIALID, MACHINEID, MACHINEGROUPID, FIXTURE, NOTE, NOTE01, WORKPIECECLASSID, STATEID1, STATEID2, LISTTYPE, USERNAME, ACCESSCODE) values (%d, N'%s', N'%s', null, null, N'%s', null, null, null, null, null, null, null, null, null, N'TOOL LIST IS PREPARING', null, 2, N'%s', null)" % (timestamp, maxid, NCprogram, maxid, user))
    cnxn.commit()

def tdmDeleteListbyNC(cnxn, NCprogram):
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM TDM_LIST WHERE NCPROGRAM = '%s'" % (NCprogram))
    cnxn.commit()


def tdmAddTools(cnxn, listID, tlist, timestamp):
    i = 1
    cursor = cnxn.cursor()
    for tool in tlist:
        cursor.execute("INSERT INTO TDM_LISTLISTB VALUES ('%s', %d, NULL, '%s', NULL, NULL, NULL, '%s', NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, %d)" % (listID, i, tool, tool, timestamp))
        cnxn.commit()
        i += 1
        print("%d tool added")

    

def tdmAddLogfile(cnxn, listid, user, timestamp):
    cursor = cnxn.cursor()
    #cursor.execute("INSERT INTO TMS_CHANGEINFO (TIMESTAMP, TNAME, ID, ID2, ID3, ID4, ID5, POS, USERID, NOTE, CHANGEDATE, CHANGETIME, CREATIONTIMESTAMP) VALUES (1628337608, N'TDM_LIST', N'0002712',null ,null ,null ,null ,1, N'PIETRZYK_P ,null ,153986, 50408, 1628337608)")
    cursor.execute("INSERT INTO TMS_CHANGEINFO (TIMESTAMP, TNAME, ID, ID2, ID3, ID4, ID5, POS, USERID, NOTE, CHANGEDATE, CHANGETIME, CREATIONTIMESTAMP) VALUES (%d , 'TDM_LIST', '%s',null ,null ,null ,null ,1 , '%s','Lista stworzona automatycznie za pomocą programu Tool List Maker' ,153986, 50408, %d)" % (timestamp, listid, user, timestamp))
    cnxn.commit()

def tdmDisconnect(cnxn):
    cnxn.close()
