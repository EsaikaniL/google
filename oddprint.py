a=int(input("Enter number:"))
b=''
while(a!=0):
	k=a%10
	if(k%2!=0):
		b=b+' '+str(k)
	a=a//10
print(b[::-1])
