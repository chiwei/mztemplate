from dbfread import DBF
import time

dbfdir="./data/"
jbdbf="jb18.dbf"

csvdir="./output"
jbcsv="jb18.csv"

dbfpath=dbfdir+jbdbf
csvpath=csvdir+jbcsv

jbraw=open(csvpath,"w")
print('qhdm','sq','csdbrs','csdbhs','ncdbrs','ncdbhs',sep=',',file=jbraw)
table=DBF(dbfpath,ignore_missing_memofile=True)
begin_time=time.time()
for record in table:
   print(str(record['SYS_ZDM'])[0:12],",",str(record['SYS_ZDM'])[12:14],",",record['F_144'],\
         ",",record['F_157'],",",record['F_158'],",",record['F_170'],sep="",file=jbraw)
end_time=time.time()
print("csv created!",len(table),"items wrote down.",round(end_time-begin_time,2),"seconds elapsed.")
jbraw.close()