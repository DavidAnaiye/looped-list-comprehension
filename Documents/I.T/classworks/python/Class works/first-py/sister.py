#!c:Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
msg= input('say something:')
i = 1
while  msg != "stop copying me":
    if i<3:
        msg = input(f"{msg}\n")
        i = i + 1
    else:
        print('You lost')
        break
else:
    print("UGH FINE YOU WIN, BROTHER")