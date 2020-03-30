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


def print_map(map, initial_state, final_state):
    map_copy = map
    map_copy[initial_state[0]][initial_state[1]] = "S"
    map_copy[final_state[0]][final_state[1]] = "G"
    
    for i in range(len(map_copy)):
        for j in range(len(map_copy[i])):
            if (map_copy[i][j] == '0'):
                map_copy[i][j] = " "
            elif (map_copy[i][j] == '1'):
                map_copy[i][j] = "|"
        print(map_copy[i])


            

    