def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    counter = {}

    max = None
    maxCount = 0

    for num in nums:
        counter[num] = counter.get(num, 0) + 1
        if counter[num] > maxCount:
            max = num
            maxCount = counter[num]

    return max

