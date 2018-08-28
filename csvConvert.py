
file=open("./output/jb18.csv","r")
outputFile=open("./output/jbhead.csv","w")
head=[]
for item in file:
    head=item
    print(item,file=outputFile)
    break
print(head[5])
outputFile.close()
file.close()