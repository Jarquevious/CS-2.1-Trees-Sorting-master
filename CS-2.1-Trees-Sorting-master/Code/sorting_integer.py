#!python

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    ##################################################################
    #                           Step 1:
    # TODO: Find range of given numbers (minimum and maximum values)
    ##################################################################
    
    minimum = min(numbers)
    maximum = max(numbers)
    numbers_range = maximum - minimum
    # print(numbers_range), print(minimum), print(maximum)

    ##################################################################################
    #                           Step 2:
    # TODO: Create list of buckets to store numbers in subranges of input range
    ##################################################################################
    buckets = []
    for bucket in buckets:
        buckets.append[[]]

    # TODO: Loop over given numbers and place each item in appropriate bucket
    for num in numbers: 
        index = int((int((num - minimum) * 100) / numbers_range) / num_buckets)
        buckets[index].append(num)

    # TODO: Sort each bucket using any sorting algorithm (recursive or another)


    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


numbers=[10,3,6,2,8]
bucket_sort(numbers, num_buckets=10)
