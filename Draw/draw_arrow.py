def draw_arrow(n):
    for i in range(n):
        for _ in range(n - i - 1):
            print('', end = ' ')
        for _ in range(2*i + 1):
            print('*', end = '')
        print()

n = int(input())
draw_arrow(n)