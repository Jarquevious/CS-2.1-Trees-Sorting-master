#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    # Use Boolean to check to see if size of array is 0. 
    if len(items) == 0:
        return True
    
    item_to_sort = items[0]
    # Loop over each item from index 1
    for i in range(1, len(items)): #o(n)
        # Comparison operator to check values at each item
        if item_to_sort > items[i]:
            # Signify the output to user if false         
            return False
        # Reassigning the items[i] for each item to for comparison
        item_to_sort = items[i]
    # Signify the output to user if false
    return True



def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    num_items = len(items)
    # Loop over items from 0 to length of items
    for i in range(num_items-1):                        
        # Loop over items from 0 to i minus 1 for comparing
        for j in range(0, num_items-i-1):
            # Check if second to last item is greater than last item
            if items[j] > items[j+1]:
                # Swap items 
                (items[j], items[j+1]) = (items[j+1], items[j])
    # Return items at end of for loop           
    return items

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    
    # Loop over each item from 0 to items[-1]
    for i in range(0, len(items) - 1):
        # Assignn i as minimum value
        minimum_value = i

        # Loop over items from right of i to end of list
        for j in range(i + 1, len(items)):
            # Compare items[j] to the minimum value
            if items[j] < items[minimum_value]:
                # If true, assign minimum value to j
                minimum_value = j
        # If item is not i
        if minimum_value != i:
            # Swap items if true
            items[minimum_value], items[i] = items[i], items[minimum_value]

    return items

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    
    # Loop over the list from index 1.
    for i in range(1, len(items)):
        # Comparison operator 
        while items[i-1] > items[i] and i > 0:
            # Swap items 
            items[i], items[i-1] = items[i-1], items[i]
            # Continue looping over items
            i-=1

    return items
            

####Test Code for is_sort###
sorted_items = [5,6,7,8,9]
unsorted_items = [21, 6, 8, 7, 91, -1, 100, 34]
print('Is_Sorted:')
print(is_sorted(sorted_items))
print('Un_Sorted:')
print(is_sorted(unsorted_items))   

        
####Test Code for bubble sort###
items = [5,8,2,4,1,6,13,25,6,20]
print('')
print("Bubble Sort:")
print(bubble_sort(items))


###Test Code for selection###
items=[5,8,2,4,1,6,13,25,6,20]
print('')
print('Selection Sort:')
print(selection_sort(items))

###Test Code for insert###
items=[376,2,6573,67,9,4,7,94,65,56745]
print('')
print('Insertion Sort:')
print(insertion_sort(items))

