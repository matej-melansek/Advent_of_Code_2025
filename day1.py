input = []

with open('inputs/day1.txt', 'r') as file:
    for line in file:
        input.append(line[:-1])

def turn_dial(turns, start):
    current = start
    dial = [start]
    for move in turns:
        if move[0] == 'L':
            current = (current - int(move[1:])) % 100
        elif move[0] == 'R':
            current = (current + int(move[1:])) % 100
        dial.append(current)
    return dial, dial.count(0)

(dial, zeros) = turn_dial(input, 50)
print(f"Pozicija po vseh obratih:{dial[-1]}, geslo: {zeros}" )

def turn_dial_pass_zero(turns, start):
    current = start
    past = start
    dial = [start]
    pass_zero = 0
    for move in turns:
        past = current
        if move[0] == 'L':
            current_inf = current - int(move[1:])
            current = current_inf % 100
            abs_current = abs(current_inf//100) 
            pass_zero += (abs_current if past != 0 else abs_current-1 if abs_current>0 else 0) 
        elif move[0] == 'R':
            current_inf = current + int(move[1:])
            current = current_inf % 100
            abs_current = abs(current_inf//100) 
            pass_zero += abs_current - 1 if current == 0 else abs_current
        dial.append(current)
        
    return dial.count(0) + pass_zero

pass_zeros = turn_dial_pass_zero(input, 50)
#pass_zeros_test = turn_dial_pass_zero(['R150', 'L200', 'L50'], 50)

print(f'Novo geslo: {pass_zeros}')