words=list(input("enter your choice:"))
for i in range(len(words )):
  if words[i].islower():
    words[i]=words[i].upper()
  else:
    words[i]=words[i].lower()
print(words)
