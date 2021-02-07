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


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case). 
    if len(items) > 1:
         # TODO: Split items list into approximately equal halves.
        mid = len(items)//2
        left_list = items[:mid]
        right_list = items[mid:]

        # TODO: Sort each half by recursively calling merge sort.
        merge_sort(left_list)
        merge_sort(right_list)

        # TODO: Merge sorted halves into one list in sorted order
    
        # Create indexes for looping.
        l = r = i = 0

        # Create new variables equal to the length of both left and right list.
        left_list_length = len(left_list)
        right_list_length = len(right_list)
    
        # Loop through both list starting at index 0 until the list end simultaneously. 
        while l < left_list_length and r < right_list_length:
        
            # Set conditional if index in left list is smaller than right list index
            if left_list[l] < right_list[r]:
           
                # Set items[i] as left left list index
                items[i] = left_list[l]
                
                # Move to the next index after each loop
                l += 1
        
            # Set a conditional for items[i] if the condition above is not true
            else:
                items[i] = right_list[r]
                # Move to next index and go through same process.
                r += 1
            i += 1

        # Loop through left list from index 0 to the end of the list.
        while l < left_list_length:
            # Set items[i] as left list l
            items[i] = left_list[l]
            # Iterate to the next index and go through the same process. 
            l += 1
            i += 1
    
        # Loop though right list from index 0 until last index. 
        while r < right_list_length:
            # Set items[i] for each index represented by r.
            items[i] = right_list[r]
            # Iterate through each index.
            r += 1
            i += 1

    # Return items in a sorted order.
    return items





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


items1 = [4,5,6,7,8,9]
items2 = [23,24,25,26,27,28]
new_list=merge(items1, items2)
print('Merge newly sorted list: ')
print(new_list)


items = [45,2,6,8,3,27,55,34,8,1,56,67,234]
print('')
print('Merge Sorted newly sorted list: ')
new = merge_sort(items)
print(new)
