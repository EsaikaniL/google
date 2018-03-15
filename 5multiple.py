p=int(input("Enter Value"))
l=[]
for i in range(1,6,1):
    l.append(p*i)
print(" ".join(str(x) for x in l))
