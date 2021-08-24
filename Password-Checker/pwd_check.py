def isdigit(st):
    # Return True is st contains at least one digit
    return any (c.isdigit() for c in st)

def isupper(st): return any(c.isupper() for c in st)
def islower(st): return any(c.islower() for c in st)

def pwd_check(lst):
    pwd = []
    for w in lst:
        if (isdigit(w) and isupper(w) and islower(w) and not w.isalnum() 
            and len(w) >= 8):
            pwd.append(w)
    return pwd

lst = list(map(str, input().split()))
# We are getting multiple inputs on the same line 
# and storing them in a list
print("Good Passwords:")
for x in pwd_check(lst): print(x)
print('-'*20)