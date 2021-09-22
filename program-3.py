a=int(input("enter number for a:"))
if(a%2==0):
    a-=1
    for j in range(1,a*2):
        if(j%2!=0):
            print(j,end=",")
else:

    for j in range(1,a*2):
        if(j%2!=0):
            print(j,end=",")
