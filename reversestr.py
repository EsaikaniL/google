def reverse(k):
  str = ""
  for x in k:
    str = x + str
  return str
k =input("enter your string")
print (k)
print (reverse(k))
