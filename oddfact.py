n=int(input("enter your num:"))
a=[]
for i in range(2,n):
  if(n%i==0 and i%2!=0):
    a.append(i)
print(*a)
