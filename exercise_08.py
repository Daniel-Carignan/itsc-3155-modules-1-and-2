#
 
i=1
origList = []
appearOnceList = []

for x in range(10):
    userNum = int(input('Enter number '+str(i)+': '))
    origList.append(userNum)
    i+=1

print('Original List: '+str(origList))


i = 10
for i in range(10):
    if origList[i-1] != origList[i]:
        appearOnceList.append(origList[i])
        i-=1
    

print('Nums that appear once: '+str(appearOnceList))
    
