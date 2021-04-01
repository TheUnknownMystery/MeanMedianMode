Survey = [18, 100, 'Afganisthan']

Age = Survey[0]
Country = Survey[1]
IQ = Survey[2]

if(str(Age) >= str(18)):
    print("Passed")
else:
    print("NotPassed")

if(IQ >= str(100)):
    print("Passed")
else:
    print("NotPassed")

if(Country):
    print("Passed")
