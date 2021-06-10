guess = None
value = 5
lifermaining = 5
print ("welcome to our guess game")

while lifermaining !=0:
    print(f'you life remains:{lifermaining}')
    guess = int(input("enter a number:"))
    if guess== value:
        print ('Congrats, you win')
        break
    else:
        lifermaining-=1
else:
    print("game over")