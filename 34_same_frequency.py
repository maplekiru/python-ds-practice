def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    str1 = str(num1)
    str2 = str(num2)

    count1 = {}
    count2 = {}

    for num in str1:
        count1[num] = count1.get(num,0) + 1
    
    for num in str2:
        count2[num] = count2.get(num,0) + 1
    
    return count1 ==  count2