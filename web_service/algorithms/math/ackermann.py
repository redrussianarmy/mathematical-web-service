def ackermann(m, n):
    '''
        Ackermann Function
        Args:
            m (int) - Ackermann value 
            n (int) - Ackermann value
        Return:
            (int) 

        Time Complexity -  O(mA(m, n))
    '''
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
