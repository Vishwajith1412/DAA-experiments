import heapq

def dijkstra(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    prev = [None] * n

    dist[source] = 0
    pq = [(0, source)]
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, prev


def reconstruct_path(prev, source, target):
    path = []

    while target is not None:
        path.append(target)
        target = prev[target]

    path.reverse()

    if path and path[0] == source:
        return path

    return []


# ----------- Random Graph -----------

graph = {
    0: [(1, 6), (2, 2)],
    1: [(3, 5), (4, 3)],
    2: [(1, 1), (4, 7)],
    3: [(5, 4)],
    4: [(3, 2), (5, 6)],
    5: [(6, 3)],
    6: []
}

source = 0

dist, prev = dijkstra(graph, source)

print(f"Shortest paths from vertex {source}\n")

print(f"{'Vertex':<10}{'Distance':<12}{'Path'}")
print("-" * 45)

for v in range(len(graph)):
    path = reconstruct_path(prev, source, v)
    path_str = " -> ".join(map(str, path)) if path else "No Path"

    distance = dist[v] if dist[v] != float('inf') else "INF"

    print(f"{v:<10}{distance:<12}{path_str}")
