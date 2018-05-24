p=int(input("enter ur values"))
l=list(map(int,input().split(' ')))
for i in range(p):
  if(l[i]>l[i+1]):
    print(i+1)
    break
