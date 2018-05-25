n=int(input(""))
s=[]
for i in range(0,n):
  b=int(input(""))
  s.append(b)
print(s)
m=s[:len(s)//2]
n=s[len(s)//2:]
avg=sum(m)/len(m)
av=sum(n)/len(n)
if(avg==av):
  print("yes")
else:
  print("no")

