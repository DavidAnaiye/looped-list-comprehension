Colors = ['red', 'yellow', 'green', 'blue', 'orange']
#To check color type
print(type(Colors))                            
print('____________')

#For all in upper case
for i in Colors:
    print(i.upper(),'\n')
print('____________')

#for 1st letter in upper case
for i in Colors:
    print(i.capitalize(),'\n')
print('____________')

#for each letter with number of occurance
for i in Colors:
    for j in i:
        print('{} = {}'.format(j,i.count(j)))
print('____________')

#for each word with number of occurance
for i in Colors:
    print('{} = {}'.format(i,len(i)))