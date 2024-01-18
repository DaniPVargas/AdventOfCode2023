with open("input.txt", 'r') as fp:
    commands = fp.readline().split(',')

hash_sum = 0
for com in commands:
    hash_result = 0
    for c in com:
        hash_result += ord(c)
        hash_result = hash_result*17
        hash_result = hash_result % 256
    hash_sum += hash_result

print(hash_sum)