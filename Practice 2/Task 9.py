input_string = input("Введите N быков и K семей: ")
nums = input_string.split(" ")
n = int(nums[0])
k = int(nums[1])
result = n % k
print(result)