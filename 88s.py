lcms1,lcms2=map(int,input().split())
maxima=max(lcms1,lcms2)
while(1):
   if(maxima%lcms1==0 and maxima%lcms2==0):
          print(maxima)
          break
   maxima+=1
