def find_non_repeating(s):
    for char in s:
        if s.count(char) == 1:
            return char

s = "swiss"
result = find_non_repeating(s)
print(result)