# part 1
puzzle = open('puzzle.txt').readlines()
l1, l2 = [], []
for line in puzzle:
    l = line.split('   ')
    l1.append(int(l[0]))
    l2.append(int(l[1]))
l1 = sorted(l1)
l2 = sorted(l2)
diff = 0
for i, j in zip(l1, l2):
    diff += abs(j-i)
print(diff)

# part 2
sim = 0
for i in l2:
    count = 0
    for j in l1:
        if i == j:
            count += 1
    sim += i * count
print(sim)