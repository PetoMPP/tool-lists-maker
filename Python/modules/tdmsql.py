import pyodbc

def tdmConnect(cnxn):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=testdb;UID=tms;PWD=tms')

def tdmGetMaxListID(cnxn):
    cursor = cnxn.cursor()
    cursor.execute("Select max(LISTID) from TDM_LIST;")
    maxid = cursor.fetchone()
    maxid = int(maxid) + 1
    maxid = str(maxid)
    while len(maxid) < 7:
        maxid = '0' + maxid
    return maxid

def tdmCreateList(cnxn, NCprogram, maxid, user, timestamp):
    cursor = cnxn.cursor()
    #cursor.execute("insert into TDM_LIST (TIMESTAMP, LISTID, NCPROGRAM, PARTNAME, PARTNAME01, WORKPIECEDRAWING, JOBPLAN, WORKPROCESS, MATERIALID, MACHINEID, MACHINEGROUPID, FIXTURE, NOTE, NOTE01, WORKPIECECLASSID, STATEID1, STATEID2, LISTTYPE, USERNAME, ACCESSCODE) values (1628337607, N'0002712', N'5555555', null, null, null, null, null, null, null, null, null, null, null, null, N'TOOL LIST IS PREPARING', null, 2, null, null)")
    cursor.execute("insert into TDM_LIST (TIMESTAMP, LISTID, NCPROGRAM, PARTNAME, PARTNAME01, WORKPIECEDRAWING, JOBPLAN, WORKPROCESS, MATERIALID, MACHINEID, MACHINEGROUPID, FIXTURE, NOTE, NOTE01, WORKPIECECLASSID, STATEID1, STATEID2, LISTTYPE, USERNAME, ACCESSCODE) values (%d, N'%s', N'%s', null, null, null, null, null, null, null, null, null, null, null, null, N'TOOL LIST IS PREPARING', null, 2, %s, null)" % (timestamp, maxid, NCprogram, user))
    cnxn.commit()

def tdmAddTools(listID, tlist):
    pass

def tdmAddLogfile(cnxn, listid, user, timestamp):
    cursor = cnxn.cursor()
    #cursor.execute("INSERT INTO TMS_CHANGEINFO (TIMESTAMP, TNAME, ID, ID2, ID3, ID4, ID5, POS, USERID, NOTE, CHANGEDATE, CHANGETIME, CREATIONTIMESTAMP) VALUES (1628337608, N'TDM_LIST', N'0002712',null ,null ,null ,null ,1, N'PIETRZYK_P ,null ,153986, 50408, 1628337608)")
    cursor.execute("INSERT INTO TMS_CHANGEINFO (TIMESTAMP, TNAME, ID, ID2, ID3, ID4, ID5, POS, USERID, NOTE, CHANGEDATE, CHANGETIME, CREATIONTIMESTAMP) VALUES (%d , N'TDM_LIST', N'%s',null ,null ,null ,null ,1 , n'%s','Lista stworzona automatycznie za pomocą programu Tool List Maker' ,153986, 50408, %d)" % (timestamp, listid, user, timestamp))
    cnxn.commit()

def tdmDisconnect(cnxn):
    cnxn.close()
