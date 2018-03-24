o=input("enter your choice:")
print(''.join([j for i,j in enumerate(o) if j not in o[:i]]))
