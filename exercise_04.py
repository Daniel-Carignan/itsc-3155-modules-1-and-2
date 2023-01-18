#DONE

n = int(input('Enter a number: '))
list = []
i = 1

total = 0
j = 0
for x in range(n):
    newNum = input('Enter number '+str(i)+': ')
    i+=1
    list.append(newNum)
    
print('List: '+str(list))


for x in range(n):
    list[x] = int(list[x])

for x in range(n):
    total = total + list[x]

ave = total/len(list)
print('Average: '+str(ave))


    #                       SOURCES
    #https://www.digitalocean.com/community/tutorials/python-add-to-list
    #  This page shows how to add new elements to a python list
    #
    #https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
    #  This page goes over how to print a list
    #
    #https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    #  this page explains how to convert every element in the string array
    #into an int
    #
