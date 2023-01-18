#DONE

#two lists each containing 5 elements
#third list containing common values between the two lists

fList = []
sList = []

#first list
for x in range(5):
    newNum = input('Enter a number for the first list: ')
    fList.append(newNum)

#second list
for x in range(5):
    newNum = input('Enter a number for the second list: ')
    sList.append(newNum)

print('First List: '+str(fList))

print('Second List: '+str(sList))

cList = []
if fList[0] == sList[0]:
    cList.append(fList[0])
if fList[1] == sList[1]:
    cList.append(fList[1])
if fList[2] == sList[2]:
    cList.append(fList[2])
if fList[3] == sList[3]:
    cList.append(fList[3])
if fList[4] == sList[4]:
    cList.append(fList[4])

print('Common List: '+str(cList))
