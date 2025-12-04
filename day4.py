import functools
inputs = []

with open('inputs/day4.txt', 'r') as file:  
    for line in file:
        inputs.append(line.strip())

test= ['..@@.@@@@.','@@@.@.@.@@','@@@@@.@.@@','@.@@@@..@.','@@.@@@@.@@','.@@@@@@@.@','.@.@.@.@@@','@.@@@.@@@@','.@@@@@@@@.','@.@.@@@.@.']

def accessible_papers(paper_map): 
    accessible_count = 0
    rows = len(paper_map)
    cols = len(paper_map[0])
    dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

    paper_map[1] = paper_map[1].replace('x','.')
    for r in range(1,rows-1):
        paper_map[r+1] = paper_map[r+1].replace('x','.')
        for c in range(1,cols-1):
            current = paper_map[r][c]
            if current == '@':
                num_neighbours = 0
                for (dir1,dir2) in dirs:
                    neighbour = paper_map[r+dir1][c+dir2]
                    if  neighbour== '@' or neighbour == 'x':
                        num_neighbours += 1
                if num_neighbours < 4:
                    accessible_count += 1
                    paper_map[r] = paper_map[r][:c] + 'x' + paper_map[r][c+1:]
    return accessible_count, paper_map


def part_1(paper_map):
    paper_map = [(len(paper_map[0])+2)*'-'] + ['|'+row+'|' for row in paper_map] + [(len(paper_map[0])+2)*'-']
    return accessible_papers(paper_map)[0]

def part_2(paper_map):
    paper_map = [(len(paper_map[0])+2)*'-'] + ['|'+row+'|' for row in paper_map] + [(len(paper_map[0])+2)*'-']
    total_accessible = 0
    while True:
        accessible_count, paper_map = accessible_papers(paper_map)
        if accessible_count == 0:
            break
        total_accessible += accessible_count
    return total_accessible

print(f"Part 1: {part_1(inputs)}")
print(f"Part 2: {part_2(inputs)}")