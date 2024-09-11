#fibonacci series
n=int(input("Enter term : "))
c,v1,v2=0,0,1
while c<=n:
 print(v1)
 c+=1
 summ=v1+v2
 v1=v2
 v2=summ