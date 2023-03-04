def game():
    return 444
score=game()

with open("chutiya.txt","r") as f:
    hiScore=f.read()
    
if hiScore=='' :
    with open("chutiya.txt","w") as f:
       f.write(str(score)) 

if int(hiScore)<score:
    with open("chutiya.txt","w") as f:
        f.write(str(score))