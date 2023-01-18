#DONE

allNums = []
evenNums = []
n = 1000000

for x in range(n):
    newNum = input('Enter a number or QUIT to quit: ')
    if newNum == 'QUIT':
        break
    else:
        allNums.append(newNum)

#print all numbers
print('All Nums:'+str(allNums))

for x in range(len(allNums)):
    allNums[x] = int(allNums[x]) 

i = 0
#print even numbers
for x in range(len(allNums)):
    if allNums[i] % 2 == 0:
        evenNums.append(allNums[i])
    i+=1

print('Even Nums:'+str(evenNums))



        #                       SOURCES
        #
        #https://www.geeksforgeeks.org/python-program-to-print-even-numbers-in-a-list/
        #  This page shows how to find the modulo of a number,
        # aka getting the even nums