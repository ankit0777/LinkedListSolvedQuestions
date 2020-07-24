# Given two linked list of size N1 and N2 respectively of distinct elements, your task is to complete the function countPairs(), which returns the count of all pairs from both lists whose sum is equal to the given value X.
def countPair(h1,h2,n1,n2,x):
    '''
    h1:  head of linkedList 1
    h2:  head of linkedList 2
    n1:  len of  linkedList 1
    n2:   len of linkedList 1
    X:   given sum
    '''
    count = 0

    #struct Node p1, p2

    # traverse the 1st linked list
    p1 = h1
    for i in range(n1):

        p2 = h2
        for j in range(n2):

            # if sum of pair is equal to 'x'
            # increment count
            if ((p1.data + p2.data) == x):
                count+=1
            p2 = p2.next

        p1 = p1.next
    # required count of pairs
    return count 
