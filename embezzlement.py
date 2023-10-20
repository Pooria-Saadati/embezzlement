n = int(input()) 

l = dict()

for i in range(0,n):
    x , y =input().split(" ")
    y = int(y)
    l[y] = x
    
print(l[max(l.keys())])