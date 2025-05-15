input_str = input("Nhap X , Y :")
dimesions = [int(x) for x in input_str.split(",")]
rowNumber = dimesions[0]
columnNumber = dimesions[1]
multilist = [[0 for col in range(columnNumber)] for row in range(rowNumber)]
for i in range(rowNumber):
    for j in range(columnNumber):
        multilist[i][j] = i * j
print(multilist)