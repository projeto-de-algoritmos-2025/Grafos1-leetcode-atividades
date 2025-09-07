class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        #Inicializa as variaveis

        #criação do grafo baseado nas conexões
        grafo = [[] for _ in range(n)]
        for a, b in connections:
            grafo[a].append(b)
            grafo[b].append(a)

        time = 0
        disc = [-1] * n
        low = [-1] * n
        resposta = []
        #DFS adaptada com a logica de detecção de SCC, é iterado para cada nó a partir do nó v
        #chamando outras funções de DFS , gerando assim recursão, é calculado a distancia percorrida para a volta
        #pela recursão  por arestas alternativas, caso não consiga isso determina uma bridge ou ponto critico
        
        def dfs(v, pai):
            nonlocal time
            disc[v] = low[v] = time
            time += 1
            for w in grafo[v]:
                if w == pai:
                    continue
                if disc[w] == -1:
                    dfs(w, v)
                    low[v] = min(low[v], low[w])
                    if low[w] > disc[v]:
                        resposta.append([v, w])
                else:
                    low[v] = min(low[v], disc[w])
 # A busca em profundidade é executada para todos os nós não visitados
        for v in range(n):
            if disc[v] == -1:
                dfs(v, -1)

        return resposta
