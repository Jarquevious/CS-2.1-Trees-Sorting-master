#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    if len(items) == 0:
        return True
    
    item_to_sort = items[0]
    for i in range(1, len(items)): #o(n)
        if item_to_sort > items[i]:          
            return False
        item_to_sort = items[i]
    return True



def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    num_items = len(items)
    # loop over items from 0 to length of items
    for i in range(num_items-1):                        
        # loop over items from 0 to i minus 1 for comparing
        for j in range(0, num_items-i-1):
            # check if second to last item is greater than last item
            if items[j] > items[j+1]:
                # swapping
                (items[j], items[j+1]) = (items[j+1], items[j])
                
    return items

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    # find lowest num in list compare to index 1; swap
    for i in range(0, len(items) - 1):
        minimum_value = i

        for j in range(i + 1, len(items)):
            if items[j] < items[minimum_value]:
                minimum_value = j

        if minimum_value != i:
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
    
    # Search through the list starting at index 1.
    for i in range(1, len(items)):

        while items[i-1] > items[i] and i > 0:
            items[i], items[i-1] = items[i-1], items[i]
            i-=1

    return items
            

####Test Code for is_sort###
sorted_items = [5,6,7,8,9]
unsorted_items = [21, 6, 8, 7, 91, -1, 100, 34]
print('Is_Sorted:')
print(is_sorted(sorted_items))
print(is_sorted(unsorted_items))   
print('')
        
####Test Code for bubble sort###
# Array for items
items = [5,8,2,4,1,6,13,25,6,20]
#Call the bubble function
# Print Statement to illustrate complete sorted array
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
insertion_sort(items)
print(insertion_sort(items))

