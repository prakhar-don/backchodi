import time
initial=time.time()

print("******Welcome to health management system*******")

client_list={1:"amber",2:"prakhar",3:"scofield"}
log_list={1:"Exercise",2:"Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()

print("select the client name:")
for key,value in client_list.items():
     print("PRESS",key ,"for",value,end="\n" )

client_name=int(input()) 
print("selected client:",client_list[client_name],end="\n")

print("PRESS 1 for log")
print("PRESS 2 for retrieve" )
op=int(input())

if op == 1:
        for key,value in log_list.items():
            print("PRESS",key,"for",value,end="\n")
        log_name=int(input())

        print("selected task:",log_list[log_name],end="\n") 

        f=open(client_list[client_name]+"_"+log_list[log_name]+".txt","a") 

        k='y'
        while (k !="n"):
            print("enter:",client_list[client_name],end="\n")
            mytext=input()
            f.write("["+str(getdate())+"]:" +mytext+"\n")
            k=input("ADD more? y or n:")
            continue
        f.close()
elif op == 2:
        for key,value in log_list.items():
            print("PRESS",key,"to retrieve",value,end="\n") 
        log_name=int(input())

        print(client_list[client_name],"-", log_list[log_name],"Report:",end="\n")

        f=open(client_list[client_name]+"_"+log_list[log_name]+".txt","rt")
        contents=f.readlines()
        for line in contents:
            print(line)
        f.close()
else:
        print("invalid input!!!")

print(initial)




               







