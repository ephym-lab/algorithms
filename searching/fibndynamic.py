#formulae:# F(n) = F(n-1) + F(n-2)
#uses memoization to store previously computed Fibonacci numbers
#time complexity: O(n) due to memoization, space complexity: O(n) for the memoization dictionary


def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

def fibonacci_sequence(n):
    return [fibonacci(i) for i in range(n)]

print(fibonacci_sequence(10))