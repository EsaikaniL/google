n=int(input("Enter a number"))
sum1=0
a=n 
while n!=0:
	rem=n%10
	sum1=sum1*10+rem
	n=n/10
if(sum1==a):
	print (a,"is palindrome")
else:
	print (a,"is not palindrome")
