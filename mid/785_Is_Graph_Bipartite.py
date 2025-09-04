class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        # -1 significa "não visitado ainda"
        # 0 e 1 são as duas cores possíveis
        cor = [-1] * n
        
        # A busca em largura (BFS) é usada para percorrer cada componente do grafo.
        # A cada nó inicial ainda não visitado, ele é colocado na fila e recebe uma cor (0).
        # Em seguida, seus vizinhos são processados: se ainda não têm cor, recebem a cor oposta;
        # se já têm a mesma cor do nó atual, o grafo não é bipartido e retornamos False.
        # Caso contrário, a BFS continua até visitar todos os nós conectados.

        for inicio in range(n):
            
            # Se o nó ainda não foi colorido E tem vizinhos
            if cor[inicio] == -1 and graph[inicio]: 
                fila = [inicio]  
                cor[inicio] = 0

                while fila:
                    node = fila.pop(0)

                    # Percorre todos os vizinhos do nó atual
                    for vizinho in graph[node]:
                        if cor[vizinho] == -1: 
                            cor[vizinho] = 1 - cor[node] # vizinho recebe a cor oposta 
                            fila.append(vizinho) 
                        
                        # Se o vizinho já foi colorido com a mesma cor do nó atual,
                        # então o grafo NÃO é bipartido 
                        elif cor[vizinho] == cor[node]:
                            return False

        # se não tiver nenhum problema, ele vai retornar True indicado que o grafo é bipartido
        return True
