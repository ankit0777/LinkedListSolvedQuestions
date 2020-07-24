# Given two linked lists, your task is to complete the function makeUnion(), that returns the union of two linked lists. This union should include all the distinct elements only.
def union(head1,head2):
    #code here
    item1 = []
    temp = head1
    while(temp!=None):
        item1.append(temp.data)
        temp = temp.next
    item2 = []
    temp = head2
    while(temp!=None):
        item2.append(temp.data)
        temp = temp.next
    set1 = set(item1)
    set2 = set(item2)
    setc = set1.union(set2)
    list3 = sorted(list(setc))
    head = Node(list3[0])
    for item in list3[1:]:
        temp = head
        while(temp!=None):
            currnode = temp
            temp = temp.next
        currnode.next = Node(item)
    return head
