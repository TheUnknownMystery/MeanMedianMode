import csv

# Reading File Data
CSV_File_OBJ = open('Mean,Median,Mode\SOCR-HeightWeight.csv')
Reader = csv.reader(CSV_File_OBJ)
  
# Deleting The Title ans storing it in a list
All_CSV_Data_Title = list(Reader)
All_CSV_Data_Title.pop(0)

# Creating a List to later store all the height Data
All_Weight = []

#Finding/Getting the weight inside a list
for i in range(len(All_CSV_Data_Title)):

    # Getting The Weight and stoaring it in All_Weights
    Weights = All_CSV_Data_Title[i][1]
    All_Weight.append(float(Weights))

Total = 0

# Adding(Sum)
for x in All_Weight:
    Total = Total + float(x)

# Length of Weights...
Length_Of_Weights = len(All_Weight)
Mean = Total % Length_Of_Weights

print('Median(Average)' + '-> ' + str(Mean))
