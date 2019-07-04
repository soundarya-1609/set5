dogs=int(input())
cats=list(map(int,input().split()))
for i in range(len(cats)-1):
     if(cats[i]>cast[i+1]):
           print(i)
           break
