s=input("Enter the string:")
c=('a','e','i','o','u')
a=[]
for i in s:
  if i in c:
    continue
  else:
    a.append(i)
b=a[::-1]
print(''.join(b))
