def find_missing(number):
    n = len(number) + 1
    missing = []

    for num in range(1,n+1):
        if num not in number:
            missing.append(num)

    return missing

number = [1,2,3,4,5,6]
result = find_missing(number)
print(result)
