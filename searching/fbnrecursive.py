#formulae:# F(n) = F(n-1) + F(n-2)
#very slow for large n due to repeated calculations
#time complexity: O(2^n)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Print full sequence up to n
n = 10
for i in range(n):
    print(fibonacci(i), end=" ")
    
