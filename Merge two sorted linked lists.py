# Given two sorted linked lists consisting of N and M nodes respectively. The task is to merge both of the list (in-place) and return head of the merged list.
# Note: It is strongly recommended to do merging in-place using O(1) extra space.
Node* sortedMerge(Node* head1,   Node* head2)
{
if(head1 == NULL)
return head2;
if(head2 == NULL)
return head1;

if(head1->data < head2->data) {
head1->next = sortedMerge(head1->next,head2);
return head1;
} else {
head2->next = sortedMerge(head1,head2->next);
return head2;
}
}
