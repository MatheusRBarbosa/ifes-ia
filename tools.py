# Arquivo para conter qualquer logica auxiliar sem ser do algoritimo
def read_text_file(file_path):
    file = open(file_path, 'r')
    map = []
    
    for line in file:
        map_line = []
        for node in line:
            if( node != "\n" and node != " "):
                map_line.append(node)
        map.append(map_line)
    
    return map


def print_map(map, initial_node, final_node, result=None):
    map_copy = map

    if result != None:
        for node in result:
            map_copy[node[0]][node[1]] = "#"

    map_copy[initial_node[0]][initial_node[1]] = "S"
    map_copy[final_node[0]][final_node[1]] = "G"

    for line in map_copy:
        print(line)

def check_inputs(inputs, map):
    m = len(map)
    n = len(map[0])

    for node in inputs:
        if (node[0] > m - 1 or node[1] > n - 1 ):
            print("Erro! Input esta apontando para uma posicao fora da matriz")
            return False
        if (map[node[0]][node[1]] == '1'):
            print("Erro! Input esta em cima de obstaculo")
            return False
    return True