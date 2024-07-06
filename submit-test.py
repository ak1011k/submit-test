graph = {}

while True:
    try:
        line = input() 
        if line == "":
            break
        

        parts = line.split(',')
        start = int(parts[0].strip())
        end = int(parts[1].strip())
        distance = float(parts[2].strip())
        

        if start not in graph:
            graph[start] = []
        if end not in graph:
            graph[end] = []
        graph[start].append((end, distance))
        graph[end].append((start, distance))
    except EOFError:
        break


def find_path(node, visited, path, distance):
    visited.append(node)
    path.append(node)
    
    longest_path = path[:]
    max_distance = distance
    
    for neighbor, weight in graph[node]:
        if neighbor not in visited:
            new_visited = visited[:]
            new_path = path[:]
            new_path, new_distance = find_path(neighbor, new_visited, new_path, distance + weight)
            if new_distance > max_distance:
                longest_path = new_path
                max_distance = new_distance
    
    return longest_path, max_distance


longest_path = []
max_distance = 0

for start_node in graph:
    path, distance = find_path(start_node, [], [], 0)
    if distance > max_distance:
        longest_path = path
        max_distance = distance


for node in longest_path:
    print(node)