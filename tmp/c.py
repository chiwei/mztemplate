from dbfread import DBF
import csv
ff=open('123.csv','w')
table = DBF('t205.dbf',load=True,ignore_missing_memofile=True,encoding='gbk')
for record in range(0,len(table)):
   # print(record+1,",",table.records[record]['F1_1'],",",table.records[record]['F1_5'],",",table.records[record]['F1_6'],sep='',file=ff)
    print(record+1,table.records[record]['F1_1'],table.records[record]['F1_3'],table.records[record]['F1_4'],table.records[record]['F1_7'])
