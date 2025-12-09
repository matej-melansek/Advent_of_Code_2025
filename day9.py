import numpy as np
import matplotlib.pyplot as plt
input = []

with open('inputs/day9.txt', 'r') as file:
    for line in file:
        input.append([int(x) for x in line.strip().split(',')])

def largest_rectangle(red_tiles):
    largest = 0
    largest_pair = None
    for i in range(len(red_tiles)-2):
        for j in range(i+2,len(red_tiles)):
            rectangle = (abs(red_tiles[i][0]-red_tiles[j][0]) + 1)*(abs(red_tiles[i][1]-red_tiles[j][1]) + 1)
            if rectangle > largest:
                largest = rectangle
                largest_pair = (i,j)
    return largest, largest_pair, red_tiles[largest_pair[0]], red_tiles[largest_pair[1]]

test = [[7,1],[11,1],[11,7],[9,7],[9,5],[2,5],[2,3],[7,3]]

def are_all_corners(red_tiles):
    dir = None
    all_corners = True
    for i in range(len(red_tiles)-1):
        new_dir = None
        if red_tiles[i][0]-red_tiles[i+1][0] == 0:
            new_dir = 'x'
        else:
            new_dir = 'y'
        if dir == new_dir:
            all_corners = False
            break
    print(f'Are all red tiles corners: {all_corners}')
are_all_corners(input)

def list_largest_rectangles(red_tiles):
    list_of_rectangles = []
    for i in range(len(red_tiles)-2):
        for j in range(i+2,len(red_tiles)):
            rectangle = (abs(red_tiles[i][0]-red_tiles[j][0]) + 1)*(abs(red_tiles[i][1]-red_tiles[j][1]) + 1)
            list_of_rectangles.append((rectangle,i,j))
    return sorted(list_of_rectangles,reverse=True)

def all_edges(red_tiles):
    edges = []
    for i in range(len(red_tiles)):
        j = (i+1)%len(red_tiles)
        x1,y1 = red_tiles[i]
        x2,y2 = red_tiles[j]
        if x1-x2==0:
            edges.append(('x',x1,min(y1,y2),max(y1,y2)))
        else:
            edges.append(('y',y1,min(x1,x2),max(x1,x2)))    
    return edges

def largest_green_rectangle(red_tiles):
    sorted_rectangles = list_largest_rectangles(red_tiles)
    print(f'Part 1: {sorted_rectangles[0][0]}')
    edges = all_edges(red_tiles)
    for area,i,j in sorted_rectangles:
        x1,y1 = red_tiles[i]
        x2,y2 = red_tiles[j]
        x_min, x_max, y_min, y_max = min(x1,x2), max(x1,x2), min(y1,y2), max(y1,y2)
        intersects = False
        for direction,p,q,r in edges:
            if direction == 'x':
                if x_min < p < x_max and (y_min < q < y_max or y_min < r < y_max or (q <= y_min <= r and q <= y_max <= r)):
                    intersects = True
                    break
            else:
                if (x_min < q < x_max or x_min < r < x_max or (q <= x_min <= r and q <= x_max <= r)) and y_min < p < y_max:
                    intersects = True
                    break
        if not intersects:
            return area, red_tiles[i], red_tiles[j]
    return None

print(f'Part 2: {largest_green_rectangle(input)[0]}')