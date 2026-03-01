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
#
#a=0,b=1,  a=1,b=1,  a=1,b=2,  a=2,b=3,  a=3,b=5,  a=5,b=8,  a=8,b=13,  a=13,b=21,  a=21,b=34,  a=34,b=55