import csv
import time
from utils.sqlutils import getDB

from dbfread import DBF

RESULTCSVPATH='../output/resultbz'

def datacsvfromdbf(DbfPath, CurPeriod, DbfKind ):
    dbfTable = DBF(DbfPath, ignore_missing_memofile=True, encoding="gbk")
    f = open(RESULTCSVPATH+CurPeriod+'.csv', "w")
    header = [ 'qhdm', 'period', 'year', 'sq', 'table' ]
    dataRow = [ ]
    writer = csv.writer(f)
    conn = getDB().get_conn()
    headerSQL = 'select DbfID from IndexDict where Period={CurPeriod} and DataTable="{DbfKind}"'.format(CurPeriod=CurPeriod,DbfKind=DbfKind)
    cursor = conn.cursor()
    cursor.execute(headerSQL)
    for res in cursor:
        header.append(res[ 0 ])
    writer.writerow(header)
    print(header)
    sTime = time.time()
    print('Start to creat CSV file.')
    for record in dbfTable:
        dataRow.append(record[ 'SYS_ZDM' ][ 0:12 ])
        dataRow.append(CurPeriod[ 0:4 ]+record[ 'SYS_ZDM' ][ 12:14])
        dataRow.append(CurPeriod[ 0:4 ])
        dataRow.append(record[ 'SYS_ZDM' ][ 12:14 ])
        dataRow.append(DbfKind)
        for i in range(6, len(header) + 1):
            dataRow.append(record[ header[ i - 1 ] ])
        writer.writerow(dataRow)
        dataRow = [ ]
    eTime =time.time()
    print('CSV file result'+CurPeriod+'.csv has been created.'+str(round(eTime-sTime,1))+' seconds elapsed')
    conn.close()

def indexcsvfromdbf(DbfPath, CurPeriod, DbfKind ):
    dbfTable = DBF(DbfPath, ignore_missing_memofile=True, encoding="gbk")
    f = open(RESULTCSVPATH+CurPeriod+'index.csv', "w")
    header = [ 'qhdm', 'period', 'year', 'sq', 'table' ]
    dataRow = [ ]
    writer = csv.writer(f)
    conn = getDB().get_conn()
    headerSQL = 'select DbfID from IndexDict where Period={CurPeriod} and DataTable="{DbfKind}" and indexID="SFL_EXP"'.format(CurPeriod=CurPeriod,DbfKind=DbfKind)
    cursor = conn.cursor()
    cursor.execute(headerSQL)
    for res in cursor:
        header.append(res[ 0 ])
    writer.writerow(header)
    print(header)
    sTime = time.time()
    print('Start to creat CSV file.')
    for record in dbfTable:
        dataRow.append(record[ 'SYS_ZDM' ][ 0:12 ])
        dataRow.append(CurPeriod[ 0:4 ]+record[ 'SYS_ZDM' ][ 12:14])
        dataRow.append(CurPeriod[ 0:4 ])
        dataRow.append(record[ 'SYS_ZDM' ][ 12:14 ])
        dataRow.append(DbfKind)
        for i in range(6, len(header) + 1):
            dataRow.append(record[ header[ i - 1 ] ])
        writer.writerow(dataRow)
        dataRow = [ ]
    eTime =time.time()
    print('CSV file result'+CurPeriod+'.csv has been created.'+str(round(eTime-sTime,1))+' seconds elapsed')
    conn.close()

def qhcsvfrmdbf(qhdbf, curperiod):
    dbfTable = DBF(qhdbf, ignore_missing_memofile=True, encoding="gbk")
    f = open(RESULTCSVPATH+curperiod+'.csv', "w")
    header = [ 'qhdm', 'period', 'year', 'sq','table']
    dataRow = [ ]
    writer = csv.writer(f)
    conn = getDB().get_conn()
    sTime = time.time()
    print('Start to creat qhdm CSV file.')
    try:
        for record in dbfTable:
            print(record)
            continue
    except UnicodeDecodeError:
        print('error')

    eTime =time.time()
    print('CSV file result'+curperiod+'.csv has been created.'+str(round(eTime-sTime,1))+' seconds elapsed')
    conn.close()

#datacsvfromdbf('../DBF/MZBB18YBZH0001.DBF','201808','YB')
indexcsvfromdbf('../DBF/MZBB18YBZH0001.DBF','201808','YB')
#qhcsvfrmdbf('../DBF/MZBB18YBZH0001.DBF','201807')
