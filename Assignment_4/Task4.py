num_list=[]

while True:
    try:
        num = int(input("Enter a number (type any else in to exit ig): "))
        num_list.append(num)
    except:
        break

def list_sum(num_list):
    return sum(num_list)

print(list_sum(num_list))