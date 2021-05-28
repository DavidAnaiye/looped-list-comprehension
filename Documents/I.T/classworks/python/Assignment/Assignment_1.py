names = ['john', 'jacob', 'anabel', 'jonathan', 'jack', 'tabita', 'winifred', 'jalang']
#FOR NAMES THAT START WITH 'j'
for i in names:
    if i .startswith('j'):
        i == True
        print('its {} that {} begins with a "j"'.format(True, i),'\n')

    else:
        i == False
        print('its {} that {} begins with a "j"'.format(False, i),'\n')
print('__________________________________________________________________________________','\n')
    
# FOR LONGEST WORD
print ('The longest Word is {}'.format(max(names, key=len)))
print('__________________________________________________________________________________','\n')  
# FOR SORT AND INDEX
names.sort()
for idx, val in enumerate(names):
    print('{} has an index of {}'.format(val,idx),'\n')

print('__________________________________________________________________________________','\n') 

# FOR LENGHT OF WORDS
for i in names:
    print('{} = {}'.format(i,len(i),),'\n')
print('__________________________________________________________________________________','\n') 

# FOR LENGHT OF LIST
print('The Lenght of the list is {}'.format(len(names)),'\n')
print('__________________________________________________________________________________','\n')

# FOR EVEN AND ODD NUMBERS
for i in names:
    if len(i)%2==0:
        print('{} is Even'.format(i),'\n')
    else:
        print('{} is Odd'.format(i),'\n')
#end