s= "~`!@#$%^&*()_-+={}[]:>;',</?*-+"
def check(name):
    count=0
    for i in name:
        if i in s:
           count+=1
    return count          
print(check(input("Enter the String:")))
