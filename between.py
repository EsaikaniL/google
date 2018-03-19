x=int(input("Enter Value:"))
a,b=map(int,input("Enter Two values").split(' '))
if x in range(a+1,b):
  print("yes")
else:
  print("no")
