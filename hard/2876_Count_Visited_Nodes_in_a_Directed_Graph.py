class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:

        #Inicializa as variaveis
        n = len(edges)
        resposta = [-1] * n 
        # 0 = não visitado / 1 = visitado / 2 = finalizado 
        visitado = [0] * n
        
        # Busca em profundidade onde é marcado o nó como visitado e o adicionando a arvore,
        # é verificado se o proximo nó esta ou não visitado, se sim é feita uma busca nesse nó,
        #  se não foi encontrado um ciclo e o tamanho do ciclo adicionado a resposta
        # ao final os nós não envolvidos no ciclos são adicionados e o nó marcado como 2
        # para evitar que a função se perca em loop
        def DFS(v,arvore) :
            visitado[v] = 1
            arvore.append(v)
            w = edges[v]
            if visitado[w] == 0:
                DFS(w,arvore)
            elif visitado[w] == 1:
                
                ciclo = arvore[arvore.index(w):]

                for no in ciclo :
                    resposta[no]=len(ciclo)
                    
            if resposta[v] == -1:
                resposta[v] = resposta[edges[v]] + 1
        
            visitado[v] = 2

            
        # A busca em profundidade é executada para todos os nós não visitados
        for v in range(n):
            if visitado[v] == 0:
                DFS(v,[])

        return resposta

        