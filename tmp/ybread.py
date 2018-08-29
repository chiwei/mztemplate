from dbfread import DBF
ybraw=open('./output/yb18.csv',"w")
table = DBF('./DBF/yb.dbf',load=True,ignore_missing_memofile=True)
print('qhdm','sq','csdbrs','csdbhs','ncdbrs','ncdbhs',sep=',',file=ybraw)
for record in range(0,len(table)):
#    print(table.records[record]['SYS_ZDM'][0:12],',',table.records[record]['SYS_ZDM'][12:14])
    print(table.records[record]['SYS_ZDM'][0:12],',',table.records[record]['SYS_ZDM'][12:14],",",table.records[record]['YZH21110'],\
          ",",table.records[record]['YZH21120'],",",table.records[record]['YZH21210'],",",table.records[record]['YZH21220'],\
          sep="",file=ybraw)
ybraw.close()
