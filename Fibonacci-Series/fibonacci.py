def iterative(n):
    a1 = 0
    a2 = 1
    ans = 0
    for _ in range(n - 1):
        ans = a1 + a2
        a1, a2 = a2, ans
        # Switching the varibles
    return ans

def recursive(n):
    if n == 0: return 0
    if n == 1: return 1
    return recursive(n-1) + recursive(n-2)
# Look at how easy the recursive method is, compared to the iterative one

print(iterative(20))
print(recursive(20))