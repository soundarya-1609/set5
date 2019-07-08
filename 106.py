sound,d=map(int,input().split())
list=input().split()
s1=[]
for i in list:
   if(int(i)%2!=0):
    s1.append(i)
print(s1[d-1])
