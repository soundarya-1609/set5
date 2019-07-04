chos=list(input())
cha=[]
for i in chos:
  if(i not in cha):
    cha.append(i)
if(chos==cha):
  print("Yes")
else:
  print("No")
