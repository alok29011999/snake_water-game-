# snake water gun project

import random


def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == "w":
            return False
        elif you =='g':
            return True
    elif comp =='w':
        if you == 's':
            return True
        elif you =="g":
            return False
    elif comp == 'g':
        if you =="w":
            return True
        elif you =='s':
            return False




randomNo = random.randint(1,3)
# comp = None
comp = None
if randomNo ==1:
    comp = 's'

elif randomNo == 2:
    comp ="w"

elif randomNo ==3:
    comp = 'g'

# print(comp)
you = input("enter snake(s) and water(w) and gun(g)")

a = gamewin(comp, you)
if a==None:
    print(f"match is tie")
elif a:
    print("you win")
else:
    print(f"computer win ")

# print(random)
