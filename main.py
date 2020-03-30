import sys
from tools import *
from star import *

def main():
    if len(sys.argv) >= 2:

        map = read_text_file(sys.argv[1])

        if len(sys.argv) == 6:
            initial_node = tuple([int(sys.argv[2]), int(sys.argv[3])])
            final_node = tuple([int(sys.argv[4]), int(sys.argv[5])])
        else:
            initial_node = input("Entre com o x e y do estado inicial. Ex: 0 3: ")
            initial_node = tuple(int(x) for x in initial_node.split(" "))
            final_node = input("Entre com o x e y do estado final. Ex: 0 3: ")
            final_node = tuple(int(x) for x in final_node.split(" "))

        print("=== Matriz inicial ===")
        print_map(map, initial_node, final_node)

        result = star_main(map, initial_node, final_node)
        
        print("=== Matriz com resultado ===")
        print_map(map, initial_node, final_node, result)
        
    else:
        print("Erro! Favor informar arquivo do mapa")

main()