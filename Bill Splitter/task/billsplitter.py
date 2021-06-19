# write your code here
print('Enter the number of friends joining (including you):')
friends_num = int(input())
friends_list = []

if friends_num >= 1:
    print('Enter the name of every friend (including you), each on a new line:')
    i = 1
    while i <= friends_num:
        friends_list.append(input())
        i += 1

    friends_dict = dict.fromkeys(friends_list, 0)
    print(friends_dict)

else:
    print('No one is joining for the party')


