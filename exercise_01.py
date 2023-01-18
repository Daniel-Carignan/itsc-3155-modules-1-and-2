#DONE

#100 - 90 -> A
#89 - 80  -> B
#79 - 70  -> C
#69 - 60  -> D
#>60      -> F
# Grade scale   ^

userInput = int(input("enter a grade from 0 to 100: "))

if(userInput >=90 ):
    print('Your grade is A')
elif(userInput >=80):
    print('Your grade is B')
elif(userInput >=70):
    print('Your grade is C')
elif(userInput >=60):
    print('Your grade is D')
else:
    print('Your grade is F')




    #                   Sources Page
    #https://www.geeksforgeeks.org/taking-input-in-python/
    # in this page I had learned how to cast 
    # the user input as an in instead of a string

