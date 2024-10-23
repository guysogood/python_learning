student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_score = sum(student_scores)
print(total_score)

sum = 0
for score in student_scores:
    sum += score
print(sum)

print(max(student_scores))
max_score = 0
for score_max in student_scores:
    if score_max > max_score:
        max_score = score_max
print(max_score)

print(min(student_scores))
min_score = 199
for score_min in student_scores:
    if score_min < min_score:
        min_score = score_min
print(min_score)
