from itertools import combinations

containers = [11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]
count = 0

for r in range(1, len(containers) + 1):
    for combination in combinations(containers, r):
        if sum(combination) == 150:
            count += 1

print(count)
