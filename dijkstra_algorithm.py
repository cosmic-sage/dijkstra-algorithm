import math

def dijkstra(graph, source):
    V = len(graph)
    dist = [math.inf] * V
    dist[source] = 0
    visited = [False] * V

    for _ in range(V):
        u = min((d, i) for i, d in enumerate(dist) if not visited[i])[1]
        visited[u] = True

        for v in range(V):
            if graph[u][v] != math.inf and not visited[v]:
                if dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]

    return dist