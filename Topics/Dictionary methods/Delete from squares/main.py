
take_input = int(input())

temp_var = squares.get(take_input, 'There is no such key')
print(temp_var)

if temp_var != 'There is no such key':
    del squares[take_input]
print(squares)