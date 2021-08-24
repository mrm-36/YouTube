def draw_triangle(n):
    for i in range(n):
        for j in range(i):
            print('*', end = ' ')
        for j in range(n - i):
            print(' ', end = ' ')
        print()

n = int(input())
draw_triangle(n)
# That's it 
# Notice the two Triangles, one in points and one in stars
# To make it clearer we will remove one of them