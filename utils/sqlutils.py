import pymysql as MySQLdb
import sys
import configparser
import pandas

DBPATH='../DBs/'
class getDB:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('../config/db.conf')
        self.host = config['DATABASE']['host']
        self.db = config['DATABASE']['db']
        self.user = config['DATABASE']['user']
        self.passwd = config['DATABASE']['passwd']
        self.charset = config['DATABASE']['charset']
    def get_conn(self):
        try:
            conn = MySQLdb.connect(host=self.host,db=self.db,user=self.user,passwd=self.passwd,charset=self.charset)
            print('Connect Success')
            return conn
        except Exception as e:
            print('%s',e)
            sys.exit()

def wrapperSelector(MatchedIndex,Period,qhdm):
    conn = getDB()
    cursor = conn.get_conn().cursor()
    sql = 'select Value from DataWarehouse where Period="{Period}" \
        and qhdm="{qhdm}" and MatchedIndex="{MatchedIndex}"'.format(MatchedIndex=MatchedIndex,Period=Period,qhdm=qhdm)
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return result[0]


print(wrapperSelector('ZHN_RGN','201712','000000000000'))
def valueCoupleList(Period):
    VCL = {}
    conn = getDB()
    sql='select MatchedIndex,Value from DataWarehouse where qhdm="000000000000" and Period="{Period}"'.format(Period=Period)
    cursor=conn.get_conn().cursor()
    cursor.execute(sql)
    for item in cursor:
            print(item)
            VCL[item[0]]=item[1]
    if VCL=={}:
        print("Data not found in period {Period}".format(Period=Period))
    return VCL

def calcChain(curPeriod,prePeriod):
    chain={}
    curData=valueCoupleList(curPeriod)
    preData=valueCoupleList(prePeriod)
    for key in curData:
        chain[key+'_H']=round((curData[key]-preData[key])/preData[key]*100,1)
    return chain

def calcYOY(curYear,preYear):
    YOY={}
    curData=valueCoupleList(curYear)
    preData=valueCoupleList(preYear)
    print(curData)
    for key in curData:
        if preData[key]!=0:
            YOY[key+'_T']=round((curData[key]-preData[key])/preData[key]*100,1)
    return YOY

print(calcChain('201806','201803'))

