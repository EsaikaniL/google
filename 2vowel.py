v=['a','e','i','o','u','A','E','I','O','U']
h=list(input("Enter the string:"))
def vw(h):
  for i in v:
    if i in s:
      return "yes"
  return "no"
print(vw(h))
