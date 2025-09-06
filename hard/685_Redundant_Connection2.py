class Solution(object):
    def findRedundantDirectedConnection(self, arestas):
        """
        :type arestas: List[List[int]]
        :rtype: List[int]
        """
        pai = {}           
        cand1 = cand2 = None 

# A DFS (busca em profundidade) é usada para detectar ciclos no grafo direcionado.
# "visitado" marca os nós que já foram completamente processados.
# "caminho" marca os nós no caminho atual da DFS.
# Se durante a DFS chegarmos a um vizinho que já está em "caminho", significa que há um ciclo.

        for origem, destino in arestas:
            if destino in pai:
                cand1 = [pai[destino], destino]
                cand2 = [origem, destino]
            else:
                pai[destino] = origem

        def tem_ciclo(grafo, no, visitado, caminho):
            visitado.add(no)
            caminho.add(no)
            for vizinho in grafo.get(no, []):
                if vizinho not in visitado:
                    if tem_ciclo(grafo, vizinho, visitado, caminho):
                        return True
                elif vizinho in caminho:
                    return True
            caminho.remove(no)
            return False

        
        grafo = {}
        for origem, destino in arestas:
            if [origem, destino] == cand2:
                continue
            grafo.setdefault(origem, []).append(destino)

        visitado = set()
        ciclo = False
        for no in range(1, len(arestas) + 1):
            if no not in visitado:
                if tem_ciclo(grafo, no, visitado, set()):
                    ciclo = True
                    break

        # - Dois pais + ciclo -> remover primeira aresta
        # - Dois pais sem ciclo -> remover segunda aresta
        if cand1 and cand2:
            return cand1 if ciclo else cand2

        # Se não há dois pais, remover a aresta que fecha o ciclo
        grafo = {}
        for origem, destino in arestas:
            grafo.setdefault(origem, []).append(destino)

        for origem, destino in reversed(arestas):
            grafo_temp = {k: v[:] for k, v in grafo.items()}
            grafo_temp[origem].remove(destino)

            visitado_temp = set()
            ciclo_temp = False
            for no in range(1, len(arestas) + 1):
                if no not in visitado_temp:
                    if tem_ciclo(grafo_temp, no, visitado_temp, set()):
                        ciclo_temp = True
                        break
            if not ciclo_temp:
                return [origem, destino]