from select import select


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.heapifyUp(len(self.heap) - 1)
        print(val, self.heap)

    def extract_min(self):
        self.heap[0],  self.heap[-1] = self.heap[-1], self.heap[0]
        res = self.heap.pop()
        self.heapifyDown(0)
        return res

    def heapifyUp(self, index):
        while (index-1)//2 >= 0:
            parent_index = (index-1)//2
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] \
                    = self.heap[index], self.heap[parent_index]
                index = (index-1)//2
            else:
                break

    def heapifyDown(self, index):
        while index >= 0:
            min_child = self.min_child(index)
            if not min_child:
                return

            if self.heap[min_child] < self.heap[index]:
                self.heap[min_child], self.heap[index] \
                    = self.heap[index], self.heap[min_child]
                index = min_child
            else:
                break

    def min_child(self, index):
        if 2*index+1 >= len(self.heap):
            return None
        if 2*index+2 >= len(self.heap):
            return 2*index+1
        else:
            return 2*index+2 if self.heap[2*index+2] < self.heap[2*index+1] else 2*index+1


m = MinHeap()
m.insert(10)
m.insert(1)
m.insert(-10)
m.insert(0)
print(m.extract_min())
m.insert(-2)
m.insert(110)
print(m.extract_min())
m.insert(120)
print(m.extract_min())
print(m.extract_min())
print(m.extract_min())
print(m.extract_min())