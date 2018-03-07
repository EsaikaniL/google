def fib(o):
  if(o<=1):
    return(o)
  else:
    return(fib(o-1)+fib(o-2))
a=int(input("enter your number"))
for x in range(a):
  print(fib(x))
