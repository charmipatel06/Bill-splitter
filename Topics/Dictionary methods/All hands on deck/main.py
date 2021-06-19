card_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
input_list = []
for _ in range(1, 7):
    input_list.append(input())


sum_value = 0
for i in input_list:
    sum_value += card_dict[i]

print(sum_value / len(input_list))