people= ["Elie", "Tim", "Matt"]
answer = [i[0] for i in people]
print (answer)

number = [1,2,3,4,5,6]
answer2 = [num for num in number if num % 2 == 0]
print(answer2)

number2 =[1,2,3,4] 
answer3 = [x for x in number2 if x in [3,4,5,6]]
print(answer3)


answer4 = [name[::-1].lower() for name in people ]
print(answer4)

answer5 = [y for y in range(1,101) if y % 12 == 0]
print(answer5)

word = "amazing"
answer6 = [i for i in word if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U')]
print(answer6)


#print (answer2)

