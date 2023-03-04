with open("C:\\Users\\DELL\\OneDrive\\Documents\\python\\work.txt") as f:
    content=f.read()

with open("C:\\Users\\DELL\\OneDrive\\Documents\\python\\chal.txt") as f:
    content1=f.read()   

if content==content1:
    print("the files are same")
else:
    print("the files are not same")
      
