def floyd_warshall(edges, n):
    sp = [[float('inf')]*n for i in range(n)]

    for u in range(n):
        for v in range(n):
            if u == v:
                sp[u][v] = 0
            else:
                sp[u][v] = edges.get((u+1, v+1), float('inf'))

    for x in range(n):
        for u in range(n):
            for v in range(n):
                if sp[u][v] > sp[u][x] + sp[x][v]:
                    sp[u][v] = sp[u][x] + sp[x][v]

    return sp


edges = {
    (1, 2): 3,
    (1, 3): 8,
    (2, 4): 1,
    (3, 2): 4,
    (4, 1): 2,
    (4, 3): -5
}

print(floyd_warshall(edges, 4))

