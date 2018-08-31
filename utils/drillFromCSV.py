import csv
import time
import sqlite3
from dbfread import DBF

DBFILE='../DBs/mzdata.db'
RESULTCSV='../output/result'


def makeCsvFromDBF(DbfPath, CurPeriod):
    dbfTable = DBF(DbfPath, ignore_missing_memofile=True)
    f = open(RESULTCSV+CurPeriod+'.csv', "w")
    header = [ 'qhdm', 'year', 'sq' ]
    dataRow = [ ]
    writer = csv.writer(f)
    conn = sqlite3.connect(DBFILE)
    headerSQL = 'select DbfID from IndexDict where Period={CurPeriod}'.format(CurPeriod=CurPeriod)
    cursor = conn.execute(headerSQL)
    for res in cursor:
        header.append(res[ 0 ])
    writer.writerow(header)
    sTime = time.time()
    print('Start to creat CSV file.')
    for record in dbfTable:
        dataRow.append(record[ 'SYS_ZDM' ][ 0:12 ])
        dataRow.append(CurPeriod[ 0:4 ])
        dataRow.append(record[ 'SYS_ZDM' ][ 12:14 ])
        for i in range(4, len(header) + 1):
            dataRow.append(record[ header[ i - 1 ] ])
        writer.writerow(dataRow)
        dataRow = [ ]
    #print('CSV file created! Elapse ' + str(round(time.time() - sTime), 2) + 's')
    conn.close()

makeCsvFromDBF('../DBF/MZBB17JBZH0001.DBF','201712')
