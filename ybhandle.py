import csv

filename='./output/jb18.csv'
with open(filename) as f:
    reader=csv.reader(f)
    #print(list(reader))
    for row in reader:
        print(reader.line_num,row)