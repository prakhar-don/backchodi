sub=input("enter the name of subject:")
def exam(funct):
    def score():
        
        print(f"score in {sub}  exam")
        funct()
        print("i hope you got good marks")
    return score


@exam
def subject():
    
    a=int(input("enter marks:"))
    print(f"i got {a} marks in {sub}")   

subject() 


