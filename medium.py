l=[]
n=int(input("enter the choice"))
for i in range (0,n):
  b=int(input("enter the number"))
  l.append(b)
  l.sort()
print(l[(n-1)//2])
