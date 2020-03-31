# Inteligencia Artificial

#### Membros
Matheus Barbosa - 20152bsi0218

## Relatório - Implementação do A*

### Problema

O problema proposto consiste em um robô achar um caminho de um ponto de origem até um ponto destino dentro de um determinado mapa sem colidir com nenhum obstáculo.

![mapa](https://github.com/MatheusRBarbosa/ifes-ia-a-estrela/blob/master/img/mapa.png)

A imagem acima representa o mapa em questão. Onde o quadradro vermelho representa o inicio, o verde o final e os pretos os obstáculos. 

O problema também determina que o robô também pode fazer movimentos apenas em 90 graus, ou seja, não pode realizar movimentos em diagonais.

### Solução
A solução usada neste trabalho consiste no algoritimo de A* ( A-estrela ) usando a heurística de manhattan seguindo a seguinte fórmula matemática:

**f(n) = g(n) + h(n)**

Onde **g(n)** é a distância do ponto atual até o objetivo final, **h(n)** é o valor da heurística de manhattan e por fim, **f(n)** é a distância percorrida pelo nó.

#### Organização do código
O código está separado em três arquivos. **main.py**, **star.py** e **tools.py**.

**tools.py** é o arquivo que contém as funções auxiliares, como `print_map`, `read_text_file`, `check_inputs`. Que são funções que não fazem parte da lógica do algoritimo do A*.

**star.py** é o arquivo eu contém todas as funções da lógica do algoritimo A*.

**main.py** é o arquivo principal, que usa os outros arquivos para juntar tudo e interagir o o usuário do programa.
