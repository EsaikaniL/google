v=int(input("enter your choice"))
li=[]
for i in range(2,v+1,2):
  if v%i==0:
   li.append(i)
print(" ".join (str(i) for i in li))
