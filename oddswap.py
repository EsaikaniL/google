H=list(input())
for i in range(0,len(H)-1,2):
    H[i],H[i+1]=H[i+1],H[i]
print("".join(str(x) for x in H))
