def draw_diamond(n):
    for i in range(n):
        print(' ' * (n - i), end = '')
        print('/', end = '')
        print('*' * 2 * i, end = '')
        print('\\', end = '') #We used 2 back slashes because one is
        # considered to be a special character
        print()
    for i in range(n):
        print(' ' * (i + 1), end = '')
        print('\\', end = '')
        print('*' * 2 * (n - i - 1), end = '')
        print('/', end = '')
        print()

# That's it
# Pause the video to check the numbers and the ranges if you want
n = int(input())
draw_diamond(n)
