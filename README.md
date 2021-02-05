# Inteligencia Artificial

### Membros
Ana Carolina Cebin Pereira - 20152bsi0188
Matheus Kleber Rodrigues Barbosa - 20152bsi0218

# Relatório - Implementação do A*

## Explicação teórica do algoritmo
## Problema

O problema proposto consiste em um robô achar um caminho de um ponto de origem até um ponto destino dentro de um determinado mapa sem colidir com nenhum obstáculo.

![mapa](https://github.com/MatheusRBarbosa/ifes-ia-a-estrela/blob/master/img/mapa.png)

A imagem acima representa o mapa em questão. Onde o quadrado vermelho representa o início, o verde, o final e os pretos, os obstáculos.

O problema também determina que o robô pode fazer apenas movimentos em 90 graus, ou seja, não pode realizar movimentos em nenhuma diagonal.

## Solução
A solução usada neste trabalho consiste no algoritimo de A* ( A-estrela ) usando a heurística de manhattan seguindo a seguinte fórmula matemática:

**f(n) = g(n) + h(n)**

Onde **g(n)** é a distância do ponto atual até o objetivo final, **h(n)** é o valor da heurística e por fim, **f(n)** é a distância percorrida pelo nó.

### Organização do código
O código está separado em três arquivos: **main.py**, **star.py** e **tools.py**.

**tools.py** é o arquivo que contém as funções auxiliares, como `print_map`, `read_text_file`, `check_inputs`. Que são funções que não fazem parte da lógica do algoritimo do A*.

**star.py** é o arquivo eu contém, exclusivamente, todas as funções da lógica do algoritimo A*.

**main.py** é o arquivo principal, que usa os outros arquivos para juntar tudo e interagir com o usuário do programa.

### Implementação

Nesse relatório só será apresentado os principais detalhes da solução. Para visualizar a solução completa basta acessar os arquivos do código fonte.

```python
def star_main(map, initial_node, final_node):
  # Conjunto de listas de nos para perrcorer e nos percorridos
  open_list = []
  closed_list = []

  # Dicionario para armazenar os nos que ja foram percorridos
  path = {}
  path[initial_node] = None

  # Flag para indicar se o goal foi encontrado
  found = False

  # Distancia percorrida
  f = 0

  # Distancia para o objetivo
  g = calc_goal_distance(initial_node, final_node)

  # heuristica
  h = {}
  h[initial_node] = f + g

  open_list.append(initial_node)
```
O código acima é a principal função do algoritmo, a função começa com a definição das principais variáveis e listas usadas na solução. A função `calc_goal_distance(node, final_node)` calcula a distância do nó atual (`node`) até o nó destino (`final_node`).

Após a inicialização das variaveis na `star_main`, é necessário criar uma lógica que verifique o custos dos nós a serem percorridos dentro de `open_list`.

```python
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

```
O primeiro passo é encontrar o nó com o melhor valor da heurística. Essa façanha é realizada na função `find_best_node`, que retorna a posição (de dentro da lista passada como parâmetro) do nó que possui o menor valor da heurística.

Após ter encontrado o nó com o melhor valor de heurística dentro de `open_list`, basta remove-lo da lista, encontrar seus vizinhos através do método `find_next_nodes` e adiciona-lo em `closed_list` já que esse nó não será mais usado. 

A resposta de `find_next_nodes` é uma lista dos nós vizinhos, cada um desses nós deve ser adicionado em `open_list` para serem verificados. Para cada um desses nós também já é calculado seus respectivos valores de heurística e salvos em `path`, que é um dicionario dos caminhos percorridos.

O loop irá parar assim que o nó que estará sendo analisado (`current_node`) for igual ao nó final (`final_node`).

Logo:

```python
if found == True:
    return result(current_node, path, map)
```

A função `result` consiste em pegar o nó atual (que é igual ao nó final) e encontrar o caminho reverso dele, *"qual caminho que levou a chegar até o nó final"*. E retornar o conjuto de nós que compõe esse caminho.


## Resultados

Para se realizar testes no programa, o usuário deve passar três paramêtros, o **mapa**, **par de coordenadas de início**, **par de coordenadas de objetivo final**

Exemplo:<br>
`python main.py mapa.txt`<br>
`>> Entre com o x e y do nó inicial. Ex: 0 3: 0 2`<br>
`>> Entre com o x e y do nó final. Ex: 0 3: 4 4`<br>

Ou simplesmente:

`python main.py mapa.txt 0 2 4 4`<br>

Ao executar o programa, no console será impresso duas matrizes, a de entrada e de resultado onde:

**0** - É um espaço livre que pode ser percorrido <br>
**1** - Representa um espaço ocupado por um obstáculo <br>
**S** - Indicia o nó inicial <br>
**G** - Indica o nó final <br>
**#** - Indica o caminho percorrido saindo de **S** e indo para **G** <br>

Usando o nó inicial em `(0, 0)` e o final em `(4, 4)` o resultado de saída será:

```
 === Matriz inicial ===
['S', '0', '1', '0', '0', '0', '0', '0', '0', '0']
['0', '0', '1', '0', '0', '0', '0', '0', '0', '0']
['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
['0', '0', '0', '0', '0', '1', '0', '0', '0', '0']
['1', '1', '1', '0', 'G', '1', '0', '0', '0', '0']
['0', '0', '0', '0', '0', '1', '0', '0', '0', '0']
['0', '0', '0', '0', '0', '0', '0', '0', '1', '1']
['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
['0', '0', '0', '0', '1', '1', '1', '0', '0', '0']
['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']

=== Matriz com resultado ===
['S', '0', '1', '0', '0', '0', '0', '0', '0', '0']
['#', '0', '1', '0', '0', '0', '0', '0', '0', '0']
['#', '0', '0', '0', '0', '0', '0', '0', '0', '0']
['#', '#', '#', '#', '0', '1', '0', '0', '0', '0']
['1', '1', '1', '#', 'G', '1', '0', '0', '0', '0']
['0', '0', '0', '0', '0', '1', '0', '0', '0', '0']
['0', '0', '0', '0', '0', '0', '0', '0', '1', '1']
['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
['0', '0', '0', '0', '1', '1', '1', '0', '0', '0']
['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
```

Caso seja passado outros mapas ou outros nós iniciais e finais o resultado será semelhante, pois a solução é genérica a essas condições.

O programa também aceita uma flag adicional, `--arrows`, essa flag modifica os caracteres que serão impressos na matriz de resultado, serão usados: 

**!** - Indica que o robô foi para baixo <br>
**>** - Indica que o robô foi para direita <br>
**^** - Indica que o robô foi para cima <br>
**<** - Indica que o robô foi para esquerda <br>

<br>
Exemplo de execução:<br>

`python main.py mapa.txt --arrows`

ou

`python main.py mapa.txt 0 2 4 4 --arrows`

A matriz resultante será parecida com:

```
=== Matriz com resultado ===
['S', '0', '1', '0', '0', '0', '0', '0', '0', '0']
['!', '0', '1', '0', '0', '0', '0', '0', '0', '0']
['!', '0', '0', '0', '0', '0', '0', '0', '0', '0']
['>', '>', '>', '!', '0', '1', '0', '0', '0', '0']
['1', '1', '1', '>', 'G', '1', '0', '0', '0', '0']
['0', '0', '0', '0', '0', '1', '0', '0', '0', '0']
['0', '0', '0', '0', '0', '0', '0', '0', '1', '1']
['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
['0', '0', '0', '0', '1', '1', '1', '0', '0', '0']
['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
```

