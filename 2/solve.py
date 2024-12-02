# part 1
puzzle = open('puzzle.txt').readlines()
reports = [[int(j) for j in i.split(' ')] for i in puzzle]

safe = 0
for r in reports:
    inc = (r[1] - r[0]) > 0
    # print(r[1] - r[0], inc, (r[1] - r[0]) > 0, end = ' ')
    if abs(r[1] - r[0]) > 3 or abs(r[1] - r[0]) < 1:
        continue
    is_safe = True
    for i in range(2, len(r)):
        # print(r[i] - r[i-1], inc, (r[i] - r[i-1]) > 0, end = ' ')
        if abs(r[i] - r[i-1]) > 3 or abs(r[i] - r[i-1]) < 1 or ((r[i] - r[i-1]) > 0) != inc:
            is_safe = False
            # print(False)
            break
    if is_safe:
        safe += 1
        # print(r, True)
print(safe)

# part 2
def check(r: list):
    inc = (r[1] - r[0]) > 0
    if abs(r[1] - r[0]) > 3 or abs(r[1] - r[0]) < 1:
        return False
    is_safe = True
    for i in range(2, len(r)):
        if abs(r[i] - r[i-1]) > 3 or abs(r[i] - r[i-1]) < 1 or ((r[i] - r[i-1]) > 0) != inc:
            is_safe = False
            break
    return is_safe

safe = 0
for r in reports:
    is_safe = check(r)
    if is_safe:
        safe += 1
        continue
    else:
        for i in range(len(r)):
            r_copy = r[:i] + r[i+1:]
            print(r, r_copy)
            is_safe = check(r_copy)
            if is_safe:
                safe += 1
                break
print(safe)