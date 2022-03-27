def factorial(num):
    '''
        Function for factorial n! of a non-negative integer
        Args:
            n (int) - number for factorial n! 
        Return:
            (int) factorial n!

        Time Complexity - O(n)
    '''
    if num == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial*i
        return factorial
