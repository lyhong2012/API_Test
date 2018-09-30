import csv
path = r"D:\Project_py\API_Test\test_Data\testdate.csv"
file = open(path,"r")
content = csv.reader(file)
for row in content:
    print(row)