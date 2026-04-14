def no_odd_nums(nums):
    return [num for num in nums if num % 2 == 0]


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered = no_odd_nums(list)

print(list)
print(filtered)