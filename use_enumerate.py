my_list = ['apple', 'banana', 'cherry']

my_dict = {element:index for index, element in enumerate(my_list)}

print(my_dict)  # Output: {'apple': 0, 'banana': 1, 'cherry': 2}

s="fff"

dp = [[0]*len(s) for _ in range(len(s))]
print(dp)