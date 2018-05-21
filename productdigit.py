n=int(input("Enter a number:"))
t=1
while(n>0):
  g=n%10
  t=t*g
  n=n//10
print("The product of digits is:",t)
