pk1,pk2=map(int,input().split())
maxima=max(pk1,pk2)
while(1):
   if(maxima%pk1==0 and maxima%pk2==0):
         print(maxima)
         break
