n=int(input("enter your number:"))
k=int(input("enter your number:"))
while(n%k==0):
  n=n/k
if(n==1):
  print("yes")
else:
  print("no")
