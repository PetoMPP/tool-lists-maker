#CREATING THE LIST IN THE SYSTEM WITHOUT 'N' PREFIX (UNICODE STRING)
       insert into TDM_LIST

       (LISTID, NCPROGRAM, PARTNAME, PARTNAME01, 

        WORKPIECEDRAWING, JOBPLAN, WORKPROCESS, 

        MATERIALID, MACHINEID, MACHINEGROUPID, 

        FIXTURE, NOTE, NOTE01, WORKPIECECLASSID, 

        STATEID1, STATEID2, LISTTYPE, 

        USERNAME, ACCESSCODE)

     values

       ('0002712'      ,

      '5555555'      ,

      null      ,

      null      ,

      null      ,

      null      ,

      null      ,

      null      ,

      null      ,

      null      ,

      null      ,

      null      ,

      null      ,

      null      ,

      'TOOL LIST IS PREPARING'      ,

      null      ,

       2      ,

      null,

      ''  )
#CREATING THE LIST IN THE SYSTEM WITH 'N' PREFIX (UNICODE STRING)
       insert into TDM_LIST

    (TIMESTAMP, LISTID, NCPROGRAM, PARTNAME, PARTNAME01, 

    WORKPIECEDRAWING, JOBPLAN, WORKPROCESS, 

    MATERIALID, MACHINEID, MACHINEGROUPID, 

    FIXTURE, NOTE, NOTE01, WORKPIECECLASSID, 

    STATEID1, STATEID2, LISTTYPE, 

    USERNAME, ACCESSCODE)

       values

    (1628337607, N'0002712'      ,

    N'5555555'      ,

    null      ,

    null      ,

    null      ,

    null      ,

    null      ,

    null      ,

    null      ,

    null      ,

    null      ,

    null      ,

    null      ,

    null      ,

    N'TOOL LIST IS PREPARING'      ,

    null      ,

    2      ,

    null,

    null  )


#INSERTING LOGFILE DATA
       insert into TMS_CHANGEINFO 

    (TIMESTAMP, TNAME, ID, ID2, ID3, ID4, ID5, 

    POS, USERID, NOTE, CHANGEDATE, CHANGETIME, CREATIONTIMESTAMP) 

       values (1628337608, N'TDM_LIST', 

        N'0002712' , 

        null , 

        null , 

        null , 

        null , 

        1, 

        N'PIETRZYK_P', 

        null ,  

        153986, 50408, 1628337608 )
