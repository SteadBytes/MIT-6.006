class PriorityQueueSol:
    """Heap-based priority queue implementation."""

    def __init__(self):
        """Initially empty priority queue."""
        self.heap = [None]

    def __len__(self):
        # Number of elements in the queue.
        return len(self.heap) - 1

    def append(self, key):
        """Inserts an element in the priority queue."""
        if key is None:
            raise ValueError('Cannot insert None in the queue')

        i = len(self.heap)
        self.heap.append(key)
        while i > 1:
            parent = i // 2
            if key < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], key
                i = parent
            else:
                break

    def min(self):
        """Returns the smallest element in the queue."""
        return self.heap[1]

    def pop(self):
        """Removes the minimum element in the queue.

        Returns:
            The value of the removed element.
        """
        heap = self.heap
        popped_key = heap[1]
        if len(heap) == 2:
            return heap.pop()
        heap[1] = key = heap.pop()

        i = 1
        while True:
            left = i * 2
            if len(heap) <= left:
                break
            left_key = heap[left]
            right = i * 2 + 1
            right_key = right < len(heap) and heap[right]
            if right_key and right_key < left_key:
                child_key = right_key
                child = right
            else:
                child_key = left_key
                child = left
            if key <= child_key:
                break
            self.heap[i], self.heap[child] = child_key, key
            i = child
        return popped_key


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def append(self, key):
        if key is None:
            raise ValueError('Cannot insert None in the queue')
        self.heap.append(key)
        i = len(self) - 1
        while i > 0:  # and self.heap[self.parent(i)] > self.heap[i]:
            parent = self.parent(i)
            if key < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], key
                i = parent
            else:
                break

    def min(self):
        if len(self) == 0:
            return None
        return self.heap[0]

    def pop(self):
        if len(self) == 0:
            return None
        # min_ = self.heap.pop(0)
        # self.min_heapify(0)
        # return min_
        heap = self.heap
        popped_key = heap[0]
        if len(heap) == 1:
            return heap.pop()
        heap[0] = key = heap.pop()
        self.min_heapify(key)
        return popped_key
        # i = 0
        # while True:
        #     left = self.left(i)
        #     if len(heap) <= left:
        #         break
        #     left_key = heap[left]
        #     right = self.right(i)
        #     right_key = right < len(heap) and heap[right]
        #     if right_key and right_key < left_key:
        #         child_key = right_key
        #         child = right
        #     else:
        #         child_key = left_key
        #         child = left
        #     if key <= child_key:
        #         break
        #     self.heap[i], self.heap[child] = child_key, key
        #     i = child
        # return popped_key

    def parent(self, i):
        return i // 2

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def min_heapify(self, key):
        heap = self.heap
        i = 0
        while True:
            left = self.left(i)
            if len(heap) <= left:
                break
            left_key = heap[left]
            right = self.right(i)
            right_key = right < len(heap) and heap[right]
            if right_key and right_key < left_key:
                child_key = right_key
                child = right
            else:
                child_key = left_key
                child = left
            if key <= child_key:
                break
            self.heap[i], self.heap[child] = child_key, key
            i = child


def print_tree(A, i=0, indent=0):
    if i < len(A):
        print'  ' * indent, A[i]
        print_tree(A, i * 2 + 1, indent + 1)
        print_tree(A, i * 2 + 2, indent + 1)


if __name__ == '__main__':
    queues = [PriorityQueue(), PriorityQueueSol()]
    items = [5, 3, 9, 6, 5, 100, 50, 2]

    for i in items:
        for q in queues:
            q.append(i)
    for q in queues:
        print q.heap
    for i in range(len(items)):
        print ' '.join([str(q.pop()) for q in queues])
