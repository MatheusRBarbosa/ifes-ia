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


def print_map(map, initial_state, final_state, result=None):
    map_copy = map

    if result != None:
        for node in result:
            map_copy[node[0]][node[1]] = "#"

    map_copy[initial_state[0]][initial_state[1]] = "S"
    map_copy[final_state[0]][final_state[1]] = "G"

    for line in map_copy:
        print(line)


            

    