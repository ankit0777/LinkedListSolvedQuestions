# Given an unsorted linked list of N nodes. The task is to remove duplicate elements from this unsorted Linked List. When a value appears in multiple nodes, the node which appeared first should be kept, all others duplicates are to be removed.
def removeDuplicates(head):
    #code here
    temp1=head
    temp2=head
    l1={}
    while(temp1):
            if temp1.data not in l1:
                l1[temp1.data]=1
                temp2=temp1
                temp1=temp1.next
            else:
                temp2.next=temp1.next
                temp1=temp1.next

    return head
