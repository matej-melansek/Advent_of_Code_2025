import numpy as np
from collections import defaultdict, deque

input = []
with open('inputs/day8.txt', 'r') as file:
    for line in file:
        input.append(np.array([int(x) for x in line.strip().split(',')]))

def all_distances(junction_boxes):
    distances = {}
    for i in range(len(junction_boxes)-1):
        for j in range(i + 1, len(junction_boxes)):
            dist = np.linalg.norm(junction_boxes[i] - junction_boxes[j])
            distances[(i, j)] = dist
    return distances

# STOLEN FROM CHATGPT
def merge_connected(pairs):
    graph = defaultdict(set)
    for a, b in pairs:
        graph[a].add(b)
        graph[b].add(a)

    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            queue = deque([node])
            comp = []

            while queue:
                cur = queue.popleft()
                if cur not in visited:
                    visited.add(cur)
                    comp.append(cur)
                    queue.extend(graph[cur] - visited)
            components.append(tuple(sorted(comp)))
    return components


test_input = [np.array([162,817,812]), np.array([57,618,57]), np.array([906,360,560]),np.array([592,479,940]),np.array([352,342,300]),np.array([466,668,158]),np.array([542,29,236]),np.array([431,825,988]),np.array([739,650,466]),np.array([52,470,668]),np.array([216,146,977]),np.array([819,987,18]),np.array([117,168,530]),np.array([805,96,715]),np.array([346,949,466]),np.array([970,615,88]),np.array([941,993,340]),np.array([862,61,35]),np.array([984,92,344]),np.array([425,690,689])]

def part1(junction_boxes, cutoff=1000):
    distances = all_distances(junction_boxes)
    sorted_distances = [set(x) for x in sorted(distances, key=distances.get)[:cutoff]]
    merged = merge_connected(sorted_distances)
    sorted_merged = sorted(merged, key=len, reverse=True)
    return sorted_merged

part1_result = part1(input)
print(f'Part 1: {len(part1_result[0])*len(part1_result[1])*len(part1_result[2])}')

# STOLE KRUSKAL ALGORITHM FROM WIKIPEDIA
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x] += 1

def kruskal_mst(junction_boxes):
    graph_dict = all_distances(junction_boxes)
    edges = []
    for (u, v), weight in graph_dict.items():
        edges.append((weight, u, v))
    
    edges.sort()
    
    parent = list(range(len(junction_boxes)))
    rank = [0] * len(junction_boxes)
    mst_edges = []
    total_weight = 0

    edge_count = 0
    for weight, u, v in edges:
        x = find(parent, u)
        y = find(parent, v)
        
        if x != y:
            mst_edges.append((u, v, weight))
            union(parent, rank, x, y)
            total_weight += weight
            edge_count += 1
            if edge_count == len(junction_boxes) - 1:
                break
    last_pair1, last_pair2 = mst_edges[-1][0], mst_edges[-1][1]
    result = junction_boxes[last_pair1][0]*junction_boxes[last_pair2][0]
    return result, mst_edges, total_weight

part2_result = kruskal_mst(input,1000)
print(f'Part 2: {part2_result[0]}')