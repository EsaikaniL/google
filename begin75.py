s=input("enter your choice:")
if(len(s)%2==0):
    s=s[:int((len(s)/2))-1]+'**'+s[int(len(s)/2)+1:]
else:
    st=s[:int(len(s)/2)]+'*'+s[int(len(s)/2)+1:]
print(s)
