# Given a list of numbers and a number k, return whether any two numbers from
# the list add up to k.
# For example, given [10,15,3,7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

list = [10,15,3,7]
k = 17
combinations = []
result = False

for i in range(0,len(list)):
    for j in range(0,len(list)):
        number = list[i] + list[j]
        if number == k:
            result = True
            combinations.append(list[i])
            combinations.append(list[j])

print(combinations)
print(result)
