i =int(input("enter your number:")) 
k =int(input("enter your number:")) 
print("before swapping", i, k);
i = i ^ k;
k = i ^ k;
i = i ^ k;
print("after swapping", i, k);
