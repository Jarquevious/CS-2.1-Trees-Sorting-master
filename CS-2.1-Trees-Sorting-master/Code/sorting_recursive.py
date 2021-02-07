#!python
def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list

    # Begin with an empty list. 
    sorted_list = []
    
    # Base Cases

    # If both list are empty.
    if not items1 and not items2:
        return sorted_list

    # If items1 has items and items2 does not. 
    if items1 and not items2:
        return sorted_list + item

    # If item1 doesn't have items and items2 does. 
    if not items1 and items2:
        return sorted_list + items2

    # If both contain items
    if items1 and items2:
      
      # Check if item1 at index 0 is lesser than or equal to 
      # items2 index zero. If true add smallest item to sorted_list.
        if items1[0] <= items2[0]:
             sorted_list.append(items1[0])

            # Recursive call on the items1 index 1 until end of the list. 
             sorted_list = sorted_list + merge(items1[1:], items2)

        # Add the smallest item from item items2 to sorted_list.
        if items1[0] > items2[0]:
            sorted_list.append(items2[0])

            # Items2 at index 0 is now apart of new list.
            sorted_list = sorted_list + merge(items1, items2[1:])
    
    # Return newly sorted list as end result.
    return sorted_list

items1 = [4,5,6,7,8,9]
items2 = [23,24,25,26,27,28]
new_list=merge(items1, items2)
print(new_list)

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case) 
    # TODO: Split items list into approximately equal halves  
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order





def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
