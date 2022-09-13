from priority_queue import PriorityQueue


def dijkstra(src, adjacent_list):
    sp = {}
    pred = {}

    for node in adjacent_list:
        sp[node] = float('inf')
    sp[src] = 0

    priority_queue = PriorityQueue()
    for node in sp:
        priority_queue.add_task(sp[node], node)

    while not priority_queue.is_empty():
        node = priority_queue.pop_task()
        if node is None:
            continue

        for adj_node, time in adjacent_list[node]:
            if sp[node] + time < sp[adj_node]:
                sp[adj_node] = sp[node] + time
                pred[adj_node] = node
                priority_queue.add_task(sp[adj_node], adj_node)
    return sp


adjacent_list = {
    's': [('t', 6), ('y', 4)],
    't': [('y', 2), ('x', 3)],
    'y': [('t', 1), ('x', 9), ('z', 3)],
    'x': [('z', 4)],
    'z': [('s', 7), ('x', 5)]
}

print(dijkstra('s', adjacent_list))
