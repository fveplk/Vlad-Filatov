import random
numbers = (1,2,3,4,5,6,7,8,9,10)

weights = [1,1,1,3,1,1,1,3,1,1]
random_numbers = random.choices (numbers, weights=weights, k=3) 
print (random_numbers)
