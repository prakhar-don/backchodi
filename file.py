with open('twinkle.txt','r') as f:
    content=f.read()

if 'twinkle' in content:
    print("twinkle is present") 
else:
    print("twinkle not present")  