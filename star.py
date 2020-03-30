# Arquivo para mantar a logica do algoritimo A estrela

def result(node, path, map):
    p = []
    p.append(node)
    while path[node] != None:
        p.append(path[node])
        node = path[node]
    p = p[::-1]
    return p

# Calcula a distancia do ponto passado ate o ponto final
def calc_goal_distance(node, final_node):
    dx = abs(node[0] - final_node[0])
    dy = abs(node[1] - final_node[1])
    
    return dx + dy

def find_best_node(open_list, heuristic):
    best_heuristic = 1000000000
    current_index = 0

    for index, node in enumerate(open_list):
        if (heuristic[node] < best_heuristic):
            
            best_heuristic = heuristic[node]
            current_index = index
    
    return current_index

def find_next_nodes(current_node, map):
    m = len(map)
    n = len(map[0])

    i = current_node[0]
    j = current_node[1]

    next_nodes = []
    if i > 0 and map[i - 1][j] != '1':
        next_nodes.append((i - 1, j))
    
    if (i + 1) < m and map[i + 1][j] != '1':
        next_nodes.append((i + 1, j))

    if j > 0 and map[i][j - 1] != '1':
        next_nodes.append((i, j - 1))
    
    if (j + 1) < n and map[i][j + 1] != '1':
        next_nodes.append((i, j + 1))
    
    return next_nodes

def star_main(map, initial_node, final_node):
    found = False
    open_list = []
    closed_list = []

    path = {}
    path[initial_node] = None
    h = {}

    # Distancia percorrida
    f = 0
    # Distancia para o objetivo
    g = calc_goal_distance(initial_node, final_node)
    # heuristica
    h[initial_node] = f + g

    open_list.append(initial_node)
    
    while len(open_list) > 0:
        current_index = find_best_node(open_list, h)
        current_node = open_list.pop(current_index)
       
        if (current_node == final_node):
            found = True
            break
        
        next_nodes = find_next_nodes(current_node, map)
        closed_list.append(current_node)

        for next_node in next_nodes:
            if next_node not in closed_list and next_node not in open_list:
                open_list.append(next_node)
                if next_node not in h.keys():
                    f += 1
                    h[next_node] = calc_goal_distance(next_node, final_node) + f
                    path[next_node] = current_node
    
    if found == True:
        return result(current_node, path, map)
