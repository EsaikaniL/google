l=int(input("enter your num:"))
for i in range(2,l):
  if(l%i==0):
    print ('Yes')
    break
else:
  print ('No')
