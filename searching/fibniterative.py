#formulae:# F(n) = F(n-1) + F(n-2)
#iterative approach with O(n) time complexity and O(1) space complexity
#best for large n as it avoids recursion and memoization overhead

def fibonacci_sequence(n):
    sequence = []
    
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

print(fibonacci_sequence(10))