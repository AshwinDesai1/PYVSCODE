#11 No is prime or not

n=int(input("Enter no : "))
c=0
if n>1:
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print("No is prime")
    else :
        print("No is not prime")
else :
    print("No is not prime")