# Given a linked list of N nodes. The task is to reverse this list.
struct Node* reverseList(struct Node *head)
{
Node* prev = NULL;
Node* current = head;
Node* N = current->next;

while(current!=NULL){
N = current->next;
current->next = prev;
prev = current;
current = N;
}
head = prev;
}
