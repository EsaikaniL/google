N=int(input("Enter ur number:"))
list1=[int(input("Enter {0} element in List1:".format(i+1))) for i in range(N)]
list2=[int(input("Enter {0} element in List2:".format(i+1))) for i in range(N)]
print(*list(set(list1)&set(list2)))
