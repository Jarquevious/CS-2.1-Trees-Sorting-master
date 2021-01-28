#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
     
    isSort = False
    while isSort == True:
        for i in range(len(items) - 1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
    print("Array is Bubble Sorted")

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
#find lowest num in list compare to index 1; swap

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    
    for i in range(1, len(items)):

        while items[i-1] > items[i] and i > 0:
            items[i], items[i-1] = items[i-1], items[i]
            i-=1

    return items
            


        
        
        
        



####Test Code for bubble sort###
# Array for items
items = [56,34,24,14,10,4,6,3]
#Call the bubble 
bubble_sort(items)
# Print Statement to illustrate complete sorted array
print(items)


###Test Code for insert###
items=[376,2,6573,67,9,4,7,94,65,56745]
print('')
print('Array is Insertion Sorted')
insertion_sort(items)
print(insertion_sort(items))