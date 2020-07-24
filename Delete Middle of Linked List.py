# Given a singly linked list, delete middle of the linked list. For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5.
def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist

    '''
    temp1=head
    temp2=head
    temp3=head
    while(temp2 and temp2.next):
        temp1=temp1.next
        temp2=temp2.next.next
    while(temp3.next != temp1):
        temp3=temp3.next
    temp3.next=temp1.next
    temp1.next=None
    return head
    #code here
