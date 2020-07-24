# Given a linked list L of N nodes, sorted in ascending order based on the absolute values of its data. Sort the linked list according to the actual values.
# Ex: Input : 1 -> -2 -> -3 -> 4 -> -5
#       Output: -5 -> -3 -> -2 -> 1 -> 4
def sortList(head):
    '''
    head: head of linkedList

    Your method shouldn't print anything
    it should transform the passed linked list
    '''
    lis=[]
    global ll
    ll=LinkedList()
    while head != None:
       lis.append(int(head.data))
       head=head.next

    lis.sort()


    for i in range(len(lis)):
        ll.append(lis[i])
