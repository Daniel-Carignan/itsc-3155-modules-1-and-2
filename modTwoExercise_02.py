userString = input("Enter a string: ") #we get the string from the user

upper = "" #we distinguish upper from lower case
lower = "" #we distinguish lower from upper case

for x in userString: #for loop to iterate through the string the user entered
    if x.isupper():
        upper += x #if "x" we add whatever character "x" 
                     #currently is x to the "upper" string

    elif x.islower(): #if "x" is lowercase then we add the 
        lower += x    #character that "x" is currently sitting on to 
                        #the "lower" string
        

result = lower + upper #we merge both the "upper" and "lower" strings
                       #we created from the above loop to the new "result"
                       #variable

print(result) #print out the final string, which should be all
              #the lowercase letters in the front and uppercase in the back





#                       SOURCES
#
#https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
#  this page explains the use of the "isupper" and "islower" methods.
#this allowed me to get a better understanding of what they are and how they should
#be used.
#
#https://www.educative.io/answers/how-to-concatenate-strings-in-python
#  this page showed me how to concatenate two different string into one
#using the "+" operator. 
#
#https://www.chegg.com/homework-help/questions-and-answers/python-write-script-takes-string-user-print-string-lower-case-letters-shifted-front-spaces-q91350451
#  this page had most of the code I have written here. I learned that I can add 
#characters to a string variable by simply making the variable an empty string
#I added as much commenting as I could to show that I understand what the 
#code does and how everything functions.
#
#
#
