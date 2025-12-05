fresh_ranges = dict()
ingredient_ids = list()

with open('inputs/day5.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if '-' in line:
            bounds = line.split('-')
            start = int(bounds[0])
            end = int(bounds[1])
            fresh_ranges[start] = max(end,fresh_ranges[start]) if start in fresh_ranges else end
        elif line != '':
            ingredient_ids.append(int(line))

test_ranges = {3:5, 10:14, 16:20, 12:18}
test_ids = [1,5,8,11,17,32]


def fresh_count(ranges, ids):
    count = 0
    for ingredient_id in ids:
        for start in ranges:
            end = ranges[start]
            if start <= ingredient_id <= end:
                count += 1
                break
    return count

print(f'Part 1: The number of fresh ingredients is {fresh_count(fresh_ranges, ingredient_ids)}')
        
def possible_fresh_ingredients(ranges):
    fixed_ranges = ranges.copy()
    sorted_ranges_list = sorted(ranges.keys())
    count = 0
    for i in range(len(sorted_ranges_list)):
        key = sorted_ranges_list[i]
        if key in fixed_ranges.keys():
            end = ranges[key]
            try:
                next_key = sorted_ranges_list[i + 1]
            except IndexError:
                count += end - key + 1
                break
            j = 1
            while end >= next_key:
                fixed_ranges[key] = max(fixed_ranges[key], fixed_ranges[next_key])
                end = max(end, fixed_ranges[next_key])
                del fixed_ranges[next_key]
                j += 1
                try:
                    next_key = sorted_ranges_list[i + j]
                except IndexError:
                    break
            count += fixed_ranges[key] - key + 1
    return count
   
print(f'Part 2: The number of possible fresh ingredients is {possible_fresh_ingredients(fresh_ranges)}')