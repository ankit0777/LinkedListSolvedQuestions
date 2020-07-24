# Given Pointer/Reference to the head of the linked list, the task is to Sort the given linked list using Merge Sort.
# Note: If the length of linked list is odd, then the extra node should go in the first list while splitting.
def sortedMerge(self, a, b):
    result = None

        # Base cases
    if a == None:
        return b
    if b == None:
        return a

        # pick either a or b and recur..
    if a.data <= b.data:
        result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result

    def mergeSort(self, h):

        # Base case if head is None
        if h == None or h.next == None:
            return h

        # get the middle of the list
        middle = self.getMiddle(h)
        nexttomiddle = middle.next

        # set the next of middle node to None
        middle.next = None

        # Apply mergeSort on left list
        left = self.mergeSort(h)

        # Apply mergeSort on right list
        right = self.mergeSort(nexttomiddle)

        # Merge the left and right lists
        sortedlist = self.sortedMerge(left, right)
        return sortedlist 
