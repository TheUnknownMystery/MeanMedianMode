import csv
from collections import Counter

file_path = 'Mean,Median,Mode\SOCR-HeightWeight.csv'
File_OBJ = open(file_path)

CSV_FILE_Reader = csv.reader(File_OBJ)

All_CSV_Data = list(CSV_FILE_Reader)
All_CSV_Data.pop(0)

All_Heights = []

for i in range(len(All_CSV_Data)):
    Heights = All_CSV_Data[i][1]
    All_Heights.append(float(Heights))

Data = Counter(All_Heights)

Mode_Data = {

    '50-60': 0,
    "60-70": 0,
    "70-80": 0

}

for height, occurrence in Data.items():
    if 50 < float(height) < 60:
        Mode_Data["50-60"] = Mode_Data["50-60"]+occurrence
    elif 60 < float(height) < 70:
        Mode_Data["60-70"] = Mode_Data["60-70"]+occurrence
    elif 70 < float(height) < 80:
        Mode_Data["70-80"] = Mode_Data["70-80"]+occurrence

mode_Range, mode_occurrence = 0, 0

for range, occurrence in Mode_Data.items():
    if occurrence > mode_occurrence:
        mode_Range, mode_occurrence = [
            int(range.split("-")[0]), int(range.split("-")[1])], occurrence

mode = float((mode_Range[0]+mode_Range[1])/2)
print(mode)