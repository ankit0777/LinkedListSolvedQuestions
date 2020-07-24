# Given a Linked List of integers, write a function to modify the linked list such that all even numbers appear before all the odd numbers in the modified linked list. Also, keep the order of even and odd numbers same.
t=int(input())
while(t):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=[]
    l3=[]
    for i in l1:
        if(i%2==0):
            l2.append(i)
        else:
            l3.append(i)
    l4=[]
    l4= l2 + l3
    for i in l4:
        print(i, end=" ")
    print('\t')
    t=t-1
