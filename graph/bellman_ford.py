def bellman_ford_shortest_path(src, edges, nodes):
    sp = {node: float('inf') for node in nodes}
    sp[src] = 0
    pred = {node: None for node in nodes}

    for i in range(len(nodes)-1):
        for u, v, w in edges:
            if sp[v] > sp[u] + w:
                sp[v] = sp[u] + w
                pred[v] = u

    return sp, pred


def bellman_ford_negative_cycle(sp, pred):
    cycle_nodes, reachable_vertex = [], None

    for i in range(len(pred)-1):
        for u, v, w in edges:
            if sp[v] > sp[u] + w:
                reachable_vertex = v
                sp[v] = sp[u] + w
                pred[v] = u

    if reachable_vertex:
        visited = {node: False for node in pred}

        while not visited[reachable_vertex]:
            visited[reachable_vertex] = True
            reachable_vertex = pred[reachable_vertex]

        visited = {node: False for node in pred}

        while not visited[reachable_vertex]:
            visited[reachable_vertex] = True
            cycle_nodes.append(reachable_vertex)
            reachable_vertex = pred[reachable_vertex]

    return cycle_nodes


adjacent_list_no_neg_cycle = {
    's': [('t', 6), ('y', 7)],
    't': [('x', 5), ('z', -4), ('y', 8)],
    'y': [('x', -3), ('z', 9)],
    'x': [('t', -2)],
    'z': [('s', 2), ('x', 7)]
}

adjacent_list_neg_cycle = {
    's': [('t', 6), ('y', 7)],
    't': [('x', -5), ('z', -4), ('y', 8)],
    'y': [('x', -3), ('z', 9)],
    'x': [('t', -2)],
    'z': [('s', 2), ('x', -7)]
}

adjacent_list = adjacent_list_neg_cycle

edges = [(k, edge[0], edge[1]) for k in adjacent_list for edge in adjacent_list[k]]
sp, pred = bellman_ford_shortest_path('s', edges, adjacent_list.keys())
cycle_nodes = bellman_ford_negative_cycle(sp, pred)
print(cycle_nodes)
