scores = [
    [85, 72, 90, 65, 78],
    [50, 42, 61, 55, 48],
    [92, 88, 95, 91, 89],
    [60, 75, 80, 58, 70]
]

def pass_count(data, limit):
    res = []
    for row in data:
        c = 0
        for x in row:
            if x >= limit:
                c = c + 1
        res.append(c)
    return res

def top_student(data):
    max_score = 0
    best_idx = 0
    for i in range(len(data)):
        total = 0
        for x in data[i]:
            total = total + x
        if total > max_score:
            max_score = total
            best_idx = i
    return best_idx, max_score

def sub_avg(data):
    res = []
    for j in range(len(data[0])):
        total = 0
        for i in range(len(data)):
            total = total + data[i][j]
        avg = total / len(data)
        res.append(avg)
    return res

print("Pass:", pass_count(scores, 60))
idx, score = top_student(scores)
print("Top:", idx, "Score:", score)
print("Avg:", sub_avg(scores))