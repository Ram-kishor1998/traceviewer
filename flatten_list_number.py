def flatten_list(number):
    new_list = []

    for num in number:
        if isinstance (num,list):
            new_list.extend(flatten_list(num))
        else:
            new_list.append(num)

    return new_list

number = [1,2,3,4,[5,6,[7,8,[9]]]]
result = flatten_list(number)
print(result)