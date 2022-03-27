def fibonacci(n):
    '''
        Function for nth fibonacci number - Dynamic Programming 
        Args:
            n - number for nth fibonacci number (int)
        Return:
            nth fibonacci number (int)

        Time Complexity - O(n)
    '''

    fib_list = [0, 1]
    for i in range(2, n+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[n]
