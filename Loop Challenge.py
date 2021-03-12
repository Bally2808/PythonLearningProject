#1st Method#
numbers = [5, 2, 5, 2, 2]
for item in numbers:
    print('x' * item)

#2nd Method#
numbers = [5, 2, 5, 2, 2]
for item in numbers:
    output = ''
    for count in range(item) :
        output += 'x'
    print(output)