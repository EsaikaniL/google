p='paper'
r='rock'
s='scissor'
user1,user2=input().split(" ")
if(user1=='p' and user2=='r'):
  print('p wins')
elif(user1=='p' and user2=='s'):
  print('s wins')
elif(user1=='r' and user2=='p'):
  print('p wins')
elif(user1=='r' and user2=='s'):
  print('r wins')
elif(user1=='s' and user2=='p'):
  print('s wins')
elif(user1=='s' and user2=='r'):
  print('r wins')
else:
  print("invalid")
