def is_power(o):
  o=o/2
  if(o==2):
    print("yes it is power of 2")
  elif(o>2):
    return is_power(o)
  else:
    print("no it is not power of 2")
o=int(input("enter your choice:"))
is_power(o)
