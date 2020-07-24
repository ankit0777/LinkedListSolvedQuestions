# Given a singly linked list, the task is to rearrange it in a way that all odd position nodes are together and all even positions node are together.
# Assume the first element to be at position 1 followed by second element at position 2 and so on.
def rearrangeEvenOdd(head):
    #code here
    temp1=head
    temp2=head.next
    head2=temp2
    while(temp1.next and temp2.next):
        temp1.next=temp1.next.next
        temp2.next=temp2.next.next
        if(temp1.next):
            temp1=temp1.next
        if(temp2.next):
            temp2=temp2.next
    temp1.next=head2
    return head
