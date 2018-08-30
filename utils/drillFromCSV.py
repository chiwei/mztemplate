import csv
import sqlite3
from dbfread import DBF

DBFPATH='../DBF/jb18.DBF'
DBFILE='../DBs/mzdata.db'
RESULTCSV='../output/result.csv'


def makeCsvFromDBF(DbfPath,CurPeriod):
    dbfTable=DBF(DBFPATH,ignore_missing_memofile=True)
    f=open(RESULTCSV,"w")
    header=['qhdm','year','sq']
    dataRow=[]

    writer=csv.writer(f)
    conn=sqlite3.connect(DBFILE)
    headerSQL='select DbfID from IndexDict where Period={CurPeriod}'.format(CurPeriod=CurPeriod)
    cursor=conn.execute(headerSQL)
    for res in cursor:
        header.append(res[0])
    for rec in dbfTable:
        print(rec['F_1'])
    writer.writerow(header)
    conn.close()

makeCsvFromDBF(DBFPATH,'201806')
