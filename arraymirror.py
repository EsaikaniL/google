n=int(input('enter size 1:'))
a=[]
for i in range(n):
  c=int(input('enter the value:'))
  a.append(c)
  a.sort(reverse=True)
m=int(input('enter size 2:'))
b=[]
for i in range(n):
  d=int(input('enter the value:'))
  b.append(d)
if(a==b):
  print("yes")
else:
  print("no")
