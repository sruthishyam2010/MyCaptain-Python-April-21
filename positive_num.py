list1=[]
n=int(input("Enter the no of elements:"))
for i in range(0,n):
    x=int(input())
    list1.append(x)
for i in range (0,n):
    if(list1[i]>0):
        print(list1[i], end=" ")