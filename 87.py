ws1,ws2=map(int,input().split())
n=1
while(n<=ws1 and n<=ws2):
   if(ws1%n==0 and ws2%n==0):
      gcd=n
   n=n+1
print(gcd)
