as,ds,n=map(int,input().split())
current=0
for i in range(0,n):
   current=current+as
   as=as+ds
print(current)
