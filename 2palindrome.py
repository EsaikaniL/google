s=int(input("Enter a number:"))
sum1=0
a=s 
while s!=0:
	rem=s%10
	sum1=sum1*10+rem
	s=s//10
if(sum1==a):
	print (a,"is palindrome")
else:
	print (a,"is not palindrome")
