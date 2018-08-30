import os
import sqlite3
import csv

DBPATH='../DBs/'

def createConn(dbName):
    if os.path.exists(DBPATH+dbName+'.db'):
        print('database exists.')
    else:
        conn=sqlite3.connect(dbName+'.db')
        print('database '+dbName+' created!')
        return dbName+'.db'

def wrapperSelector(MatchedIndex,Period,qhdm):
    conn=sqlite3.connect(DBPATH+"mzdata.db")
    sql='select Value from DataWarehouse where Period="{Period}" \
        and qhdm="{qhdm}" and MatchedIndex="{MatchedIndex}"'.format(MatchedIndex=MatchedIndex,Period=Period,qhdm=qhdm)
    cursor=conn.execute(sql)
    for row in cursor:
        print(row[0])
    conn.close()
    return row[0]


def loadfromCSV(csvpath):
   data=[]
   with open(csvpath,'r') as csvfile:
       filereader=csv.reader(csvfile)
       print('start to create DBF object.')
       for row in filereader:
          print(row)
          data.append(row)
   print('DBF object created.')
   conn=sqlite3.connect("cmder.db")
   conn.execute('''create table if not exists jbdata(
                          qhdm varchar(32),
                          sq varchar(32),
                          csdbrs number,
                          csdbhs number,
                          ncdbrs number,
                          ncdbhs number
                );''')
   conn.execute('delete from jbdata')
   statement="insert into jbdata values(?,?,?,?,?,?)"
   print('start DBF inserting.')
   conn.executemany(statement,data)
   conn.execute("delete from jbdata where qhdm='qhdm'")
   conn.commit()
   print('DBF insert completed.')
   conn.close()
   print('database closed.')

def valueCoupleList(Period,DivTimes):
    VCL={}
    conn=sqlite3.connect(DBPATH+'mzdata.db')
    sql='select MatchedIndex,Value from DataWarehouse where qhdm="000000000000" and Period="{Period}"'.format(Period=Period)
    cursor=conn.execute(sql)
    for item in cursor:
        if DivTimes!=1:
            VCL[item[0]]=round(item[1]/DivTimes,1)
        else:
            VCL[item[0]]=int(item[1])
    if VCL=={}:
        print("Data not found in period {Period}".format(Period=Period))
    return VCL

def calcChain(curPeriod,prePeriod):
    chain={}
    curData=valueCoupleList(curPeriod,1)
    preData=valueCoupleList(prePeriod,1)
    for key in curData:
        chain[key+'_H']=round((curData[key]-preData[key])/preData[key]*100,1)
    return chain

def calcYOY(curYear,preYear):
    YOY={}
    curData=valueCoupleList(curYear,1)
    preData=valueCoupleList(preYear,1)
    print(curData)
    for key in curData:
        YOY[key+'_T']=round((curData[key]-preData[key])/preData[key]*100,1)
    return YOY

print(calcChain('201806','201803'))

