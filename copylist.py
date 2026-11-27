def copy_list(number):
    copied = number.copy()
    return copied

number = [1,2,3,4,5,6,7]
new_list = copy_list(number)
print("original_list=", number)
print("copy_list=",new_list)