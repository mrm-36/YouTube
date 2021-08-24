def draw_grid(n, m):
    for i in range(m):
        for j in range(n):
            x = i + (m * j)
            print(x, end = ' ')
        print()

n, m = int(input()), int(input())
draw_grid(n, m)