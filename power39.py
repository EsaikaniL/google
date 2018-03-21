def is_power(l):
  l=l/2
  if(l==2):
    print("yes it is power of 2")
  elif(l>2):
    return is_power(l)
  else:
    print("no it is not power of 2")
l=int(input("enter your choice:"))
is_power(l)
