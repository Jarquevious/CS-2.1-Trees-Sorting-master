#!python

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    minimum = min(numbers)
    maximum = max(numbers)

    # TODO: Create list of counts with a slot for each number in input range
    counts = [[x, 0] for x in set(numbers)]

    # TODO: Loop over given numbers and increment each number's count
    for num in numbers:
        for i in range(0, len(counts)):
            if num == counts[i][0]:
                counts[i][1] += 1

    # TODO: Loop over counts and append that many numbers into output list
    output = []
    for count in counts:
        for _ in range(count[1]):
            output.append(count[0])
   
    return output
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
    for i in range(num_buckets+1):
        buckets.append([])

    # TODO: Loop over given numbers and place each item in appropriate bucket
    for num in numbers: 
        index = int((int((num - minimum) * 100) / numbers_range) / num_buckets)
        buckets[index].append(num)

    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    
    for bucket in buckets:
        for i in range(1, len(bucket)):
            j = i - 1
            num = bucket[i]
            while j >= 0:
                if bucket[i] < bucket[j]:
                    bucket[j+1] = bucket[j]
                    bucket[j] = num
                    j -= 1
                else:
                    break
    # for bucket in buckets:
    #     for i in range(1, len(buckets)):
    #         # Comparison operator 
    #         while buckets[i-1] > buckets[i] and i > 0:
    #             # Swap items 
    #             buckets[i], buckets[i-1] = buckets[i-1], buckets[i]
    #             # Continue looping over items
    #             i-=1

    return buckets

    # TODO: Loop over buckets and append each bucket's numbers into output list
    output = []
    for bucket in buckets:
        for num in bucket:
            output.append(num)

    return output
    # FIXME: Improve this to mutate input instead of creating new output list


numbers=[10,3,6,2,8, 100, 4,56,2345,576,3,6,3472,7,3,2,78,93,76,23,456,7,3,56,23, 29,57]
print(bucket_sort(numbers, num_buckets=10))
print('')
print(counting_sort(numbers))
