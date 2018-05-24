n,k=map(int,input("enter your values:").split(' '))
l=list(map(int,input("enter your values:").split(' ')))
s=[]
for x in l:
  if(x%2!=0):
    s.append(x)
print(s[k-1])
