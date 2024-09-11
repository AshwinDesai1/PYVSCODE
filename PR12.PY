#find birth month
d={"Ashwin":"12/02/04","Jignesh":"30/03/03","Manish":"10/05/03","Nitesh":"20/11/04","Tanvi":"28/09/96"}
c=1
for i in d.keys():
    print(str(c)+"."+i)
    c+=1

n=int(input("Choose No for find student Birth month : "))
search="null"
if n==1:
    search="Ashwin"
elif n==2:
    search="Jignesh"
elif n==3:
    search="Manish"
elif n==4:
    search="Nitesh"
elif n==5:
    search="Tanvi"
else:
    print("Please enter correct student no !...")

if search !="null":    
   m={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"Octomber","11":"November","12":"December"}
   searchMonth=""
   if "Ashwin" in search:
     searchMonth=d["Ashwin"][3:5]
   elif "Jignesh" in search:
     searchMonth=d["Jignesh"][3:5]
   elif "Manish" in search:
     searchMonth=d["Manish"][3:5]
   elif "Nitesh" in search:
     searchMonth=d["Nitesh"][3:5]
   else:
     searchMonth=d["Tanvi"][3:5]
        
   for i in m.keys():
      if searchMonth in i:
            print(m[i])