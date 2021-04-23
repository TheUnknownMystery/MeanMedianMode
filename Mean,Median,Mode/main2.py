import csv

#Reading and storing file object...
#Path for the csv file....
File_Path = 'Mean,Median,Mode\SOCR-HeightWeight.csv'
File_OBJ = open(File_Path)
CSV_Reader = csv.reader(File_OBJ)

#Storing the Data in a list Called All_CSV_Data
All_CSV_Data = list(CSV_Reader)
All_CSV_Data.pop(0)

Heights = []

for i in range(len(All_CSV_Data)):
    All_Heights = All_CSV_Data[i][1]
    Heights.append(float(All_Heights))

#Getting the length of the arry 
HeightLength = len(Heights)
Sorted_Height = Heights.sort()

if(HeightLength % 2 == 0):
    median1 = float(Heights[HeightLength//2])
    print('FirstMedian-> ' + str(median1))

    median2 = float(Heights[(HeightLength // 2) + 1])
    print('SecondMedian-> ' + str(median2))

    median = (median1 + median2)/2
else:
    median = float(Heights[(HeightLength//2)+1])

#Finaly mean(printed)
print('medain' + '-> ' + str(median))