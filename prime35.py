h=int(input("Enter a number "))
for i in range(2,h):
  if((h%i)==0):
    print('no')      
    break
else:
  print('yes')
