import csv
import time
from utils.sqlutils import getDB

from dbfread import DBF

RESULTCSVPATH='../output/result'


def makeCsvFromDBF(DbfPath, CurPeriod):
    dbfTable = DBF(DbfPath, ignore_missing_memofile=True)
    f = open(RESULTCSVPATH+CurPeriod+'.csv', "w")
    header = [ 'qhdm', 'period', 'year', 'sq' ]
    dataRow = [ ]
    writer = csv.writer(f)
    conn = getDB().get_conn()
    headerSQL = 'select DbfID from IndexDict where Period={CurPeriod}'.format(CurPeriod=CurPeriod)
    cursor = conn.cursor()
    cursor.execute(headerSQL)
    for res in cursor:
        header.append(res[ 0 ])
    writer.writerow(header)
    sTime = time.time()
    print('Start to creat CSV file.')
    for record in dbfTable:
        dataRow.append(record[ 'SYS_ZDM' ][ 0:12 ])
        dataRow.append(CurPeriod[ 0:4 ]+record[ 'SYS_ZDM' ][ 12:14])
        dataRow.append(CurPeriod[ 0:4 ])
        dataRow.append(record[ 'SYS_ZDM' ][ 12:14 ])
        for i in range(5, len(header) + 1):
            dataRow.append(record[ header[ i - 1 ] ])
        writer.writerow(dataRow)
        dataRow = [ ]
    eTime =time.time()
    print('CSV file result'+CurPeriod+'.csv has been created.'+str(round(eTime-sTime,1))+' seconds elapsed')
    conn.close()

makeCsvFromDBF('../DBF/MZBB17YBZH0001.DBF','201711')
