import random
start = 1
end = 3
exlude = [2]
while True:
    random_number = random.randint(start, end)
    if random_number not in exlude:
       break

print (random_number)
