import os
import sqlite3
import csv

def createConn(dbName):
    if os.path.exists(dbName+'.db'):
        print('database exists.')
    else:
        conn=sqlite3.connect(dbName+'.db')
        print('database '+dbName+' created!')
        return dbName+'.db'

def wrapperSelector(indexName,SQ):
    conn=sqlite3.connect("cmder.db")
    sql='select {indexName} from jbdata where SQ="{SQ}" and qhdm="000000000000"'.format(indexName=indexName,SQ=SQ)
    cursor=conn.execute(sql)
    for row in cursor:
        pass
    print(indexName+"`s value is "+str(row[0]))
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
print(wrapperSelector("ncdbhs","06"))
#loadfromCSV("outputjb18.csv")
