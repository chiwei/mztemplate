import csv


def csvSpilt(frmFile, toFile):
    header = [ ]
    convertFile = open(toFile, "w")
    with open(frmFile, 'r') as fromFile:
        reader = csv.reader(fromFile)
        print("Start to convert primal csv.")
        for row in reader:
            for i in range(0, len(row)):
                header.append(row[ i ])
            break
        for row in reader:
            for i in range(4, len(row)):
                print(row[ 0 ], row[ 1 ], row[ 2 ], row[ 3 ], row[ i ], header[ i ], sep=',', file=convertFile)
    print("Csv file has been converted.")
    fromFile.close()
    convertFile.close()
    return


f = '../output/result201711.csv'
t = './2017yb.csv'
# csvSpilt(f,t)
if __name__ == 'builtins':
    csvSpilt(f, t)
