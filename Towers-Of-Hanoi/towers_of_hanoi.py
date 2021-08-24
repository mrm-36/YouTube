def towers_of_hanoi(orig, aux, dest, n):
    # if we have 1 disk, we just move it to the destination
    if n == 1: return [(orig, dest)]
    # if we have more, we use the pattern that we found previously
    return (towers_of_hanoi(orig, dest, aux, n-1)
            + towers_of_hanoi(orig, aux, dest, 1)
            + towers_of_hanoi(aux, orig, dest, n-1)
            )

print(towers_of_hanoi('A', 'B', 'C', 2))
# Let's try it with two disks

# The reason is that we always want to move the n-1 disks to the 
# auxiliary tower, then move the last disk to the destination
# And repeat the pattern