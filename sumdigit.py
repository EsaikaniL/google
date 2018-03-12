n=int(input("Enter a number:"))
t=0
while(n>0):
  g=n%10
  t=t+g
  n=n//10
print("The total sum of digits is:",t)
