def copy_dict(data):
    copied = data.copy()
    return copied

data = {
    "name":"ram",
    "age":27,
    "city":"delhi"
}
new_dict = copy_dict(data)
print("original_dict=",data)
print("copy_dict=",new_dict)