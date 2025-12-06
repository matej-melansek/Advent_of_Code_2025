import numpy as np

number_lines = list()
operations_line = None
input_numbers = list()
input_operations = list()

with open('inputs/day6.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line[0] in '+*-/':
            input_operations = line.split()
            operations_line = line
        else:
            input_numbers.append([int(x) for x in line.split()])    
            number_lines.append(line) 
    input_numbers = np.array(input_numbers, dtype=np.int64).transpose()   

def apply_operations(matrix, operations):
    results = []
    for i in range(len(matrix)):
        row = matrix[i]
        if operations[i] == '+':
            result = np.sum(row)
        elif operations[i] == '*':
            result = np.prod(row)
        results.append(result)
    return sum(results)#, results

print(f'Part 1:{apply_operations(input_numbers, input_operations)}')

def cephalopods_notation(number_lines, operations_line):
    spaces_loc = [i for i, char in enumerate(operations_line) if char != ' ']
    spaces_loc.append(len(number_lines[0])+1)
    previous_location = spaces_loc[0]
    results = 0
    for location in spaces_loc[1:]:
        numbers = list()
        for i in range(previous_location,location-1):
            number =int(''.join([number_lines[j][i] for j in range(len(number_lines))]))
            numbers.append(number)
        if operations_line[previous_location] == '+':
            results += sum(numbers)
        elif operations_line[previous_location] == '*':
            results += np.prod(numbers,dtype=np.int64)
        previous_location = location
    return results

test_numbers = ['123 328  51 64 ',
                ' 45 64  387 23 ',
                '  6 98  215 314']
test_operations = '*   +   *   + '

#print(f'Test Part 2:{cephalopods_notation(test_numbers, test_operations)}')
print(f'Part 2:{cephalopods_notation(number_lines, operations_line)}')