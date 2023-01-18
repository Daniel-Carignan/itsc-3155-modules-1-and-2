#DONE

#Take in a row number from 1 to 5 inclusive and 
#a column number from 1 to 5. Print out a grid of 0s, 
#but in the row and column entered by the user, 
#print a 1.

rows, cols = (5, 5) #creation of size of grid

rowNum = int(input('Enter a row number form 1 to 5: ')) #user input for the row
colNum = int(input('Enter a col number from 1 to 5: ')) #user input for the col

arr = [[0 for i in range(cols)] for j in range(rows)] #this declares the array boundaries and 
                                                      #sets the array to zeros as well

arr[rowNum-1][colNum-1] = 1 #this is the coordinates the user chose
for row in arr:  #this simply loops through the grid and prints it out
    print(row)




#                       SOURCES
#
#https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
# this page explains how they created a gird in many differnet ways
#I used the one that was closest to this assignment.
#I copied most of the code with exception to the "arr[rowNum][colNum]" part




