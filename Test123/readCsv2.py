import csv

def ReadCsv(filename):
    path = "D:/Project_py/API_Test/test_Data/"+filename
    file = open(path,'r')
    content = csv.reader(file)
    testdata = []
    i = 0
    for row in content:
        if i == 0:
            print("这是表头")
        else:
            testdata.append(row)
        i = i + 1
    return testdata


if __name__ == '__main__':
    testdata = ReadCsv("login.csv")
    print(testdata)