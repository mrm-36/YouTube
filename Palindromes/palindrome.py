def iterative(st):
    n = len(st) // 2
    for i in range(n):
        if st[i] != st[len(st) - i - 1]:
            return False
    return True

def recursive(st):
    if len(st) in [0, 1]: return True
    return st[0] == st[-1] and recursive(st[1:-1])

def reverse(st):
    return st == st[::-1]

st = 'levela'
print(iterative(st))
print(recursive(st))
print(reverse(st))
