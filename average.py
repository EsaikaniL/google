k=int(input("enter your num:"))
l=[]
for i in range(k):
  a=int(input("enter your num:"))
  l.append(a)
  print(l)
total=sum(l)
print(total)
avg=total/k
print("avg is",avg)

