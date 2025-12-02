input = []

with open('inputs/day2.txt', 'r') as file:
    input = file.read().strip().split(',')


def invalid_ID_sum(input):
    sum = 0
    for num_range in input:
        for num in range(int(num_range.split('-')[0]), int(num_range.split('-')[1]) + 1):
            if len(str(num))%2 != 0:
                pass
            else:
                left = str(num)[:len(str(num))//2]
                right = str(num)[len(str(num))//2:]
                sum += int(num) * (left == right)
    return sum

print(invalid_ID_sum(input))

def invalid_ID_sum2(input):
    sum = 0
    for num_range in input:
        for num in range(int(num_range.split('-')[0]), int(num_range.split('-')[1]) + 1):
            is_invalid = False
            split_num_list = [[str(num)[x:x+y] for x in range(0, len(str(num)), y)] for y in range(1,len(str(num))//2 + 1) if len(str(num))%y == 0]
            for split_num in split_num_list:
                if len(set(split_num)) == 1:
                    is_invalid = True
            sum += int(num) * is_invalid
    return sum

print(invalid_ID_sum2(input))