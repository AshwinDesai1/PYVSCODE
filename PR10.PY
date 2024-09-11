n=int(input("Enter no : "))
while n!=1:
    if n%2==0 :
        p=n
        n=n/2
    else :
        p=n
        n=n*3+1
    print(int(p),end=",")
print(int(p/2))
