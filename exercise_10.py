#

#Take in a string from the user and split it 
# into an array of single characters. Split the 
# list of characters into a list of lists where
#  each inner list has 3 elements. Notice that 
# the last inner array may have less than 3 elements.


string=input("Enter a string: ") #this takes in the users input for the string we need to create the list
stringList=list(string) #this split the string into list so that we can mold it into a list of lists
fullnewstringlist=[] #empty list for the final list of lists


for k in range(0,len(stringList),3): #loop from 0 to length of stringList
    newstringlist=[] #empty list for the initial list holding inner list
    for i in range(0,3): #loop from 0 to 3, this is for the inner list
        if (k+i)<len(stringList): #if k+i is less than length of stringList
            newstringlist.append(stringList[k+i]) #append value of stringList : k+i index to newstringlist
    fullnewstringlist.append(newstringlist) #append newstringlist to fullnewstringlist


print(fullnewstringlist) #display fullnewstringlist



#                       SOURCES
#
#https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
#  this page showed me how to separate the string into 
# a character list using hte unpack method
#
#
#https://www.chegg.com/homework-help/questions-and-answers/10-take-string-user-split-array-single-characters-split-list-characters-list-lists-inner-l-q91316405
#  This page had the necesarry code to create the list of lists separating the string into characters
# I have copied this code but have added more comments to the code explaining what everything does. 
#
#