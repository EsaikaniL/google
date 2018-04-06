n=input("enter ur choice:")
d=0
for i in n:
  if(int(i)%2!=0):
    d=d+int(i)
print(d)
if(d%2==0):
  print("yes")
else:
  print("no")

