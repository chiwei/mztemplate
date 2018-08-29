import csv

def csvSpilt(frmFile,toFile):
    header=[]
    convertFile=open(toFile,"w")
    with open(frmFile,'r') as fromFile:
        print(fromFile)
        print('phase 1')
        reader=csv.reader(fromFile)
        for row in reader:
            for i in range(0,len(row)):
                header.append(row[i])
            break
        print(header)
        for row in reader:
            for i in range(3,len(row)):
                print(row[0],row[1],row[2],row[i],header[i],sep=',',file=convertFile)
    fromFile.close()
    convertFile.close()
    return

f='../output/headder.csv'
t='./tester.csv'
#csvSpilt(f,t)
if __name__=='builtins':
    csvSpilt(f,t)

