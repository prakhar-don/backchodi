import random
def gameWin(comp,you):
    if (comp==you):
        return None
    elif (comp=='s'):
        if (you=='w'):
            return False
        elif(you=='g'):
            return True   
    elif (comp=='w'):
        if(you=='s'):
            return True
        elif(you=='g'):
            return False
    elif (comp=='g'):
        if (you=='w'):
            return True
        elif (you=='s'):
            return False

print("now computer turn snake(s),water(w),gun(g)")

randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g' 

you=input("enter your choice s,w or g:\t") 
a= gameWin(comp,you) 

print(f"Computer choose {comp}")


if a==None:
    print("Game is tie")
elif a==True:
    print("You win the game") 
else:
    print("You lost the game")       








