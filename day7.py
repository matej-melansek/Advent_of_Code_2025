input = []

with open('inputs/day7.txt', 'r') as file:
    for line in file:
        input.append(line.strip())

def beam_through_splitters(input):
    result = 0
    beam_picture = [input[0]]
    current_beam = [input[0].index('S')]
    for line in input[1:]:
        new_beam = list()
        beam_picture_line = line
        for i in current_beam:
            if line[i] == '.':
                new_beam.append(i)
                beam_picture_line = beam_picture_line[:i] + '|' + beam_picture_line[i+1:]
            elif line[i] == '^':
                result += 1
                if i+1 < len(line):
                    new_beam.append(i+1) if i+1 not in new_beam else None
                    beam_picture_line = beam_picture_line[:i+1] + '|' + beam_picture_line[i+2:]
                if i-1 >= 0:
                    new_beam.append(i-1) if i-1 not in new_beam else None
                    beam_picture_line = beam_picture_line[:i-1] + '|' + beam_picture_line[i:]
        beam_picture.append(beam_picture_line)
        current_beam = new_beam
    return beam_picture

test_input = [
'.......S.......',
'...............',
'.......^.......',
'...............',
'......^.^......',
'...............',
'.....^.^.^.....',
'...............',
'....^.^...^....',
'...............',
'...^.^...^.^...',
'...............',
'..^...^.....^..',
'...............',
'.^.^.^.^.^...^.',
'...............']


def part1(picture,show_picture=False):
    result = 0
    for i in range(len(picture)):
        if show_picture:
            print(picture[i])
        line = picture[i]
        for j in range(len(line)):
            if line[j] == '^' and picture[i-1][j] == '|':
                result += 1
    return result

print(f'Part 1: {part1(beam_through_splitters(input))}')


def beam_through_splitters_dict(input):
    current_beam = [input[0].index('S')]
    beam_dict = {(0,current_beam[0]):1}
    for i in range(1,len(input)):
        line = input[i]
        new_beam = list()
        for j in current_beam:
            if line[j] == '.':
                if j not in new_beam:
                    new_beam.append(j)
                    beam_dict[(i,j)] = beam_dict[(i-1,j)]
                else:
                    beam_dict[(i,j)] += beam_dict[(i-1,j)]
            elif line[j] == '^':
                if j-1 not in new_beam:
                    new_beam.append(j-1)
                    beam_dict[(i,j-1)] = beam_dict[(i-1,j)]
                else:
                    beam_dict[(i,j-1)] += beam_dict[(i-1,j)]
                if j+1 not in new_beam:
                    new_beam.append(j+1)
                    beam_dict[(i,j+1)] = beam_dict[(i-1,j)]
                else:
                    beam_dict[(i,j+1)] += beam_dict[(i-1,j)]
        current_beam = new_beam
    return sum([value for (key1,key2),value in beam_dict.items() if key1 == len(input)-1])

print(f'Part 2: {beam_through_splitters_dict(input)}')