#[4] WORD shuffle using string manipulation

st=input("Enter String here:-->")

f=st[:6]
s=st[6:12]
t=st[12:]

f2=f[:2]
f3=f[2]
f4=f[3:5]
f5=f[-1]

t2=t[:2]
t3=t[-1]

st=f2+f3+f4+f5+s+t2+t3
after=t2+f2+f4+s+t3+f5+f3

print("Before Manipulation:",st)
print("After manipulation:",after)


