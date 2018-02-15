n=int(input("enter your number"))
rev=0
while(n>0): 
 b=n%10 
 rev=rev*10+b
 n=n//10  
print("the reverse of number is:",rev)
