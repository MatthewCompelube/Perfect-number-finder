import os

print(os.getcwd())

numberStorage = open("numbers.txt", "w")
numberStorage.write("Perfect Numbers")
numberStorage.write("\n")
numberStorage.write("________________")
numberStorage.write("\n")
numberToTest = 0
printInfo = 0
perfectNumbers = []

while numberToTest < 900000:
    numberToTest += 1
    total = 0
    addList =[]
    addList.clear()
    if printInfo == 1:
        print("Current Number to test is: ", numberToTest)
    for x in range(1, numberToTest):
        if (numberToTest / x).is_integer():
            addList.append(x)
            #print(x)
    for i in addList:
        total += i
        #print("total:", total)
    if total == numberToTest:
        perfectNumbers.append(numberToTest)
        print("\n")
        print("\n")
        print("PERFECT NUMBER FOUND", numberToTest)
        print("\n")
        print("\n")
        numberStorage.write(str(numberToTest))
        numberStorage.write("\n")
        

print("Closed")
numberStorage.close()
