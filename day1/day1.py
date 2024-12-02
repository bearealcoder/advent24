# prep
with open("input1.txt", "r") as f:
    left = []
    right = []
    for line in f.readlines():
        pair = line.strip().split()
        left.append(int(pair[0]))
        right.append(int(pair[1]))

# part 1

left.sort()
right.sort()
distances = 0
for i in range(len(left)):
    distances = distances + abs(left[i] - right[i])

print(distances)

# part 2
similarity = 0
for num in left:
    right_count = right.count(num) * num
    similarity += right_count

print(similarity)







