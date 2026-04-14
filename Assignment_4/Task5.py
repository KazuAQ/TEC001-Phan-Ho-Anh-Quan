num_list=[]

while True:
    try:
        num = int(input("Enter a number (type any else in to exit ig): "))
        num_list.append(num)
    except:
        break

def filter(nums):
    return [num for num in nums if num % 2 == 0]

filtered = filter(num_list)

print(num_list)
print(filtered)