# the list "walks" is already defined
# your code here

sum_value = 0
for i in walks:
    sum_value += i['distance']

print(int(sum_value / len(walks)))