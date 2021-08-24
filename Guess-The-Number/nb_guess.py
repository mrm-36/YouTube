nb = int(input("Enter any integer between 1 and 1000: "))
x = int(0) #We will initialize our number to an invalid value of the set
    # So that we enter the loop

T = ['True', 'T', 'true', 't']
F = ['False', 'F', 'false', 'f']
# These are the acceptable answers that we will base our search on

interval = [1, 1000] #This is our search interval

if 1 <= nb <= 1000:
    while x != nb:
        x = round((interval[1] - interval[0]) / 2) + interval[0]
        
        y = input("Is your number <= to " + str(x) + ' ?')
        if y in T:
            interval[1] = x # We lowered the upper bound
        elif y in F:
            interval[0] = x # We increased the lower bound
        else:
            print('Invalid Response! Please Try Again')
else:
    print('Invalid Number!')