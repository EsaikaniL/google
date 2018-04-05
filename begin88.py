x1,y1=map(int,input("enter your choice:").split(' '))
if(x1>y1):
    great=x1
else:
    great=y1
while(True):
    if((great%x1==0) and (great%y1==0)):
        lcm=great
        break
    great=great+1
print(lcm)
