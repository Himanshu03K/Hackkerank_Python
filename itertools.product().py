# Enter your code here. Read input from STDIN. Print output to STDOUT
l=input().split( )
l1=input().split( )
for i in range(len(l)):
    l[i]=int(l[i])
for i in range(len(l1)):
    l1[i]=int(l1[i])
A=tuple(l)
B=tuple(l1)
for x in A:
    for y in B:
        print((x,y),end=' ')
