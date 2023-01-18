#DONE

#Take in 5 words from the user and store them in a list. 
# Then, create a single string from the individual words, 
# separated by spaces, and print the list and resultant string.

wordList = []

for x in range(5):
    userWord = input('Enter a word: ')
    wordList.append(userWord)

print('Words: '+str(wordList))
s =' '.join(wordList)
print('One String: '+ str(s))



#                       SOURCES
#
#https://note.nkmk.me/en/python-string-concat/#:~:text=You%20can%20concatenate%20a%20list,the%20string%20method%2C%20join()%20.&text=Call%20the%20join()%20method,pass%20%5BList%20of%20strings%5D%20.&text=If%20you%20use%20an%20empty,makes%20a%20comma%2Ddelimited%20string.
#  This page shows when and where to use the '.join' method to concatenate string from a list