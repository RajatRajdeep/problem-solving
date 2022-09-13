import heapq
import itertools

REMOVED = 'REMOVED'


class PriorityQueue:
    def __init__(self):
        self.entry_finder = {}
        self.queue = []
        self.counter = itertools.count()

    def add_task(self, priority, task):
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        self.entry_finder[task] = [priority, count, task]
        heapq.heappush(self.queue, self.entry_finder[task])

    def remove_task(self, task):
        self.entry_finder[task][-1] = REMOVED
        del self.entry_finder[task]

    def pop_task(self):
        while self.queue:
            _, _, task = heapq.heappop(self.queue)
            if task is not REMOVED:
                self.remove_task(task)
                return task

    def is_empty(self):
        return not bool(self.queue)
