import sys
from tools import *
from star import *

def main():
    if len(sys.argv) == 2:
        map = read_text_file(sys.argv[1])

        initial_state = input("Entre com o x e y do estado inicial. Ex: 0 3: ")
        initial_state = tuple(int(x) for x in initial_state.split(" "))
        final_state = input("Entre com o x e y do estado final. Ex: 0 3: ")
        final_state = tuple(int(x) for x in final_state.split(" "))

        print_map(map, initial_state, final_state)
    else:
        print("Erro! Favor informar arquivo do mapa")

main()