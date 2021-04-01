Input = str(input("Please enter file name or file path"))

def CountLinesOfAFile(FilePath):
    File_Obj = open(FilePath)
    Lines = File_Obj.readlines()
    Length = 0

    for words in Lines:
        SplitedWords = words.split()
        Length = Length + len(SplitedWords)

    print(Length)

CountLinesOfAFile(Input)