def count_substr(main, second):
    n = len(second)
    counter = 0
    for i in range(len(main) - n + 1):
        if second == main[i : i + n]:
            counter += 1
    return counter

main = input()
second = input()
print(count_substr(main, second))