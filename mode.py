def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
        max_val = max(frequency.values())

        for (num, count) in frequency.items():
            if count == max_val: 
                return num 